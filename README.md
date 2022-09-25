# NBAPredictions
ECE 539 NBA Predictions Project Repository

# Data Processing
The first few cells in the data processing notebook will download the NBA basketball dataset from https://www.kaggle.com/datasets/wyattowalsh/basketball.
Kaggle uses an authentication method for their api, so you'll need to download a token from your kaggle account. 
More info on that can be found under the 'Authentication' heading here: https://www.kaggle.com/docs/api.
Note that the kaggle documentation will tell you to store the kaggle.json file in some generalized .kaggle directory,
for this project just put the kaggle.json file into the root of the repository directory (NBAPredictions/kaggle.json)

You'll also need to install some packages for the data processing step, namely 'kaggle' and 'ipython-sql'. 
Run 'pip install kaggle' and 'pip install ipython-sql' in your terminal to install these dependencies.
