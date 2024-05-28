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
#



#In-class

 

data_2017 = pd.read_csv('redsox_2017_hitting.txt')
data_2018 = pd.read_csv('redsox_2018_hitting.txt')

print("2017 Data Description:")
print(data_2017.describe())
print("\n2018 Data Description:")
print(data_2018.describe())

sorted_data_2017 = data_2017.sort_values(by='BA', ascending=False)
sorted_data_2018 = data_2018.sort_values(by='BA', ascending=False)

print("\n2017 Data Sorted by Batting Average:")
print(sorted_data_2017)
print("\n2018 Data Sorted by Batting Average:")
print(sorted_data_2018)

# Import pandas library
import pandas as pd

# Load data
data_2017 = pd.read_csv('redsox_2017_hitting.txt')
data_2018 = pd.read_csv('redsox_2018_hitting.txt')

# Define UDF
def all_star(row):
    if row['BA'] > 0.280 or row['OBP'] > 0.360:
        return 'Yes'
    else:
        return 'No'

# Apply UDF to create 'All-Star' column
data_2017['All-Star'] = data_2017.apply(all_star, axis=1)
data_2018['All-Star'] = data_2018.apply(all_star, axis=1)

# Print data
print(data_2017)
print(data_2018)
