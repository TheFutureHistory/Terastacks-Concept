from easy_exchange_rates import API
import moneyed

def convert_currencies():
    api = API
    print(api.get_exchange_rates('USD'))



convert_currencies()