# coding: utf8

import sqlite3
import hashlib

def create_user(status, username, password):
    # status: 0 - admin, 1 - врач

    # Хеширование пароля
    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()

    # Подключение к нашей базе данных
    conn = sqlite3.connect('Database/database.db')
    c = conn.cursor()

    # Добавление нового пользователя
    c.execute('INSERT INTO users (status, username, password) VALUES (?, ?, ?)', (status, username, hashed_password))

    # Сохранение изменений и закрытие соединения с базой данных
    conn.commit()
    conn.close()

# Замените 'admin' и 'your_password' на желаемые имя пользователя и пароль
#create_user(0, 'admin', 'your_password')
# create_user(1, 'doctor', 'doctor')