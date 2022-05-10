# -*- coding:utf-8 -*-
from app import WEB_API
from bs4 import BeautifulSoup
import os
from flask import jsonify

def get_env():
    env_dict = {
        'divisionNo':os.getenv('divisionNo'),
        'chartId':os.getenv('chartId'),
        'selectYear':os.getenv('selectYear'),
        'selectMonth':os.getenv('selectMonth'),
        'selectDay':os.getenv('selectDay'),
        'gatherYear':os.getenv('gatherYear'),
        'gatherMonth':os.getenv('gatherMonth'),
        'gatherDay':os.getenv('gatherDay'),
    }
    return env_dict

def get_cghPage(env_dict):
    cghPage = WEB_API.get_cgh(env_dict)
    doc = BeautifulSoup(cghPage.text, "html.parser")
    return doc.find('td', {'data-th': '報告結果'}).get_text()

def cgh_crawler():
    env_dict = get_env()
    result = get_cghPage(env_dict)

    return jsonify({'result': result.encode().decode()})