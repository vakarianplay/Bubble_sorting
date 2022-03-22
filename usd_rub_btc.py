import requests

def getUsdRub():
    usdrub = requests.get('https://free.currconv.com/api/v7/convert?apiKey=f6a0091b3994120d9fbd&q=USD_RUB&compact=ultra').json()
    usdrubPrint = str(usdrub['USD_RUB'])
    return usdrubPrint

def getBtcString():
    usdbtc = requests.get('https://usd.rate.sx/1BTC').text
    rubbtc = requests.get('https://rub.rate.sx/1BTC').text
    btcPrint = str("₿ - USD " + usdbtc + "₿ - RUB " + rubbtc)
    return btcPrint

print (getUsdRub()+ "\n" +getBtcString())
