import random
from flask import Flask, request, jsonify

app = Flask(__name__)

OPERATIONS = ['sum', 'sub', 'mul', 'div']

@app.route('/number/', methods=['GET'])
def get_number():
    """
    Раздел I, задача 1: GET эндпоинт /number/, параметр query param 'param'.
    Возвращает рандомное число * param в формате JSON.
    """
    try:
        # Получаем параметр param из строки запроса
        param = request.args.get('param')
        
        if param is None:
            return jsonify({"error": "Parameter 'param' is required"}), 400
            
        param_value = int(param)
        random_number = random.randint(1, 100)
        result_number = random_number * param_value
        
        # Хотя в задании 1 не указано явно возвращать операцию, 
        # в Разделе II ожидается число и операция. Возвращаем случайную.
        operation = random.choice(OPERATIONS)
        
        return jsonify({
            "number": result_number,
            "operation": operation
        })
    except ValueError:
        return jsonify({"error": "Parameter 'param' must be a number"}), 400

@app.route('/number/', methods=['POST'])
def post_number():
    """
    Раздел I, задача 2: POST эндпоинт /number/, тело JSON с полем 'jsonParam'.
    Возвращает рандомное число * jsonParam и случайную операцию.
    """
    try:
        # Получаем данные из тела запроса
        data = request.get_json()
        
        if not data or 'jsonParam' not in data:
            return jsonify({"error": "Field 'jsonParam' is required in JSON"}), 400
            
        param_value = int(data['jsonParam'])
        random_number = random.randint(1, 100)
        result_number = random_number * param_value
        operation = random.choice(OPERATIONS)
        
        return jsonify({
            "number": result_number,
            "operation": operation
        })
    except (ValueError, TypeError):
        return jsonify({"error": "Field 'jsonParam' must be a number"}), 400

@app.route('/number/', methods=['DELETE'])
def delete_number():
    """
    Раздел I, задача 3: DELETE эндпоинт /number/.
    Возвращает сгенерированное число и случайную операцию.
    """
    random_number = random.randint(1, 100)
    operation = random.choice(OPERATIONS)
    
    return jsonify({
        "number": random_number,
        "operation": operation
    })

app.run(debug=True, port=5000)

