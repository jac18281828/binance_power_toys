from binance_order import binance_order

import json,sys

if __name__ == '__main__':

    if len(sys.argv) > 1:
        try:
            apikeyfile = sys.argv[1]
            with open(apikeyfile) as keyfile:
                apikey = json.load(keyfile)
                orderapi = binance_order(apikey)

                order = {
                    'symbol': 'BTCUSDT',
                    'side': 'BUY',
                    'type': 'LIMIT',
                    'timeInForce': 'GTC',
                    'price': 9000,
                    'quantity': 0.01,
                    'recvWindow': 5000
                }


                orderinfo = orderapi.submit(order)
                print("Order Result = %s" % orderinfo)
        except Exception as e:
            print("Failed. "+repr(e))
    else:
        print('apikey is required')
