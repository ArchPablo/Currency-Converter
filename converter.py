import requests

currency = input('enter the currency you want to convert: ').lower()
currency_code = f'http://www.floatrates.com/daily/{currency}.json'
r = requests.get(currency_code)
py_r = r.json()
if currency == "eur":
    cashe = {'usd': py_r['usd']}
if currency == "usd":
    cashe = {'eur': py_r['eur']}
elif currency != "eur" or "usd":
    cashe = {'usd': py_r['usd'], 'eur': py_r['eur']}
while True:
    exch = input('enter the currency to which you want to convert the original currency: ').lower()
    if exch == "":
        break
    amount = float(input(f'enter amount {currency} :'))
    print('Checking the cache...')
    if exch in cashe:
        print('Oh! It is in the cache!')
        rate = cashe[exch]['rate'] * amount
        print(f'You received {round(rate, 2)} {exch.upper()}.')
    else:
        print('Sorry, but it is not in the cache!')
        rate = py_r[exch]['rate'] * amount
        print(f'You received {round(rate, 2)} {exch.upper()}.')
        cashe[exch] = py_r[exch]
