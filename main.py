from eospy.cleos import Cleos
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import datetime

ce = Cleos(url='https://api.wax.alohaeos.com')
arguments = {
    "code": "miningntwrkc",
    "scope": "miningntwrkc",
    "table": "config"
}

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)


def animate(i):
    data_file = open('prices.csv', 'a')

    get_data = ce.get_table(arguments['code'], arguments['scope'], arguments['table'])
    line_data = get_data['rows'][0]
    sh_pool = int(line_data['shares_pool'])
    btk_pool = line_data['tokens_pool']
    y = btk_pool / sh_pool * 1000
    x = datetime.datetime.now().strftime("%H:%M:%S")
    data_file.write(x + ',' + str(y) + '\n' )
    data_file.close()

    data_file = open('prices.csv', 'r').read()
    lines = data_file.split("\n")
    del lines[-1]
    xs = []
    ys = []

    for line in lines:
        x, y = line.split(',')
        xs.append(x)
        ys.append(float(y))

    ax.clear()
    ax.plot(xs, ys)

    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Realtime Data for BTK price BTK/SH')
    print(x, y)


ani = animation.FuncAnimation(fig, animate, interval=60000)
plt.show()
