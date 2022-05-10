import os
import requests
import json

LINEBot_SERVERURL = os.getenv('LINEBot_SERVERURL')

def get_cgh(env_dict):
    url = f'https://reg.cgh.org.tw/tw/checkUp/cghCovidReport.jsp?divisionNo={env_dict["divisionNo"]}&chartId={env_dict["chartId"]}&selectYear={env_dict["selectYear"]}&selectMonth={env_dict["selectMonth"]}&selectDay={env_dict["selectDay"]}&gatherYear={env_dict["gatherYear"]}&gatherMonth={env_dict["gatherMonth"]}&gatherDay={env_dict["gatherDay"]}'
    res = requests.post(url)
    return res

def notofy_LINEBot(result):
    res = requests.get(f'{LINEBot_SERVERURL}?result={result}')
    print(res)
    return res