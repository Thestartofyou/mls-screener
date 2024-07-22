import requests
import json

# Function to get MLS data
def get_mls_data(api_url, headers, params):
    response = requests.get(api_url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None

# Function to filter apartments based on criteria
def filter_apartments(apartments, criteria):
    filtered = []
    for apt in apartments:
        if (criteria['pets'] in apt['pets_allowed'] and
            criteria['students_or_working'] in apt['tenant_type'] and
            criteria['min_sqft'] <= apt['sqft'] <= criteria['max_sqft'] and
            criteria['in_unit_laundry'] == apt['in_unit_laundry'] and
            criteria['location'] in apt['location'] and
            criteria['move_in_date'] >= apt['available_date']):
            filtered.append(apt)
    return filtered

# User's criteria
criteria = {
    'pets': 'yes',  # 'yes' or 'no'
    'students_or_working': 'working',  # 'students' or 'working'
    'min_sqft': 500,
    'max_sqft': 1000,
    'in_unit_laundry': True,
    'location': 'Dorchester',
    'move_in_date': '2024-08-01'
}

# MLS API endpoint and headers
api_url = 'https://api.mls.com/v1/apartments'
headers = {
    'Authorization': 'Bearer YOUR_API_KEY',
    'Content-Type': 'application/json'
}

# Parameters for API request
params = {
    'location': criteria['location'],
    'min_sqft': criteria['min_sqft'],
    'max_sqft': criteria['max_sqft'],
    'in_unit_laundry': criteria['in_unit_laundry'],
    'available_date_from': criteria['move_in_date']
}

# Get data from MLS API
apartments = get_mls_data(api_url, headers, params)

if apartments:
    # Filter apartments based on detailed criteria
    filtered_apartments = filter_apartments(apartments, criteria)

    # Print filtered apartments
    print("Filtered Apartments:")
    for apt in filtered_apartments:
        print(json.dumps(apt, indent=4))
else:
    print("No apartments found.")
