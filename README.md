# miningnetwork-price
With this small script you can calculate the most accurate price for BTK/SH pair - tokens of the game Mining Network on the WAX blockchain.
The price is calculated based on the information digged right from the blockchain. Price will be shown in BTK for 10 000 000 (10 millions) SHARES. 
This program also draws an ugly plot with the price fluctuation. Feel free to adjust the interval of animation.

This is my first attempt to develop a piece of code, so will appreciate any feedback. 

## Docker
To run the script get_data_in_csv.py in docker container just execute following commands in your CLI:
```
git clone https://github.com/alparo/miningnetwork-price.git
cd miningnetwork-price/
docker compose up --build -d
```
The file new_prices.csv will be created in the current directory and updated each minute.