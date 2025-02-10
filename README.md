1. Создание скрипта
Скрипт может быть написан на любом языке программирования, который поддерживается на сервере Zabbix (например, Python, Bash, Perl и т.д.). 

Как это работает:
Скрипт принимает SQL-запрос как аргумент командной строки.

Подключается к PostgreSQL и выполняет запрос.

Возвращает результат в стандартный вывод (Zabbix будет использовать это значение).

2. Настройка скрипта в Zabbix
Чтобы Zabbix мог использовать этот скрипт, его нужно добавить в конфигурацию Zabbix-агента или Zabbix-сервера.

Шаги:
Сохраните скрипт на сервере Zabbix (например, в /usr/lib/zabbix/scripts/pg_query.py).

Убедитесь, что скрипт имеет права на выполнение:

```bash
chmod +x /usr/lib/zabbix/scripts/pg_query.py
```
Установите необходимые зависимости (например, psycopg2 для Python):

```bash
pip install psycopg2
```
3. Настройка UserParameter
Чтобы Zabbix-агент мог выполнять скрипт, нужно добавить UserParameter в конфигурацию агента.

Пример настройки:
Откройте файл конфигурации Zabbix-агента (обычно /etc/zabbix/zabbix_agentd.conf).

Добавьте строку:

```ini
UserParameter=pg.query[*],/usr/lib/zabbix/scripts/pg_query.py "$1"
```

Перезапустите Zabbix-агент:

```bash
systemctl restart zabbix-agent
```
4. Создание элемента данных в Zabbix
Теперь вы можете использовать ключ pg.query для создания элементов данных в Zabbix.

Пример:
Перейдите в **Configuration** → **Hosts** → выберите нужный хост.

Создайте новый элемент данных:

**Name**: PostgreSQL Query: Row Count

**Type**: Zabbix agent

**Key**: pg.query["SELECT COUNT(*) FROM your_table"]

**Update interval**: Укажите интервал обновления (например, 1m).

Сохраните элемент данных.

5. Проверка работы
Перейдите в Monitoring → Latest data и проверьте, что данные собираются.

Если данные не появляются, проверьте логи Zabbix-агента и сервера:

Логи агента: /var/log/zabbix/zabbix_agentd.log

Логи сервера: /var/log/zabbix/zabbix_server.log

6. Дополнительные советы
Безопасность: Не храните пароли в скрипте. Используйте файлы с ограниченным доступом или переменные окружения.

Обработка ошибок: Добавьте проверки на случай, если PostgreSQL недоступен или запрос неверный.

Производительность: Убедитесь, что SQL-запросы оптимизированы, чтобы не нагружать базу данных.

Пример использования в Zabbix
Мониторинг количества строк в таблице:

sql
Copy
pg.query["SELECT COUNT(*) FROM your_table"]
Мониторинг средней нагрузки:

sql
Copy
pg.query["SELECT AVG(load) FROM metrics WHERE timestamp > NOW() - INTERVAL '1 hour'"]