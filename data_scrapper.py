import requests, os
import json
import datetime
def get_ticker_data(data_limit=5):
    response = requests.get("https://api.binance.us/api/v3/ticker/price").json()
    count = 0
    currencies = []
    for data in response:
        # data == dict('symbol': symbol, 'price': price)
        filter = data['symbol']
        filter = filter[-3:]
        # only get pairs matched with USD$
        if filter == 'USD':
            currencies.append(data)
            count += 1
        if count == data_limit: return currencies

'''
 {
        "model": "main_app.currency",
        "pk": 1,
        "fields": {
          "symbol": "BTCUSD",
          "price": 59213.4200,
        }
    },
''' 
def parse_data(currency_info):
    new_list = []
    counter = 1
    for item in currency_info:
        new_obj = {
            "model": 'main_app.currency',
            "pk": counter,
            "fields": {
                "symbol": item.get('symbol'),
                "price": float(item.get('price'))
            }
        }
        counter += 1
        new_list.append(new_obj)

    x = json.dumps(new_list)
    return x

def append_text(info):
    '''Append data to an existing file'''
    with open('data.json', 'w') as f:
        f.write(info)
        print('done')

currency_info = get_ticker_data(45)
x = parse_data(currency_info)
append_text(x)
os.system('python3 manage.py loaddata data.json')


# import requests
# import json
# import datetime
# # import DB
# from .models import Currency



# # base URL = https://api.binance.us
# # all prices endpoint = /api/v3/ticker/price

# def get_ticker_data(data_limit=5):
#     response = requests.get("https://api.binance.us/api/v3/ticker/price").json()
#     count = 0
#     currencies = []
#     for data in response:
#         # data == dict('symbol': symbol, 'price': price)
#         filter = data['symbol']
#         filter = filter[-3:]

#         # only get pairs matched with USD$
#         if filter == 'USD':
#             currencies.append(data)
#             count += 1
    
#         if count == data_limit: return currencies

# currency_info = get_ticker_data(45)

# for curr in currency_info:
#     print(curr)



# print(f"Currency : {currency}  Price: {price}")