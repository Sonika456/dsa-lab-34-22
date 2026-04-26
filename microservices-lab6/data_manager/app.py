import psycopg
from flask import Flask, request, jsonify

app = Flask(__name__)
DB_CFG = {"host": "localhost", "port": "5432", "dbname": "microservices_lab", "user": "postgres", "password": "postgres"}

def get_conn():
    return psycopg.connect(**DB_CFG)

@app.route('/convert', methods=['GET'])
def convert():
    """Конвертация суммы по курсу из БД"""
    name = request.args.get('currency')
    amount = request.args.get('amount', type=float)
    
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT rate FROM currencies WHERE currency_name = %s", (name,))
    row = cur.fetchone()
    if not row:
        return jsonify({"error": "Валюта не найдена"}), 404
        
    rate = float(row[0])
    return jsonify({"currency": name, "amount": amount, "rate": rate, "converted_amount": amount * rate}), 200

@app.route('/currencies', methods=['GET'])
def get_all():
    """Возврат списка всех валют"""
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id, currency_name, rate FROM currencies ORDER BY id")
    # Формирование списка словарей из результата запроса
    data = [{"id": r[0], "currency_name": r[1], "rate": float(r[2])} for r in cur.fetchall()]
    return jsonify(data), 200

if __name__ == '__main__':
    app.run(port=5002)