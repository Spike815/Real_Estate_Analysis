import requests
test = {
  "type_of_property": "HOUSE",
  "subtype_of_property": "VILLA",
  "number_of_bedrooms": 2,
  "living_area":60,
  "furnished": 0,
  "terrace": 0,
  "terrace_area": 0,
  "garden": 1,
  "garden_area": 20,
  "total_property_area": 120,
  "total_land_area": 300,
  "number_of_facades": 2,
  "swimming_pool": 0,
  "state_of_the_building": "GOOD",
  "Province": "Oost-Vlaanderen",
  "kitchen": "Not equipped",
  "digit": 90
}

url = "http://127.0.0.1:8000/predict/"


response = requests.post(url, json=test)
print(response.text)