## Analysis Plan - Wise regional expansion

**Context and Goal** Wise has launched a new currency route (MXN -> USD). With the data in our power [[src/wise_funnel_events.csv]] we want to evaluate. (i) Wether the launch is on track (ii) possible issues that we'd like to share with the product team.

## Important Info

**Customer Happy Path** A customer uses wise to transfer money abroad or keep money into an international currency account, thus the happy path is 

Transfer Created -> Transfer Funded -> Transfer Transferred

color_palette -> use the wise palette expained in the end of the document
preferred charts: use 100% stacked bars, line charts, bar and column charts, always plot tables. Never use pie charts.

## Dataset organization

bewlo it's the column and description of the dataset we're using

| Column | Description |
|--------|-------------|
| event_name | Name of the transfer flow step event the user has been able to successfully complete |
| dt | Event date |
| user_id | User unique identifier that performed the transfer |
| region | Region grouping of the residential country of the user |
| platform | Platform used by the user to perform the event |
| experience | Customer experience type when performing the transfer. **New**: When the customer is new to wise. **Existing**: When the customer has already performed transfers in the past |


## Analysis Plan

**1. Validate the data: ** 
- check if there is missing data
- compute agregates (give us sense of the numbers)
- check unique user_ids
- Ceate some charts answering: how many unique users do we have in each region, how many new/existing customers, how many are using each platfomrm
- check if the other properties related to user_ids change (region, platform and experience) flag it. 
- Identify extrems and outliers - are there user_ids creating an transferring multiple events? 

Questions: is the data sound? are there changes in customer profiling? 

**2. Categorize the transactions to seek the _"happy path"_** 

- Categorize transfers between `settled` `partially_settled` and `unsettled` 
- Settled transaction - events `transfer created - transfer funded - transfer transferred` ocurr in sequence for the same user_id - consider events this order for events in the same day.
- `partially_settled` occurs when the loop stops: transfer created -> transfer funded
- unsettled occurs when a transfer is only created 
- each new transfer created is event should be attributed a single transfer_id, the following steps will determine wether it's settled, partially settled or not.
- Create a new dataframe and save it on the /src as wise_transfer_info. This dataframe has to bring also the data of the user in the omment the transfer was created.
- This dataframe will be in fact the base of our analysis rather than isolated events. 



**3. Evaluate the state of transfers** 

- How the % of trasnfeer settled/partially settled/unsetlled is evolving weekly - consider a 7 day moving average
- break it by the existing variables - The existing variables show any change of pattern (eg: less new customers, more customers in a given region, etc) - a line chart for each one of the variables througout the period should make it work.

Question: is the profile changing during the time? Are the new users being as sucessful as the old ones? Is there some platform showing problems? 

- Run a logistic regression (consider partially_settled and settled = 0 and unsetteld = 1) to undertand what is causing this level of friction. 

Look into the variables that can explain more what is causing unsettled transactions.



**4. Analyze friction and recurrency**

- Who is getting friction comes back an try again? Is this different by experience, region or plaform? 
- customers who get friction in one platform try again in other platfomr? 
- New customers are coming back after being sucessful in the same rate existin customers? 
- Old Customers who get friction - who are they? Are they different from the new customers who get friction
- After getting friction - are they coming back? 

- Are customers coming back? What's the prevalence of recurrency for customers who concluded one transaction


**5. Deep Dive and Synthesize** 

Look for other signals, check wether we have something extra to look at
Synthesize the findings and key messages
Save the manipulated datasets as .csv in the /src folder
Save the images in the /exports
Save a run copy of the noteebook as pdf in /exports
Crate a readme.md for github


--- 

Tips 

# Tips for Success:
## What We're Looking For
### 1. A Clear, Defensible Demand Estimate:

For the demand estimation, it's great to brainstorm multiple methodologies. However, your final recommendation should not be a list of all possible options.
What to aim for: We want to see you make a decision. Please identify and justify one primary metric or a focused methodology that you believe is most effective for estimating demand. Explain why you chose it over other options. This shows us your ability to move from exploration to a concrete, defensible recommendation.


### 2. Insights Backed by Evidence:

Your analysis is a story, and data is your evidence. Every conclusion or insight you present must be directly supported by data and, ideally, a visualization from your analysis.
What to aim for: Don't just state a conclusion. Guide us to it. For example, instead of just saying "X is lagging," say "X is lagging, driven by X seen in Chart X." Explicitly reference your charts and data points to make your argument compelling and easy to follow.

### 3. Go Deep, Not Just Wide:

Surface-level analysis isn't enough to drive action. We're looking for you to dig into the data to find the "why" behind the numbers.
What to aim for: Break down the top-line metrics. Segment the data by key dimensions provided (e.g., region, platform, experience). Often, the most critical insight is hidden in a specific slice of the data. The goal is to identify a root cause, not just describe overall trends.

### 4. Make Your Code Accessible:

A common and easily avoidable hiccup is sharing-permission issues. We want to see your work, so please make sure we can access it!
What to aim for: Before you submit, please double-check that any links to your work (like a Google Colab notebook, GitHub repo, or presentation) are set to "Anyone with the link can view."

### 5. Frame Actionable Recommendations:

The ultimate goal of our analysis at Wise is to help product teams make better decisions. Your conclusions should be practical and focused on what the team should do next.
What to aim for: Based on your key finding, what is your recommendation? Should the team investigate a bug? Re-evaluate a user flow? Double down on a specific market? Be specific about the next steps.
We provide these tips because we want you to succeed. We're looking forward to seeing your unique approach and how you think.


--- 

wise_palette

wise_colors = [
    '#1A4D3A',  # Verde escuro principal (Wise dark green)
    '#2E7D32',  # Verde médio-escuro
    '#4CAF50',  # Verde médio
    '#66BB6A',  # Verde médio-claro
    '#81C784',  # Verde claro
    '#A5D6A7',  # Verde muito claro
    '#C8E6C9',  # Verde pastél
    '#E8F5E8'   # Verde quase branco
]

