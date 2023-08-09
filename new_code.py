import json

with open('test.json', 'r') as file:
    districts = json.load(file)
count = 0
def create_district_local_body_dict(data):
    district_dict = {}
    for entry in data:
        district_name = entry['district name'].upper()
        local_body_name = entry['local body name']
        local_body_code = entry['local body code']
        corporation_flag = entry['corporation flag']

        if district_name not in district_dict:
            district_dict[district_name] = []
        
        
        district_dict[district_name].append({'subdistrict_name': local_body_name, 'local_body_code': local_body_code, 'corporation_flag': corporation_flag})
        if(district_name == district_dict[district_name]["district name"]) :
            count += 1
    return district_dict


district_local_body_dict = create_district_local_body_dict(districts)


# with open('final_district_subdistrict.json', 'w') as file:
#     json.dump(district_local_body_dict, file)

