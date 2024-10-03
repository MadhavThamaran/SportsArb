import json
from operator import itemgetter

with open("api.the-odds-api.com.json", 'r') as file:
    data = json.load(file)

# print(data[0])
# print(data[0]['bookmakers'][0]["markets"])
# print(data[0]['bookmakers'][1])
# print(data[0]['bookmakers'][1]["markets"])
# print(len(data))
# print(len(data[0]))
prices = []
teamA = []
teamB = []
for i in range(len(data[0]) - 1):
    # prices.append()
    teamA.append((data[0]['bookmakers'][i]['markets'][0]['outcomes'][0]['price'] + 200))
    teamB.append(((-100/data[0]['bookmakers'][i]['markets'][0]['outcomes'][1]['price']) + 1.0)* 100)
    prices.append([(data[0]['bookmakers'][i]['markets'][0]['outcomes'][0]['price'] + 200), ((-100/data[0]['bookmakers'][i]['markets'][0]['outcomes'][1]['price']) + 1.0)* 100, data[0]['bookmakers'][i]['key']])
    # print(data[0]['bookmakers'][i]['key'], data[0]['bookmakers'][i]['markets'][0]['outcomes'][0])
# print(prices)
prices.sort()
print(prices)
teamA.sort()
teamB.sort()
print(teamA)
print(teamB)

