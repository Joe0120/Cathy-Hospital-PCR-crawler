import json
import re
from app import app, WEB_API, cgh_crawler
from flask import jsonify
from flask_cors import CORS

app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app, support_credentials=True)


@app.route('/')
def index():
    return jsonify({'result':'u r ready to go :)'}), 200

@app.route('/cgh')
def cgh():
    result = cgh_crawler.cgh_crawler()
    return jsonify({'result': result}), 200


@app.route('/check')
def check_result():
    result = cgh_crawler.cgh_crawler()
    if result != '報告尚未出來':
        WEB_API.notofy_LINEBot(result)
    return result, 200