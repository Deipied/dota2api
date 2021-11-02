import requests
r = requests.get("https://randomuser.me/api/", params=query_params)
print(r)
print(r.json())