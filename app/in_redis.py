import redis
import datetime
from datetime import datetime

r = redis.Redis(db=0)
links = ["http://yandex.ru?q=123", "http://yandex.ru", "yandex.ru"]

# Очистка базы данных: очистка старых записей
r.flushdb()

# Добавление записей
count = 1
timestamp = round(datetime.today().timestamp())
for link in links:
    # временная метка
    # timestamp = round(datetime.today().timestamp())
    # timestamp = datetime.today().timestamp()
    r.set(str(timestamp + count), link)
    print(r.keys())
    count += 1

for key in r.scan_iter():
    print(key, r.get(key))
