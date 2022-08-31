# Web Scraping to CSV

import csv
from urllib.request import urlopen
# in terminal "pip install beautifulsoup4"
from bs4 import BeautifulSoup
import pandas as pd
import csv

# ***********************************************
# ***********************************************
# start open html and send csv
with open("Bradesco_Credit_Card_Bill.html") as fp:
    soup = BeautifulSoup(fp, "html.parser")

    phrase = soup.body.text

    phrase_to_list = phrase.splitlines()
    phrase_to_list = list(filter(None, phrase_to_list))
    del phrase_to_list[0:7]
    valueToBeRemoved = ['\t\t\t\t\t\t\t\xa0', '\t\t\t\t\t\t', '\xa0', "Total da fatura (final 5033):', 'R$Â\xa01.591,15", '*Valores sujeitos a alteraÃ§Ã£o o fechamento da fatura', '                    Demais telefones consulte o site Se Preferir, fale com a BIA pelo  (11) 3335 0237', '                ', '                    Atendimento de segunda a sexta-feira das 9h\tàs 18h, exceto feriados', '                ', '                    Ouvidoria 0800 727 9933', "                    Cancelamento, reclamação, informação, sugestão e elogio: Atendimento disponível 24h', '                ", 'Total da fatura (final 5033):', 'R$Â\xa01.591,15', '                    Fone Fácil Bradesco', '                    Capitais e Regiões metropolitanas 4002 0022 Demais Regiões 0800 570 0022', '                    Atendimento eletrônico disponível 24h', '                    Atendimento personalizado de segunda a sexta-feira, das 7h às 22h', '                    Cancelamento, reclamação, informação, sugestão e elogio: Atendimento disponível 24h', '                    SAC - deficiência Auditiva ou de Fala 0800 722 0099', '                    e, aos sábados das 9h às 15h. Domingos e feriados nacionais - não há expediente.' '                    SAC - AlÔ Bradesco 0800 704 8383 ', '                    e, aos sábados das 9h às 15h. Domingos e feriados nacionais - não há expediente.','                    SAC - AlÔ Bradesco 0800 704 8383 ' ]
    phrase_to_list = [value for value in phrase_to_list if value not in valueToBeRemoved]

    positionList = 0
    index = 1
    day = 0
    changes = 0
    for item in phrase_to_list:
        itemActive = item
        itemBefore = itemActive

        if index == 1:
            dayBefore = day
            day = item

        if index == 2 and item == 'AGO':
            dayMain = day
        else:
            dayMain = dayBefore

        if index == 2 and item != 'AGO' and changes == 3:
            phrase_to_list.insert(positionList+1, 'AGO')
            phrase_to_list.insert(positionList+1, dayBefore)
            changes = 1

        if index == 2 and item != 'AGO' and changes <= 2:
            phrase_to_list.insert(positionList-1, 'AGO')
            phrase_to_list.insert(positionList-1, dayMain)
            changes += 1
            day = dayMain
            dayBefore = dayMain

        if index == 4:
            index = 0
            changes = 0

        # test
        if item == "17":
            test33 = 0

        if index == 4 and item == 'AGO':
            dayBefore = itemBefore
            day = itemBefore
            # phrase_to_list.remove(positionList - 2)
            del phrase_to_list[positionList - 1]
            index = 2

        index += 1
        positionList += 1

    listForCard = list()
    listTemporaly = list()
    index = 0
    for item in phrase_to_list:
        listTemporaly.append(item)
        copiedListTemporaly = listTemporaly[:]

        if index == 3:
            listForCard.append(copiedListTemporaly)
            index = 0
            listTemporaly.clear()
        else:
            index += 1

    print(listForCard)

    header = ['DAY', 'MONTH', 'NAME_PREASURE', 'VALUE_PREASURE']

    with open('card.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        # write the header
        writer.writerow(header)

        # write multiple rows
        writer.writerows(listForCard)
# end open html and send csv
# ***********************************************
# ***********************************************

# csv to google sheets
