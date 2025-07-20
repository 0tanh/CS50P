import requests
import sys
import json
       
# Check if command line argument is provided
if len(sys.argv) != 2:
    print("Usage: python bitcoin.py <amount_in_btc>")
    sys.exit(1)

try:
    # Convert command line argument to float
    btc_amount = float(sys.argv[1])
except ValueError:
    print("Error: Please provide a valid number for Bitcoin amount")
    sys.exit(1)

# Using your original API
API_KEY = "1f0e5922834489754976585770fe6f9e54b0fa082ca1d7515a0f828f5f83a573"
API_URL = "https://rest.coincap.io/v3/assets?search=BTC&ids=bitcoin&limit=5&offset=8"

# Headers for authentication
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}   

try:
    # Make API call
    r = requests.get(API_URL, headers=headers)
    r.raise_for_status()  # Raise an exception for bad status codes
    
    # Parse JSON response
    alldata = r.json()
    
    # Debug: Print the structure to see what we're working with
    print("API Response structure:")
    print(json.dumps(alldata, indent=2))
    
    # The API returns a list, so we need to access the first item
    if isinstance(alldata, list) and len(alldata) > 0:
        # Access the first item in the list
        bitcoin_data = alldata[0]
        price_usd = float(bitcoin_data["priceUsd"])
    elif isinstance(alldata, dict) and "data" in alldata:
        # If it's a dict with "data" key, handle accordingly
        if isinstance(alldata["data"], list):
            bitcoin_data = alldata["data"][0]
            price_usd = float(bitcoin_data["priceUsd"])
        else:
            price_usd = float(alldata["data"]["priceUsd"])
    else:
        raise ValueError("Unexpected API response structure")
    
    # Calculate total value
    total_value = btc_amount * price_usd
    
    # Print result
    print(f"${total_value:,.2f}")

except requests.exceptions.ConnectionError as e:
    print(f"Connection error: {e}")
except requests.exceptions.Timeout as e:
    print(f"Request timed out: {e}")
except requests.exceptions.HTTPError as e:
    print(f"HTTP error: {e}")
except requests.exceptions.RequestException as e:
    print(f"An unexpected requests error occurred: {e}")
except KeyError as e:
    print(f"Error parsing API response: {e}")
except ValueError as e:
    print(f"Error converting price to number: {e}")
except Exception as e:
    print(f"A general error occurred: {e}")