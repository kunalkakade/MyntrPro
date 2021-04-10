import csv
import json
import pandas as pd

from flask import Flask
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
data = []
xl_file = pd.ExcelFile('./static/myntra.xlsx')

dfs = pd.read_excel(xl_file, sheet_name="Sheet0")[:50]
# print(dfs)
# dfs.to_dict()


@app.route('/products')
def list_products():
    return dfs.to_json(orient='records', lines=True)


@app.route('/')
def main():
    return "hi there"

if __name__ == '__main__':
    app.run()
