import psycopg
from flask import Flask, request, jsonify

app = Flask(__name__)
# Параметры подключения к PostgreSQL
DB_CFG = {"host": "localhost", "port": "5432", "dbname": "microservices_lab", "user": "postgres", "password": "postgres"}

def get_conn():
    """Создание подключения к БД"""
    return psycopg.connect(**DB_CFG)

@app.route('/load', methods=['POST'])
def load():
    """Добавление валюты с проверкой уникальности"""
    data = request.get_json()
    name, rate = data.get('currency_name'), data.get('rate')
    
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id FROM currencies WHERE currency_name = %s", (name,))
    if cur.fetchone():
        return jsonify({"error": "Валюта уже существует"}), 400
        
    cur.execute("SELECT COALESCE(MAX(id), 0) + 1 FROM currencies")
    cur.execute("INSERT INTO currencies VALUES (%s, %s, %s)", (cur.fetchone()[0], name, rate))
    conn.commit()
    return jsonify({"message": "OK"}), 200

@app.route('/update_currency', methods=['POST'])
def update():
    """Обновление курса существующей валюты"""
    data = request.get_json()
    name, rate = data.get('currency_name'), data.get('rate')
    
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id FROM currencies WHERE currency_name = %s", (name,))
    if not cur.fetchone():
        return jsonify({"error": "Валюта не найдена"}), 404
        
    cur.execute("UPDATE currencies SET rate = %s WHERE currency_name = %s", (rate, name))
    conn.commit()
    return jsonify({"message": "OK"}), 200

@app.route('/delete', methods=['POST'])
def delete():
    """Удаление валюты из БД"""
    name = request.get_json().get('currency_name')
    
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id FROM currencies WHERE currency_name = %s", (name,))
    if not cur.fetchone():
        return jsonify({"error": "Валюта не найдена"}), 404
        
    cur.execute("DELETE FROM currencies WHERE currency_name = %s", (name,))
    conn.commit()
    return jsonify({"message": "OK"}), 200

if __name__ == '__main__':
    app.run(port=5001)