import json
import math
from operator import itemgetter

with open("api.the-odds-api.com.json", 'r') as file:
    data = json.load(file)


arbitrages = []


for j in range(len(data)):
    # print(data[j]['bookmakers'])
    # print("--------")
    # print(len(data[j]['bookmakers']))
    # print("--------")
    prices = []
    likelyTeamVals = []
    unlikelyTeamVals = []
    sites = []
    
    flag = 1 if data[j]['bookmakers'][0]['markets'][0]['outcomes'][0]['price'] > 0.0 else 0
    
    # print("flag:", flag)
    for i in range(len(data[j]['bookmakers'])):
        # prices.append()
        bookmaker = data[j]['bookmakers'][i]['key']
        priceA = data[j]['bookmakers'][i]['markets'][0]['outcomes'][0]['price']
        priceB = data[j]['bookmakers'][i]['markets'][0]['outcomes'][1]['price']
        # print("Bookmaker", (i + 1), ":", bookmaker, "(", priceA, ",", priceB, ")")
        sites.append(bookmaker)
        if flag:
            likelyTeamVals.append((priceA)/100.0 + 2.0)
            unlikelyTeamVals.append(100.0/abs(priceB) + 1.0)
        else:
            likelyTeamVals.append(100.0/abs(priceA) + 1.0)
            unlikelyTeamVals.append((priceB)/100.0 + 2.0)
        # print("----------------")

    # print("likelyTeamVals:", likelyTeamVals)
    # print("unlikelyTeam:", unlikelyTeam)
    if 1.0/max(likelyTeamVals) + 1.0/max(unlikelyTeamVals) < 1.0:
        # print("arb exists")
        likelyBet = (100/max(likelyTeamVals))/ (1/max(likelyTeamVals) + 1/max(unlikelyTeamVals))
        unlikelyBet = (100/max(unlikelyTeamVals))/ (1/max(likelyTeamVals) + 1/max(unlikelyTeamVals))
        # print("Bet on likely team:", likelyBet, "on site:", sites[likelyTeam.index(max(likelyTeam))])
        # print("Bet on unlikely team:", unlikelyBet, "on site:", sites[unlikelyTeam.index(max(unlikelyTeam))])
        # print("Payoff if likely team wins:", likelyBet * max(likelyTeam)/100.0)
        # print("Payoff if unlikely team wins:", unlikelyBet * max(unlikelyTeam)/100.0)
        arbitrages.append([((likelyBet * max(likelyTeamVals)/100.0) * 100.0 - 100.0), ("Bet on likely team:", likelyBet, "on site:", sites[likelyTeamVals.index(max(likelyTeamVals))]), ("Bet on unlikely team:", unlikelyBet, "on site:", sites[unlikelyTeamVals.index(max(unlikelyTeamVals))])])
    # else:
        # print("arb does not exist")
    # print("========================================================================================")

for i in range(len(arbitrages)):
    print(arbitrages[i])
    print("--------------")

