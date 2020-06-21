from urllib.request import urlopen
from bs4 import BeautifulSoup

import openpyxl
import requests
import json
import time

def dev_list_process():
    ''' Developer List Processing '''
    pageNum = 1
    developer_file = openpyxl.Workbook()
    developer_sheet = developer_file.active

    while pageNum < 1362:
        try:
            html1 = urlopen('https://www.androidrank.org/developers/ranking?&start='+str(pageNum))
            bsObject = BeautifulSoup(html1, "html.parser")
            paragraph_data = bsObject.find_all('td', style='text-align:left;')
            for a in paragraph_data:
                public_id = (a.find("a")["href"])
                public_id = public_id[14:]
                developer_sheet.append([public_id])
                developer_file.save('developer_list.xlsx')
                developer_file.close()
            print("Developer List Processing : Finish")
            pageNum += 20
            time.sleep(5.0)
        except:
            print("Developer List Processing : Fail")
            pageNum += 20
            time.sleep(50.0)
            continue