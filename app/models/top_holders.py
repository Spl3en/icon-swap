import requests
import certifi
import json
from bs4 import BeautifulSoup as bs

def get_list (contractAddress, amount):

    data = []

    for i in range (1, 201):
        try:
            if len(data) >= int(amount):
                break
            url = 'https://etherscan.io/token/generic-tokenholders2?a=%s&s=4.0022874E%%2b26&p=%d' % (contractAddress, i)
            req = requests.get(url)
            req.raise_for_status()
        except Exception as e:
            print(e)
        else:
            soupdata = bs(req.text, "html.parser")
            table = soupdata.select('table')
            rows = table[0].select('tr')
            for row in rows:
                if (row.select('th')):
                    continue
                cols = row.select('td')
                cols = [ele.text.strip() for ele in cols]
                data.append([ele for ele in cols if ele])

    return data
