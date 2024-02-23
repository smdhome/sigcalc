# SIGNA Calculator 
#
# This Python program displays the current prices of SIGNA, BTC, 
# LTC, and ETH in USD.  It also displays the price of Signum (SIGNA) in 
# terms of USD, BTC, LTC, and ETH based on information from the 
# CoinGecko API.  This program uses tkinter for graphics.
# It uses the requests library to make HTTP requests to the API.
#
# Make sure Python is installed and the requests and tkinter 
# libraries are available in your environment. If not, you can 
# install it using the following commands:
#
# pip install requests
# pip install tkinter
#
import tkinter as tk
import requests

class SignumPriceCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Signa Price Calculator")

        # Create labels
        self.sig_usd_prefix = tk.Label(root, text="SIGNA=")
        self.sig_usd_suffix = tk.Label(root, text="USD")
        self.btc_usd_prefix = tk.Label(root, text="BTC=")
        self.btc_usd_suffix = tk.Label(root, text="USD")
        self.ltc_usd_prefix = tk.Label(root, text="LTC=")
        self.ltc_usd_suffix = tk.Label(root, text="USD")
        self.eth_usd_prefix = tk.Label(root, text="ETH=")
        self.eth_usd_suffix = tk.Label(root, text="USD")
        self.sig_btc_prefix = tk.Label(root, text="SIGNA=")
        self.sig_btc_suffix = tk.Label(root, text="BTC")
        self.sig_ltc_prefix = tk.Label(root, text="SIGNA=")
        self.sig_ltc_suffix = tk.Label(root, text="LTC")
        self.sig_eth_prefix = tk.Label(root, text="SIGNA=")
        self.sig_eth_suffix = tk.Label(root, text="ETH")

        # Create entry widgets
        self.sig_usd_entry = tk.Entry(root)
        self.btc_usd_entry = tk.Entry(root)
        self.ltc_usd_entry = tk.Entry(root)
        self.eth_usd_entry = tk.Entry(root)
        self.sig_btc_entry = tk.Entry(root)
        self.sig_ltc_entry = tk.Entry(root)
        self.sig_eth_entry = tk.Entry(root)

        # Create a button to fetch prices
        self.fetch_button = tk.Button(root, text="Fetch Prices", command=self.fetch_prices)

        # Create a button to exit
        self.exit_button = tk.Button(root, text="Exit", command=root.destroy)

        # Grid layout
        self.sig_usd_prefix.grid(row=0, column=0, sticky='e')
        self.sig_usd_entry.grid(row=0, column=1)
        self.sig_usd_suffix.grid(row=0, column=2, sticky='w')

        self.btc_usd_prefix.grid(row=1, column=0, sticky='e')
        self.btc_usd_entry.grid(row=1, column=1)
        self.btc_usd_suffix.grid(row=1, column=2, sticky='w')

        self.ltc_usd_prefix.grid(row=2, column=0, sticky='e')
        self.ltc_usd_entry.grid(row=2, column=1)
        self.ltc_usd_suffix.grid(row=2, column=2, sticky='w')

        self.eth_usd_prefix.grid(row=3, column=0, sticky='e')
        self.eth_usd_entry.grid(row=3, column=1)
        self.eth_usd_suffix.grid(row=3, column=2, sticky='w')

        self.sig_btc_prefix.grid(row=4, column=0, sticky='e')
        self.sig_btc_entry.grid(row=4, column=1)
        self.sig_btc_suffix.grid(row=4, column=2, sticky='w')

        self.sig_ltc_prefix.grid(row=5, column=0, sticky='e')
        self.sig_ltc_entry.grid(row=5, column=1)
        self.sig_ltc_suffix.grid(row=5, column=2, sticky='w')

        self.sig_eth_prefix.grid(row=6, column=0, sticky='e')
        self.sig_eth_entry.grid(row=6, column=1)
        self.sig_eth_suffix.grid(row=6, column=2, sticky='w')

        self.fetch_button.grid(row=7, column=1, sticky='ew')
        self.exit_button.grid(row=7, column=2, sticky='ew')

    def fetch_prices(self):
        # Setup the base URL and parameters for Coingecko.
        url = "https://api.coingecko.com/api/v3/simple/price"
        params = {
            "ids": "signum,bitcoin,litecoin,ethereum",
            "vs_currencies": "usd,btc,ltc,eth"
        }
        # Get the data needed.
        response = requests.get(url, params=params)
        if response.status_code != 200:
            print("Failed to retrieve data from the API")
        else:
            data = response.json()
            sig_price = data.get("signum", {})
            self.sig_usd_entry.delete(0, tk.END)
            self.sig_usd_entry.insert(0, '{:.8f}'.format(sig_price.get("usd")))
            self.sig_btc_entry.delete(0, tk.END)
            self.sig_btc_entry.insert(0, '{:.8f}'.format(sig_price.get("btc")))
            self.sig_ltc_entry.delete(0, tk.END)
            self.sig_ltc_entry.insert(0, '{:.8f}'.format(sig_price.get("ltc")))
            self.sig_eth_entry.delete(0, tk.END)
            self.sig_eth_entry.insert(0, '{:.8f}'.format(sig_price.get("eth")))
                        
            btc_price = data.get("bitcoin", {})
            self.btc_usd_entry.delete(0, tk.END)
            self.btc_usd_entry.insert(0, '{:.2f}'.format(btc_price.get("usd")))

            ltc_price = data.get("litecoin", {})
            self.ltc_usd_entry.delete(0, tk.END)
            self.ltc_usd_entry.insert(0, '{:.2f}'.format(ltc_price.get("usd")))

            eth_price = data.get("ethereum", {})
            self.eth_usd_entry.delete(0, tk.END)
            self.eth_usd_entry.insert(0, '{:.2f}'.format(eth_price.get("usd")))

if __name__ == "__main__":
    root = tk.Tk()
    app = SignumPriceCalculator(root)
    root.mainloop()
