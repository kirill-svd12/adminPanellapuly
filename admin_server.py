from flask import Flask, request, jsonify, send_from_directory
from admin_data import load_users_data, save_users_data, verify_admin
import os

app = Flask(__name__)

# Статические файлы
@app.route('/')
def index():
    return send_from_directory('.', 'admin_panel.html')

@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('.', path)

# API endpoints
@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    if verify_admin(data.get('login'), data.get('password')):
        return jsonify({'success': True})
    return jsonify({'success': False}), 401

@app.route('/api/users')
def get_users():
    data = load_users_data()
    return jsonify(data)

@app.route('/api/broadcast', methods=['POST'])
def broadcast():
    data = request.get_json()
    message = data.get('message')
    if not message:
        return jsonify({'error': 'No message provided'}), 400
    
    # Здесь должна быть логика отправки сообщений через бота
    # Пока просто возвращаем успешный ответ
    return jsonify({'success': True, 'message': 'Broadcast sent'})

if __name__ == '__main__':
    app.run(debug=True, port=5000) 