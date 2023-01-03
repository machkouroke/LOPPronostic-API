import requests
import json

uri = 'https://api.football-data.org/v4/matches'
headers = {'X-Auth-Token': '3d6e6f89c3e244e4813c0c44a32fd80b'}
lig = []
# lig.add(2)
# lig.add(1)
# lig.add(2)
# print(lig)

response = requests.get(uri, headers=headers)
for match in response.json()['matches']:
    lig.append(match['competition'])
    print(match)
# print(set(lig))
unique_list = []
[unique_list.append(x) for x in lig if x not in unique_list]
print(unique_list)
# for l in set(lig):
#     print(l)
