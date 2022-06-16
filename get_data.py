from eospy.cleos import Cleos
import datetime
import sqlite3

ce = Cleos(url='https://api.wax.alohaeos.com')
arguments = {
    "code": "miningntwrkc",
    "scope": "miningntwrkc",
    "table": "config"
}

db = sqlite3.connect('btk_prices.db')

# Create cursor
cursor = db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS prices (
     date DATETIME,
     sh_pool INT,
     btk_pool INT,
     btk_price FLOAT
)""")

# Get the data from blockchain
get_data = ce.get_table(arguments['code'], arguments['scope'], arguments['table'])
line_data = get_data['rows'][0]
sh_pool     = int(line_data['shares_pool'])
btk_pool    = line_data['tokens_pool']
price       = btk_pool / sh_pool / 10
date        = datetime.datetime.now()

#print(f'{date}, {price}, {sh_pool}, {btk_pool}')

cursor.execute('INSERT INTO prices VALUES (?, ?, ?, ?)', (date, sh_pool, btk_pool, price))

db.commit()

db.close()

# def animate(i):
#     data_file = open('prices.csv', 'a')
#
#     get_data = ce.get_table(arguments['code'], arguments['scope'], arguments['table'])
#     line_data = get_data['rows'][0]
#     sh_pool = int(line_data['shares_pool'])
#     btk_pool = line_data['tokens_pool']
#     y = btk_pool / sh_pool * 1000
#     x = datetime.datetime.now().strftime("%H:%M:%S")
#     data_file.write(f'{x},{y}\n')
#     data_file.close()
#
#     data_file = open('prices.csv', 'r').read()
#     lines = data_file.split("\n")
#     del lines[-1]
#     xs = []
#     ys = []
#
#     for line in lines:
#         x, y = line.split(',')
#         xs.append(x)
#         ys.append(float(y))
#
#     ax.clear()
#     ax.plot(xs, ys)
#
#     plt.xlabel('Date')
#     plt.ylabel('Price')
#     plt.title('Realtime Data for BTK price BTK/SH')
#     print(x, y)