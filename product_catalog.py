from product_data import products  # Make sure this file exists and is correct

# Print first few products to check structure
print("Sample Products:")
print(products[1:3])  # Optional: Just to see what the data looks like

# Step 1: Collect customer preferences
customer_preferences = []

while True:
    preference = input("Enter a product preference (or type 'N' to finish): ")
    if preference.upper() == 'N':
        break
    customer_preferences.append(preference)

# Show collected preferences
print("\nCustomer Preferences:")
for pref in customer_preferences:
    print("-", pref)

# Step 4: Convert product tags to sets
converted_products = []

for product in products:
    updated_product = product.copy()
    updated_product['tags'] = set(product['tags'])  # convert tags to set
    converted_products.append(updated_product)

# Step 5: Function to count matching tags
def count_matches(product_tags, customer_tags):
    return len(product_tags & customer_tags)

# Step 6: Recommend products
def recommend_products(products, customer_tags):
    recommendations = []

    for product in products:
        product_tags = product['tags']
        match_count = count_matches(product_tags, customer_tags)

        if match_count > 0:
            recommendations.append({
                'name': product['name'],
                'matches': match_count
            })

    sorted_recommendations = sorted(recommendations, key=lambda x: x['matches'], reverse=True)
    return sorted_recommendations

# Step 7: Call the function and print the results
customer_tags = set(customer_preferences)
recommended = recommend_products(converted_products, customer_tags)

# Print results
print("\nRecommended Products:")
if not recommended:
    print("No matching products found.")
else:
    for item in recommended:
        print(f"{item['name']} - {item['matches']} tag match(es)")
