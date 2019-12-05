from django.shortcuts import render

def home(request):
    import requests
    import json
    price_req=requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,EOS,LTC,XLM,ADA,USDT,MIOTA,TRX&tsyms=USD")
    price=json.loads(price_req._content)

    api_req=requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api=json.loads(api_req.content)
    return render(request, 'home.html', {'api':api,'price':price})

def prices(request):
    if request.method == 'POST':
        quote=request.POST['quote']
        import requests
        import json
        crypto_req=requests.get(f"https://min-api.cryptocompare.com/data/pricemultifull?fsyms={quote.upper()}&tsyms=USD")
        crypto=json.loads(crypto_req.content)
        return render(request,'prices.html',{'quote':quote,'crypto':crypto})

    return render(request,'prices.html',{'nosearch':'There is no search input'})