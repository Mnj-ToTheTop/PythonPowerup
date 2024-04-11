import requests
from bs4 import BeautifulSoup
import time

product_url = "https://www.flipkart.com/casio-fx-82es-plus-2nd-scientific-calculator/p/itmehqxjh85myyg9?pid=CALFRJKGAU4V5CSQ&lid=LSTCALFRJKGAU4V5CSQYDP3SM&marketplace=FLIPKART&store=dgv&srno=b_1_2&otracker=browse&fm=organic&iid=en_YTT3n43GXz7LZvFD3Eu3Rw_TUukFf_gbOXC9AfjvYEZ7lLtAz9yCsKMRRIeafIv5ylMosV8CUDRobyoC8q9U0vUFjCTyOHoHZs-Z5_PS_w0%3D&ppt=None&ppn=None&ssid=7g97f9mb0g0000001711182479168"
target_price = 700

# Web Scraping. Scraping the data out of the website

def check_price():
    try:
        r = requests.get(product_url)
        soup = BeautifulSoup(r.content)
        price = soup.find('div', attrs = {"class":"_16Jk6d"}).text
        price_without_rupees = price[1:]
        price_witout_comma = price_without_rupees.replace(',','')
        int_price = int(price_without_comma)
        return int_price
    except:
        check_price()

cur_price = check_price()
print(f"Current price is {cur_price}")

print("Waiting")

while True:
    cur_price = check_price()
    if cur_price <= target_price:
        print(f"target reached")
        break
    time.sleep(60)
