import requests
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
URL_MGR = "http://localhost:5001"
URL_DATA = "http://localhost:5002"

@app.route('/')
def index():
    """Рендеринг frontend через Jinja2"""
    return render_template('index.html')

@app.route('/load', methods=['POST'])
@app.route('/update_currency', methods=['POST'])
@app.route('/delete', methods=['POST'])
def proxy_mgr():
    """Проксирование запросов к currency-manager"""
    resp = requests.post(f"{URL_MGR}{request.path}", json=request.get_json())
    return jsonify(resp.json()), resp.status_code

@app.route('/convert', methods=['GET'])
@app.route('/currencies', methods=['GET'])
def proxy_data():
    """Проксирование запросов к data-manager"""
    resp = requests.get(f"{URL_DATA}{request.path}", params=request.args)
    return jsonify(resp.json()), resp.status_code

if __name__ == '__main__':
    app.run(port=5000)