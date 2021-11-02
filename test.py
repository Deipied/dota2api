import requests
r = requests.get("https://randomuser.me/api/")
print(r)
print(r.json())