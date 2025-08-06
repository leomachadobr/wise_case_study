
import pandas as pd

# Wise palette from AP
WISE_COLORS = [
    "#1A4D3A", "#2E7D32", "#4CAF50", "#66BB6A",
    "#81C784", "#A5D6A7", "#C8E6C9", "#E8F5E8"
]

FUNNEL_MAP = {
    "Transfer Created": "Created",
    "Transfer Funded": "Funded",
    "Transfer Transferred": "Transferred",
}
STAGES = ["Created", "Funded", "Transferred"]

def normalize_events(df, dt_col="dt"):
    df = df.copy()
    df[dt_col] = pd.to_datetime(df[dt_col], utc=True, errors="coerce")
    df = df[df["event_name"].isin(FUNNEL_MAP)].assign(
        stage=lambda d: d["event_name"].map(FUNNEL_MAP)
    )
    df["stage"] = pd.Categorical(df["stage"], categories=STAGES, ordered=True)
    return df.sort_values(["user_id", dt_col, "stage"])

def attach_transfer_keys(df, dt_col="dt"):
    df = df.copy()
    df["transfer_idx"] = (df["stage"].eq("Created")).groupby(df["user_id"]).cumsum()
    df["is_orphan"] = (df["transfer_idx"] == 0) & df["stage"].ne("Created")
    df["orphan_seq"] = df.groupby("user_id")["is_orphan"].cumsum()
    df["transfer_key"] = df.apply(
        lambda r: f"{r.user_id}#O{int(r.orphan_seq):05d}" if r.is_orphan
        else f"{r.user_id}#N{int(r.transfer_idx):05d}",
        axis=1
    )
    return df

def build_transfer_level(df, dt_col="dt"):
    # First times per stage
    first_times = df.pivot_table(index="transfer_key", columns="stage", values=dt_col, aggfunc="min")\
                    .rename(columns={"Created":"created_dt","Funded":"funded_dt","Transferred":"transferred_dt"})

    # Boolean flags
    flags = df.pivot_table(index="transfer_key", columns="stage", values=dt_col, aggfunc="count")\
              .fillna(0).astype(bool).rename(columns={
                  "Created":"transfer_created","Funded":"transfer_funded","Transferred":"transfer_transferred"
              })

    # Metadata
    keep = ["user_id","region"] + [c for c in ("platform","experience") if c in df.columns]
    meta = df.drop_duplicates("transfer_key").set_index("transfer_key")[keep]

    # Orphan
    orphan = df.groupby("transfer_key")["is_orphan"].any()

    out = pd.concat([meta, first_times, flags, orphan], axis=1).reset_index()

    # Sequence pattern and status
    out["sequence_pattern"] = out.apply(
        lambda r: " → ".join([s for s,f in zip(STAGES,[r.transfer_created,r.transfer_funded,r.transfer_transferred]) if f]) or "Orphan",
        axis=1
    )
    def status(r):
        if r.transfer_transferred: return "settled"
        if r.transfer_funded:      return "partially_settled"
        if r.transfer_created:     return "unsettled"
        return "orphan_only"
    out["status"] = out.apply(status, axis=1)
    out = out.sort_values(["user_id","created_dt","funded_dt","transferred_dt"]).reset_index(drop=True)
    out["transfer_id"] = out.index + 1

    final_cols = [
        "transfer_id","transfer_key","user_id","region"
    ] + [c for c in ("platform","experience") if c in out.columns] + [
        "created_dt","funded_dt","transferred_dt",
        "transfer_created","transfer_funded","transfer_transferred",
        "sequence_pattern","status"
    ]
    return out[final_cols]

def daily_funnel(transfers_df):
    df = transfers_df.copy()
    df["created_date"] = pd.to_datetime(df["created_dt"]).dt.date
    grp = df.groupby(["created_date","region","platform","experience"], dropna=False)
    daily = grp.agg(
        created=("transfer_created","sum"),
        funded=("transfer_funded","sum"),
        transferred=("transfer_transferred","sum")
    ).reset_index()

    daily["failure_rate"] = (daily["created"] - daily["transferred"]).div(daily["created"]).fillna(0)
    daily["success_rate"] = 1 - daily["failure_rate"]

    sort_cols = ["region","platform","experience","created_date"]
    daily = daily.sort_values(sort_cols)
    daily["success_rate_ma7"] = daily.groupby(["region","platform","experience"], dropna=False)["success_rate"]\
                                 .transform(lambda s: s.rolling(7, min_periods=1).mean())
    return daily

def global_daily(daily):
    g = daily.groupby("created_date", as_index=False).agg(
        created=("created","sum"),
        funded=("funded","sum"),
        transferred=("transferred","sum")
    )
    g["failure_rate"] = (g["created"] - g["transferred"]).div(g["created"]).fillna(0)
    g["success_rate"] = 1 - g["failure_rate"]
    g = g.sort_values("created_date")
    g["success_rate_ma7"] = g["success_rate"].rolling(7, min_periods=1).mean()
    return g
