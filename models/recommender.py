# import pandas as pd
# from sklearn.metrics.pairwise import cosine_similarity
# from sklearn.feature_extraction.text import TfidfVectorizer
# import numpy as np

# class Recommender:
#     def __init__(self, items_df, price_weight=3, location_weight=2, category_weight=1):
#         self.items_df = items_df
#         self.price_weight = price_weight
#         self.location_weight = location_weight
#         self.category_weight = category_weight
#         self.items_df['features'] = self._create_weighted_features()
#         self.similarity_matrix = self._calculate_similarity()

#     def _create_weighted_features(self):
#         def weight_features(row):
#             price = row['price']
#             location = row['location']
#             category = row['category']
#             return f"{category} {self.category_weight} {location} {self.location_weight} {price} {self.price_weight}"
        
#         return self.items_df.apply(weight_features, axis=1)

#     def _calculate_similarity(self):
#         vectorizer = TfidfVectorizer()  # TF-IDF Vectorizer
#         features_matrix = vectorizer.fit_transform(self.items_df['features'])
#         similarity_matrix = cosine_similarity(features_matrix)
#         return similarity_matrix

#     def recommend(self, user_favorites, top_n=10):
#         recommended_items = set()
#         for item_id in user_favorites:
#             item_index = self.items_df.index[self.items_df['id'] == item_id].tolist()[0]
#             similar_items = list(enumerate(self.similarity_matrix[item_index]))
#             similar_items = sorted(similar_items, key=lambda x: x[1], reverse=True)
#             for item in similar_items:
#                 recommended_item_id = self.items_df.iloc[item[0]]['id']
#                 if recommended_item_id not in user_favorites:
#                     recommended_items.add(recommended_item_id)
#                 if len(recommended_items) >= top_n:
#                     break
#             if len(recommended_items) >= top_n:
#                 break
#         return list(recommended_items)

# if __name__ == "__main__":
#     items_df = pd.read_csv('../data/items.csv')
#     recommender = Recommender(items_df, price_weight=3, location_weight=2, category_weight=1)
#     user_favorites = ["64d9a6f41b1c4f7e", "64d9a6f41b1c4f87", "64d9a6f41b1c4f8e"]
#     recommendations = recommender.recommend(user_favorites)
#     print(f"Recommended items: {recommendations}")
import pandas as pd

# Load the items data
items_data = pd.read_csv('../data/items.csv')
favorites_data = pd.read_csv('../data/favorites.csv')

print(items_data)
category_counts = items_data['category'].value_counts()

# Print the counts for each category
print(category_counts)

# Replace commas with spaces in the 'address' column
items_data['address'] = items_data['address'].str.replace(',', ' ', regex=False)

# Select only the required fields
filtered_items = items_data[['property_id', 'property_name', 'price', 'address', 'category', 'status']]
filtered_favorites = favorites_data[['property_id','user_id','liked']]
# Print the filtered DataFrame to verify
print(filtered_items)
print(filtered_favorites)

print(items_data.isnull().sum())
print(favorites_data.isnull().sum())