import requests
from datetime import *
from itertools import combinations

baseapi="https://api.binance.com"
   

def Candles(endpoint, param):
    req = requests.get(baseapi + endpoint, params = param)
    result = req.json()

    return result


def GetPrice(endpoint, param):
    req = requests.get(baseapi + endpoint, params = param)
    result = req.json()

    return result


def GetPairs():
    liste = GetPrice("/api/v3/ticker/price", {})
    result = [""]

    for i in liste:
        pair = i["symbol"]
        result.append(pair)

    return result


symbols = list(filter(('').__ne__, GetPairs()))
symbolList = ["BTC","ETH","USDT","USDC","BNB","DOGE","LTC","AVAX","DOT","MATIC","AAVE","UNI","APE"]

def Makethefile(symbols, allSymbols):
    count = 1
    
    with open("result.txt", "w") as file:
        for symbol in symbols:
            if symbol in allSymbols:
                params = {'symbol': symbol, 'interval': '1m', 'limit': 10}
                listCandles = Candles("/api/v3/klines", params)

                index=[]
                newIndex=[]

                for j in listCandles:
                    for i in range(len(j)):
                        if i == 1 or i == 2 or i == 3 or i== 4 or i == 5 or i == 8:
                            index.append(j[i])
                    newIndex.append(index)
                    index=[]

                nameList = ["Open", "High", "Low", "Close", "Volume", "Number of trades"]

                for j in newIndex:
                    file.write("{")
                    file.write('"' + "ID" + '"' + ":" + " " + str(count) + ", ")
                    count += 1

                    for i in range(len(j)):
                        verif = False

                        try:
                            float(j[i])
                            verif = True
                        except:
                            verif = False

                        if nameList[i] == "Number of trades":
                            if verif != True:
                                file.write('"' + nameList[i] + '"' + ":" + " " + '"' + j[i] + '"')
                            else:
                                file.write('"' + nameList[i] + '"' + ":" + " " + str(j[i]))

                        else:
                            if verif != True:
                                file.write('"' + nameList[i] + '"' + ":" + " " + '"' + j[i] + '"' + ", ")
                            else:
                                file.write('"' + nameList[i] + '"' + ":" + " " + str(j[i]) + ", ")
                                
                    file.write("},AZ")


temp = combinations(symbolList, 2)
newlist=[]

for j in list(temp):
    newlist.append(j[0]+j[1])
    newlist.append(j[1]+j[0])

for i in newlist:
    if i not in symbols:
        newlist.remove(i)

myList = []

for element in newlist:
    if element not in myList:
        myList.append(element)

Makethefile(myList, symbols)