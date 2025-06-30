import requests as r
import sys

def main():
    try:
        response = r.get("https://api.artic.edu/api/v1/artworks/search") ##tries calling da api
        response.raise_for_status() ##tries raising an http error pre-emptively
    except r.HTTPError: #if it gets the http error
        print("die api het gebreek :( (couln't complete request))") #prints an error as a string
        sys.exit(1) #and then exits
    
    
    content = response.json() #JSONizes the response call. NB JSON is a dict

    for artwork in content["data"]: ##in the JSON there is a content key and data value. the data value is its own dict.
        print(f"* {artwork['title']}") #the artwork variable is recalled here as a call for .title
    



main()