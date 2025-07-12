import requests
import sys
       
##ERROR HANDLING FOR SYS.ARV
try:
    USER_Q = float(sys.argv[1])
except IndexError:
    sys.exit("Missing command-line argument")
except (ValueError, TypeError):
    sys.exit("Command-line argument is not a number")

## DECLARING API URL AND KEY
API_KEY = "1f0e5922834489754976585770fe6f9e54b0fa082ca1d7515a0f828f5f83a573"
API_URL = "https://rest.coincap.io/v3/assets?search=BTC&ids=bitcoin&limit=5&offset=8"

## FORMATS THE KEY TO BE PARSED BY THE requests.get() function
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}   
##CALLS API
try:   
    r = requests.get(API_URL, headers= headers)
    
#BOILER PLATE ERROR HANDLING FOR API CALL
except requests.exceptions.ConnectionError as e:
    print(f"Connection error: {e}")
except requests.exceptions.Timeout as e:
    print(f"Request timed out: {e}")
except requests.exceptions.HTTPError as e:
    print(f"HTTP error: {e}")
except requests.exceptions.RequestException as e:
    print(f"An unexpected requests error occurred: {e}")
except Exception as e:
    print(f"A general error occurred: {e}")

try:
    #MAKES A DICT FROM REQUEST CLASS
    alldata = r.json()
    workable = alldata["data"][1]
    priceUSD = float(workable["priceUsd"])
    #CALCULATES REQUEST * EXCHANGE RATE
    amount = USER_Q * priceUSD
    # #PRINTS THAT
    print(f"${amount:,.4f}")

except Exception as e:
    print(f"A general error occurred: {e}")