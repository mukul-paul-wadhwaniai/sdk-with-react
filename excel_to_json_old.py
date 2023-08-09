import pandas as pd
import json
# Convert the JSON strings to Python lists/dictionaries
with open('state_district.json', 'r') as file:
    districts = json.load(file)

with open('sub_dist.json', 'r') as file:
    subdistricts = json.load(file)

# Create a dictionary to store the results
result_json = {}

# Merge the data from both JSON arrays to form the desired structure
for subdistrict in subdistricts:
    district_code = subdistrict["districtcode"]
    subdistrict_name = subdistrict["subdistrictname"]
    subdistrict_code = subdistrict["subdistrictcode"]

    # Find the corresponding district name from the first JSON array
    district_name = next((district["district name"] for district in districts if district["district code"] == district_code), None)

    # Create a new dictionary with the required information
    subdistrict_data = {
        "subdistrict_name": subdistrict_name,
        "subdistrict_code": subdistrict_code
    }

    # Append the data to the result JSON dictionary under the district name key
    if district_name in result_json:
        result_json[district_name].append(subdistrict_data)
    else:
        result_json[district_name] = [subdistrict_data]

# Convert the result JSON dictionary to a JSON string
result_json_string = json.dumps(result_json, indent=2)

# Write the result JSON string to a new JSON file
with open('result.json', 'w') as file:
    file.write(result_json_string)

exit()

def excel_to_json(excel_file_path, json_file_path):
    # Read the Excel file using pandas
    df = pd.read_excel(excel_file_path)

    # Convert the DataFrame to a dictionary
    data = df.to_dict(orient='records')

    # Write the data to a JSON file
    with open(json_file_path, 'w') as json_file:
        json.dump(data, json_file)

# Example usage
excel_file_path = 'sub_dist_code.xlsx'  # Replace with your Excel file path
json_file_path = 'sub_dist.json'         # Replace with desired JSON file path
excel_to_json(excel_file_path, json_file_path)

# print(len(json_file_path))