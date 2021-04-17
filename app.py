import pandas as pd

from flask import Flask
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
data = []
xl_file = pd.ExcelFile('./static/myntra.xlsx')

dfs = pd.read_excel(xl_file, sheet_name="Sheet0")[:800]


@app.route('/products')
def list_products():
    return dfs.to_json(orient='records')


@app.route('/products/mens')
def list_products_mens():
    # print(dfs)
    df1 = dfs[dfs['brand'].str.contains("Men")]
    return df1.to_json(orient='records')


@app.route('/products/women')
def list_products_women():
    # print(dfs)
    df1 = dfs[dfs['brand'].str.contains("Women")]
    return df1.to_json(orient='records')


@app.route('/products/boys')
def list_products_boy():
    df1 = dfs[dfs['brand'].str.contains("Boys")]
    return df1.to_json(orient='records')


@app.route('/products/girls')
def list_products_girl():
    df1 = dfs[dfs['brand'].str.contains("Girls")]
    return df1.to_json(orient='records')


@app.route('/')
def main():
    return "hi there"


if __name__ == '__main__':
    app.run()
