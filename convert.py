import json

with open('zresult.json', 'r') as file:
    data = json.load(file)

# Create a new dictionary to store the converted data
converted_data = {}

# Loop through each entry in the original data
for district, items in data.items():
    new_items = []
    corporation_items = []
    subdistrict_items = []
    
    # Separate items into corporation and subdistrict lists
    for item in items:
        if item["corporation_flag"]:
            corporation_items.append(item)
        else:
            subdistrict_items.append(item)
    
    # Add corporation items if any
    if corporation_items:
        new_items.append({
            "name": "Corporation",
            "items": corporation_items
        })
    
    # Add subdistrict items if any
    if subdistrict_items:
        new_items.append({
            "name": "Sub District",
            "items": subdistrict_items
        })
    
    # Add the new items to the converted data dictionary
    converted_data[district] = new_items

# Convert the final dictionary to JSON format
converted_json = json.dumps(converted_data, separators=(',', ':'))

# Print the converted JSON
print(converted_json)

with open('final_district_subdistrict.json', 'w') as file:
    file.write(converted_json)


# ============================

# Your provided JSON data

# with open('zresult.json', 'r') as file:
#     data = json.load(file)


# # Create a new dictionary to store the converted data
# converted_data = {}

# # Loop through each entry in the original data
# for district, items in data.items():
#     new_items = []
#     corporation_items = []
#     subdistrict_items = []
    
#     # Separate items into corporation and subdistrict lists
#     for item in items:
#         if item["corporation_flag"]:
#             corporation_items.append(item)
#         else:
#             subdistrict_items.append(item)
    
#     # Add corporation items if any
#     if corporation_items:
#         new_items.append({
#             "name": "Corporation",
#             "items": corporation_items
#         })
    
#     # Add subdistrict items if any
#     if subdistrict_items:
#         new_items.append({
#             "name": "Sub District",
#             "items": subdistrict_items
#         })
    
#     # Add the new items to the converted data dictionary
#     converted_data[district] = new_items

# # Convert the final dictionary to JSON format
# converted_json = json.dumps(converted_data, indent=4)

# # Print the converted JSON
# print(converted_json)


# with open('final_district_subdistrict.json', 'w') as file:
#     json.dump(converted_json, file)
