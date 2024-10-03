import json
from operator import itemgetter

with open("api.the-odds-api.com.json", 'r') as file:
    data = json.load(file)

# print(data[j])
print(len(data))
print(data[0])
print("--------")
print(data[1])
print("--------")
print(data[1]['bookmakers'])
print("--------")
# print(data[j]['bookmakers'][0]["markets"])
# print(data[j]['bookmakers'][1])
# print(data[j]['bookmakers'][1]["markets"])
# print(len(data))
# print(len(data[j]))
for j in range(3):
    prices = []
    teamA = []
    teamB = []
    for i in range(len(data[j]) - 1):
        # prices.append()
        teamA.append((data[j]['bookmakers'][i]['markets'][0]['outcomes'][0]['price'] + 200.0))
        teamB.append(((-100.0/data[j]['bookmakers'][i]['markets'][0]['outcomes'][1]['price']) + 1.0)* 100.0)
        prices.append([(data[j]['bookmakers'][i]['markets'][0]['outcomes'][0]['price'] + 200.0), ((-100.0/data[j]['bookmakers'][i]['markets'][0]['outcomes'][1]['price']) + 1.0)* 100.0, data[j]['bookmakers'][i]['key']])
        # print(data[j]['bookmakers'][i]['key'], data[j]['bookmakers'][i]['markets'][0]['outcomes'][0])
    # print(prices)
    # prices.sort()
    # print(prices)
    # teamA.sort()
    # teamB.sort()
    # print(teamA)
    # print(teamB)
    aBet = (100/max(teamA))/ (1/max(teamA) + 1/max(teamB))
    bBet = (100/max(teamB))/ (1/max(teamA) + 1/max(teamB))
    print("Bet on team A:", aBet)
    print("Bet on team B:", bBet)
    print("Payoff if team A wins:", aBet * max(teamA)/100.0)
    print("Payoff if team B wins:", bBet * max(teamB)/100.0)
    print("---------------------")

