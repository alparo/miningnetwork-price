from eospy.cleos import Cleos
import csv
import time
import datetime


ce = Cleos(url='https://api.wax.alohaeos.com')
arguments = {
    "code": "miningntwrkc",
    "scope": "miningntwrkc",
    "table": "config"
}


try:
    counter = 0
    while True:
        # Get the data from blockchain
        get_data = ce.get_table(arguments['code'], arguments['scope'], arguments['table'])
        line_data = get_data['rows'][0]
        sh_pool = int(line_data['shares_pool'])
        btk_pool = line_data['tokens_pool']
        price = btk_pool / sh_pool / 10
        date = datetime.datetime.now()

        print(f'{date}, {price}, {sh_pool}, {btk_pool}')
        with open('new_prices.csv', "a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow([date, price, sh_pool, btk_pool])
        counter += 1

        time.sleep(6)
except KeyboardInterrupt:
    print(f'Exiting...\nRows added: {counter}')