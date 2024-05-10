import pandas as pd

# Load the NBA dataset
nba = pd.read_csv('nbastats2018-2019 - nbastats2018-2019.csv')

# What was the average age of players in the league?
average_age = nba['Age'].mean()
print("Average age of players in the league:", average_age)

# What player scored the most points?
player_most_points = nba.loc[nba['Points'].idxmax(), 'Name']
print("Player who scored the most points:", player_most_points)

# What player had the most blocks during the season? Was it a post player (F/C)?
player_most_blocks = nba.loc[nba['Blocks'].idxmax(), 'Name']
print("Player who had the most blocks during the season:", player_most_blocks)


# What player had the best 3-pt percentage?
player_best_3pt_percentage = nba.loc[nba['FG3%'].idxmax(), 'Name']
print("Player with the best 3-pt percentage:", player_best_3pt_percentage)

# Who played the most minutes during the season?
player_most_minutes = nba.loc[nba['MP'].idxmax(), 'Name']
print("Player who played the most minutes during the season:", player_most_minutes)

# What player, given their player efficiency rating, was the clutchest during the season?
clutchest_player = nba.loc[nba['PER'].idxmax(), 'Name']
print("Clutchest player based on player efficiency rating:", clutchest_player)

# What team had the youngest roster?
youngest_roster_team = nba.loc[nba['Age'].idxmin(), 'Team']
print("Team with the youngest roster:", youngest_roster_team)

# Who is the highest paid player during the season?
highest_paid_player = nba.loc[nba['Salary'].idxmax(), 'Name']
print("Highest paid player during the season:", highest_paid_player)

# At the end of a game, who WOULDN'T you want on the Free Throw Line?
worst_free_throw_shooter = nba.loc[nba['FT%'].idxmin(), 'Name']
print("Player you wouldn't want on the Free Throw Line:", worst_free_throw_shooter)

#this was fun :)