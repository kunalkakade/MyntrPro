import csv
import json
import pandas as pd

from flask import Flask

app = Flask(__name__)
data = []
xl_file = pd.ExcelFile('./static/myntra.xlsx')

dfs = pd.read_excel(xl_file, sheet_name="Sheet0")[:50]
# print(dfs)
# dfs.to_dict()


@app.route('/products')
def list_products():
    return dfs.to_json(orient='records', lines=True)


if __name__ == '__main__':
    app.run()
