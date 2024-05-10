import pandas as pd
## Homework 1
# Load data
data_2017 = pd.read_csv('redsox_2017_hitting.txt')
data_2018 = pd.read_csv('redsox_2018_hitting.txt')

# Add 'Team' column
data_2017['Team'] = 'BOS'
data_2018['Team'] = 'BOS'

# Group by 'Team' and calculate sum of 'HR' and 'RBI'
totals_2017 = data_2017.groupby('Team').agg({'HR': 'sum', 'RBI': 'sum'})
totals_2018 = data_2018.groupby('Team').agg({'HR': 'sum', 'RBI': 'sum'})

# Print results
print("2017:")
print(totals_2017)
print("\n2018:")
print(totals_2018)

