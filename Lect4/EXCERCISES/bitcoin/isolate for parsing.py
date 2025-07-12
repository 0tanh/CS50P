import json 

r = {
  "data": {
    "id": "bitcoin",
    "rank": "1",
    "symbol": "BTC",
    "name": "Bitcoin",
    "supply": "19823321.0000000000000000",
    "maxSupply": "21000000.0000000000000000",
    "marketCapUsd": "1939613325892.4607145113457500",
    "volumeUsd24Hr": "12341417371.3505338276601668",
    "priceUsd": "97845.0243474572557500",
    "changePercent24Hr": "1.4324165997531723",
    "vwap24Hr": "96203.8859537212418977",
    "explorer": "https://blockchain.info/"
  },
  "timestamp": 1739399343596
}
json.dumps(r, indent= 4)

print(r["data"]["priceUsd"])