import openpyxl
import json

def excel_to_json_array(excel_file_path):
    try:
        workbook = openpyxl.load_workbook(excel_file_path)
        worksheet = workbook.active

        headers = [cell.value for cell in worksheet[1]]

        json_array = []

        for row in worksheet.iter_rows(min_row=2, values_only=True):
            json_data = {}
            for col_num, cell_value in enumerate(row):
                header = headers[col_num]
                if isinstance(cell_value, bool):
                    cell_value = 'TRUE' if cell_value else 'FALSE'
                json_data[header] = cell_value if cell_value is not None else None
            json_array.append(json_data)

        return json_array

    except Exception as e:
        print(f"Error: {e}")
        return None

# Replace 'your_file.xlsx' with the path to your Excel file
file_path = 'ulb and subdistrict master 19072023.xlsx'
json_array = excel_to_json_array(file_path)

for entry in json_array:
    if entry["corporation flag"] == "TRUE":
        entry["corporation flag"] = True
    elif entry["corporation flag"] == "FALSE":
        entry["corporation flag"] = False


with open('test.json', 'w') as file:
    json.dump(json_array, file)

# if json_array is not None:
#     # Print the resulting JSON array
#     print(json.dumps(json_array, indent=4))
# else:
#     print("Failed to read the Excel file or empty file.")
