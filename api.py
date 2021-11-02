import requests, json, time, os

# downloadmatch dta from open dota
def get_match_by_id(match_id):
    m_id = str(match_id)
    # fetch match data
    request = requests.get("https://api.opendota.com/api/matches/" + m_id)
    if request.ok:
        print("GET:", m_id)
        data = request.json()
        # save it
        file = open("download" + os.sep + m_id + 'data.json', 'w')
        json.dump(data, file, indent=4)
        file.close()


match_id = 5820544839
get_match_by_id(match_id)
# for i in range(2):
#     get_match_by_id(match_id + i)
#     time.sleep(2)