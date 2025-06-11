import requests

url = "https://nominatim.openstreetmap.org/search"
params = {
    'q': 'Ho Chi Minh City',
    'format': 'jsonv2',
    'addressdetails': 1,
    'limit': 1
}
headers = {
    'User-Agent': 'YourAppName/1.0 (your_email@example.com)'  # Replace with your app name and email
}

response = requests.get(url, params=params, headers=headers)

if response.status_code == 200:
    data = response.json()
    # Process the data
else:
    print(f"Status code {response.status_code} from {url}: ERROR - {response.reason}")
447