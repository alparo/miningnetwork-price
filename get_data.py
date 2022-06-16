from eospy.cleos import Cleos
import datetime
import sqlite3
import time

ce = Cleos(url='https://api.wax.alohaeos.com')
arguments = {
    "code": "miningntwrkc",
    "scope": "miningntwrkc",
    "table": "config"
}

db = sqlite3.connect('btk_prices.db')

# Create cursor
cursor = db.cursor()

# Create table if don't exist
cursor.execute("""CREATE TABLE IF NOT EXISTS prices (
     date DATETIME,
     sh_pool INT,
     btk_pool INT,
     btk_price FLOAT
)""")


while True:
    # Get the data from blockchain
    get_data = ce.get_table(arguments['code'], arguments['scope'], arguments['table'])
    line_data = get_data['rows'][0]
    sh_pool = int(line_data['shares_pool'])
    btk_pool = line_data['tokens_pool']
    price = btk_pool / sh_pool / 10
    date = datetime.datetime.now()

    # print(f'{date}, {price}, {sh_pool}, {btk_pool}')

    cursor.execute('INSERT INTO prices VALUES (?, ?, ?, ?)', (date, sh_pool, btk_pool, price))

    db.commit()


    time.sleep(60)

db.close()