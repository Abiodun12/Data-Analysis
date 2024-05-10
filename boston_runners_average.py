import pandas as pd

# Load data
data = pd.read_csv('boston_marathon2017_edited csv.csv')

# Extract age column
ages = data['Age']

# Calculate average age
average_age = ages.mean()

# Print result
print("Average age of runners in the 2017 Boston Marathon:", average_age)
