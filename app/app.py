import pandas as pd

# Load sample data
items_df = pd.read_csv('data/items.csv')
users = pd.read_csv('data/users.csv')

# Display the data
print("Items Data:")
print(items_df)

print("Users Data:")
print(users)
