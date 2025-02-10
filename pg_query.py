import psycopg2
import sys

# Параметры подключения к PostgreSQL
DB_NAME = "your_database"
DB_USER = "your_user"
DB_PASSWORD = "your_password"
DB_HOST = "your_host"
DB_PORT = "5432"

# SQL-запрос (принимается как аргумент командной строки)
query = sys.argv[1]

try:
    # Подключение к базе данных
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    cur = conn.cursor()

    # Выполнение SQL-запроса
    cur.execute(query)

    # Получение результата
    result = cur.fetchone()[0]

    # Вывод результата (Zabbix будет использовать это значение)
    print(result)

except Exception as e:
    # В случае ошибки выводим сообщение
    print(f"Error: {e}")
    sys.exit(1)

finally:
    # Закрытие соединения
    if cur:
        cur.close()
    if conn:
        conn.close()