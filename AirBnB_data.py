import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

air_bnb = pd.read_csv('AB_NYC_2019 - AB_NYC_2019.csv')

# How many neighborhood groups are available and which shows up the most?
num_neighborhood_groups = air_bnb['neighbourhood_group'].nunique()
most_common_neighborhood_group = air_bnb['neighbourhood_group'].mode()[0]
print(f"Number of neighborhood groups available: {num_neighborhood_groups}")
print(f"Most common neighborhood group: {most_common_neighborhood_group}")

# Are private rooms the most popular in Manhattan?
private_rooms_manhattan = air_bnb[(air_bnb['neighbourhood_group'] == 'Manhattan') & (air_bnb['room_type'] == 'Private room')]
num_private_rooms_manhattan = private_rooms_manhattan.shape[0]
print(f"Number of private rooms in Manhattan: {num_private_rooms_manhattan}")

# Which hosts are the busiest and based on their reviews?
busiest_hosts = air_bnb.groupby('host_name')['number_of_reviews'].sum().nlargest(5)
print("Top 5 busiest hosts based on reviews:")
print(busiest_hosts)

# Which neighborhood group has the highest average price?
neighborhood_group_avg_price = air_bnb.groupby('neighbourhood_group')['price'].mean().idxmax()
print(f"Neighborhood group with the highest average price: {neighborhood_group_avg_price}")

# Which neighborhood group has the highest total price?
neighborhood_group_total_price = air_bnb.groupby('neighbourhood_group')['price'].sum().idxmax()
print(f"Neighborhood group with the highest total price: {neighborhood_group_total_price}")

# Which top 5 hosts have the highest total price?
top_5_hosts_highest_total_price = air_bnb.groupby('host_name')['price'].sum().nlargest(5)
print("Top 5 hosts with the highest total price:")
print(top_5_hosts_highest_total_price)

# Who currently has no (zero) availability with a review count of 100 or more?
hosts_no_availability = air_bnb[(air_bnb['availability_365'] == 0) & (air_bnb['number_of_reviews'] >= 100)]['host_name'].unique()
print("Hosts with no availability and 100 or more reviews:")
print(hosts_no_availability)

# What host has the highest total of prices and where are they located?
host_highest_total_prices = air_bnb.groupby(['host_name', 'neighbourhood_group'])['price'].sum().nlargest(1)
print("Host with the highest total of prices and their location:")
print(host_highest_total_prices)

# When did Danielle from Queens last receive a review?
air_bnb['last_review'] = pd.to_datetime(air_bnb['last_review'])

danielle_reviews_queens = air_bnb[(air_bnb['host_name'] == 'Danielle') & (air_bnb['neighbourhood_group'] == 'Queens')]
last_review_date = danielle_reviews_queens['last_review'].max()
print(f"Danielle from Queens last received a review on: {last_review_date}")


# Further Questions:

# Which host has the most listings?
most_listings_host = air_bnb.groupby('host_name')['id'].count().idxmax()
print(f"Host with the most listings: {most_listings_host}")

#  How many listings have completely open availability?
open_avail_listings = air_bnb[air_bnb['availability_365'] == 365].shape[0]
print(f"Number of listings with completely open availability: {open_avail_listings}")

room_types_highest_reviews = air_bnb.groupby('room_type')['number_of_reviews'].sum().idxmax()
print(f"Room types with the highest review numbers: {room_types_highest_reviews}")
