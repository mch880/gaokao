from flask import Flask, send_file
import json
import os

app = Flask(__name__)

DATA_FILE = os.path.join(os.path.dirname(__file__), 'data.json')

with open(DATA_FILE, 'r', encoding='utf-8') as f:
    ALL_DATA = json.load(f)

# 预序列化 JSON，避免每次请求重复 jsonify 3.9MB 数据
_CACHED_JSON = json.dumps(ALL_DATA, ensure_ascii=False)

@app.route('/')
def index():
    return send_file('index.html')

@app.route('/api/data')
def get_data():
    return app.response_class(_CACHED_JSON, mimetype='application/json')

@app.route('/health')
def health():
    return {'status': 'ok', 'records': len(ALL_DATA)}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=51985)
