from typing import Dict, List
import json
import os

# Данные администраторов (логин: пароль)
ADMIN_CREDENTIALS = {
    "lapuly_admin": "lapuly2024!",
    "quest_master": "quest2024!",
    "bot_operator": "operator2024!"
}

# Путь к файлу с данными пользователей
USERS_DATA_FILE = "users_data.json"

def load_users_data() -> Dict:
    """Загрузка данных пользователей из файла"""
    if os.path.exists(USERS_DATA_FILE):
        with open(USERS_DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {"users": [], "total_users": 0}

def save_users_data(data: Dict):
    """Сохранение данных пользователей в файл"""
    with open(USERS_DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def get_total_users() -> int:
    """Получение общего количества пользователей"""
    data = load_users_data()
    return data.get("total_users", 0)

def get_all_users() -> List[Dict]:
    """Получение списка всех пользователей"""
    data = load_users_data()
    return data.get("users", [])

def add_user(user_id: int, username: str = None, first_name: str = None):
    """Добавление нового пользователя"""
    data = load_users_data()
    user = {
        "user_id": user_id,
        "username": username,
        "first_name": first_name,
        "join_date": str(datetime.now())
    }
    if user not in data["users"]:
        data["users"].append(user)
        data["total_users"] = len(data["users"])
        save_users_data(data)

def verify_admin(login: str, password: str) -> bool:
    """Проверка учетных данных администратора"""
    return login in ADMIN_CREDENTIALS and ADMIN_CREDENTIALS[login] == password 