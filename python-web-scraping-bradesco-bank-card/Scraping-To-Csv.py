# Web Scraping to CSV

import csv
from urllib.request import urlopen
# in terminal "pip install beautifulsoup4"
from bs4 import BeautifulSoup

with open("Bradesco_8252022_112950 AM.html") as fp:
    soup = BeautifulSoup(fp, "html.parser")
    # print(soup.body.text)
    # test = list(soup.children)
    #for item in list(soup.children):
    #   print(item)

    # print(soup.body.div.page.div.div.table.tbody.tr.trMarginTop.td.div.table.tbody.tr.td.span)
    # tr_elements = soup.find_all('table')[2].find_all('tr')
    # print(tr_elements)

    # test = list(soup.find_all('table')[2].find_all('tr'))
    # for item in test:
    #    print(item)

    # print(soup.body.get_text())
    for item in range(10000):
        # name purchase
        # print(soup.find_all('table')[item].find_all('span')[0].get_text())

        # name purchase
        #print(soup.find_all('div')[item].find_all('span')[0].get_text())


        # date
        dateBuy = soup.find_all('span', attrs={'style':'font-size: small;'})[item].get_text()
        print(dateBuy)

        # month
        month = soup.find_all('span', attrs={'style':'font-size: x-small'})[item].get_text()
        print(month)

        # variable datemonth
        dateMonth = dateBuy + month

        # name purchase and purchase
        # purchase = soup.find_all('span', attrs={'style': 'width:100%;font-size: x-small;color: black;width:100%'})[item].get_text()
        blank = ["' '", "''", "", " ", ' ', '']
        namePurchaseBefore = ""
        namePurchase = ""
        valuePurchaseBefore = ""
        valuePurchase = ""
        test = ' '
        test2 = ''
        for x in range(item, 10000):
            purchase = soup.find_all('span', attrs={'style': 'width:100%;font-size: x-small;color: black;width:100%'})[x].get_text()
            # print(purchase)
            # if purchase != test and purchase not in blank and purchase != namePurchaseBefore:
            if purchase != test and namePurchaseBefore == "":
                namePurchase = purchase
                namePurchaseBefore = namePurchase
            else:
                test2 = ''
            if purchase != test and namePurchase != purchase and purchase != valuePurchaseBefore and valuePurchaseBefore == "":
                valuePurchase = purchase
                valuePurchaseBefore = valuePurchase
            else:
                test2 = ''
            if namePurchase != test and valuePurchase != test and namePurchase != valuePurchase and namePurchase not in blank and valuePurchase not in blank:
                break
        print(namePurchase)
        print(valuePurchase)
        print("\n")

