from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.request
from bs4 import BeautifulSoup
from datetime import datetime
import os

def exchange(): # This part of the program uses the selenium API to open the Republic Bank webpage with the javascript enabled to download the current exchange from from TTD to USD
    driver = webdriver.PhantomJS('./\phantomjs.exe') # Opens the particular driver for my instance I am using Google Chrome and you have to download a specific driver for it for selenium
    driver.get("https://www.republictt.com/personal/forex-rates")
    for row in driver.find_elements_by_class_name("table-striped"): #This uses selenium to look at the table containing the different exchange rates and looks at the USD rate of selling USD
        length = len(row.find_elements_by_tag_name("td"))
        cell = row.find_elements_by_tag_name("td")[length-2]
        ttd_rate = float(cell.text)
        print("The current exchange rate is $1 USD = $%.4f TTD" %(ttd_rate))
        break
    driver.close()
    driver.quit()
    return (ttd_rate)

def coins():
#This part of the program takes a text file that contains the differing cryptocurrencies
#amount the user has and gets the value and then multiplies it by the current amount the cryptocurrency is at which is provided by the prices function() and prints the amount you have in USD

    fact = False
    place = 0
    sum = 0
    temp = ""
    file = open("Cryptocurrencies.txt", "r")
    for line in file:
        for x in line:
            if(fact == True):
                temp += x
            if (x == " "):
                fact = True
        num = float(temp.strip())
        value = num * prices(place)
        print("You have %.2f USD\n" %(value))
        sum += value
        temp = ""
        fact = False
        place += 1
    return (sum)

def coins1():
#This part of the program takes a text file that contains the differing cryptocurrencies
#amount the user has and gets the value and then multiplies it by the current amount the cryptocurrency is at which is provided by the prices function() and prints the amount you have in USD

    fact = False
    place = 0
    sum = 0
    temp = ""
    file = open("CryptocurrenciesMom.txt", "r")
    for line in file:
        for x in line:
            if(fact == True):
                temp += x
            if (x == " "):
                fact = True
        num = float(temp.strip())
        value = num * prices1(place)
        print("You have %.2f USD\n" %(value))
        sum += value
        temp = ""
        fact = False
        place += 1
    return (sum)

def prices(place):
#This part of the program uses the BeautifulSoup library and takes the html of coinmarket and finds the a tag associated with each cryptocurrency and takes the text associated
#with that tag and passes that value back to the coins() function
    
    url = urllib.request.urlopen("https://coinmarketcap.com/all/views/all/")#Had to change from normal coinmarket to include Bitcoin Gold original was https://coinmarketcap.com/
    soup = BeautifulSoup(url, "html.parser")
    values = ["a[href*=/currencies/bitcoin/#markets]", "a[href*=/currencies/bitcoin-cash/#markets]",
              "a[href*=/currencies/ethereum/#markets]", "a[href*=/currencies/litecoin/#markets]",
              "a[href*=/currencies/neo/#markets]", "a[href*=/currencies/bitcoin-gold/#markets]"]
    currency= ["Bitcoin", "Bitcoin Cash", "Ethereum", "Litecoin", "Neo", "Bitcoin Gold"]
    Symbol = ["BTC", "BCH", "ETH", "LTC", "NEO", "BTG"]
    a = soup.select_one(values[place]).text
    temp = a.replace("$", "")
    a_new = float(temp)
    print("%s: 1 %s = %.2f USD" %(currency[place],Symbol[place], a_new))
    return (a_new)

def prices1(place):
#This part of the program uses the BeautifulSoup library and takes the html of coinmarket and finds the a tag associated with each cryptocurrency and takes the text associated
#with that tag and passes that value back to the coins() function
    
    url = urllib.request.urlopen("https://coinmarketcap.com/all/views/all/")#Had to change from normal coinmarket to include Bitcoin Gold original was https://coinmarketcap.com/
    soup = BeautifulSoup(url, "html.parser")
    values = ["a[href*=/currencies/bitcoin/#markets]","a[href*=/currencies/neo/#markets]",
              "a[href*=/currencies/gas/#markets]", "a[href*=/currencies/substratum/#markets]",
              "a[href*=/currencies/red-pulse/#markets]","a[href*=/currencies/unikoin-gold/#markets]",
              "a[href*=/currencies/bounty0x/#markets]"]
    currency= ["Bitcoin", "Neo", "Gas",  "Substratum", "Red Pulse", "Unikoin Gold", "Bounty0x"]
    Symbol = ["BTC", "NEO", "GAS", "SUB", "RPX", "UKG", "BNTY"]
    a = soup.select_one(values[place]).text
    temp = a.replace("$", "")
    a_new = float(temp)
    print("%s: 1 %s = %.2f USD" %(currency[place],Symbol[place], a_new))
    return (a_new)


#The main program starts here
#The main part of the program calculates how much profit you gained from your initial investment
#Ans = input("Do you need to convert to USD (Y/N)\n")
Ans = "N"
if(Ans == "Y"):
    #money = int(input("How much money do you need to convert\n"))
    money = 3000
    ttd_rate = exchange()
    value = money / ttd_rate #This converts the USD to TTD
    print("$%d TTD = $%.4f USD" %(money, value))
initial = 2600
initial1 = 1000
print("Keanu's Cryptocurrency:")
sum = coins()
ans = str(round(sum, 2))
file = open("sum1.txt", "a")
if(os.stat("sum1.txt").st_size == 0):
    file.write("Amount\t\t\tPercent Increase\t\tDate\n")
file.write("$" + ans + " USD\t\t")
increase = ((sum - initial) / initial) * 100
inc = str(round(increase, 2))
file.write(str(inc) + "%\t\t\t\t")
file.write(str(datetime.now()))
file.write("\n")
file.close()
y = "%"
print("Your running total is %.2f USD and your increase from the initital amount of $%d is %.2f%s" %(sum, initial, increase, y))
print()
test = input()

