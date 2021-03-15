from database import Database
from sys import argv
from os import getenv
from dotenv import load_dotenv
load_dotenv()

if len(argv) == 2 and argv[1] == 'setup':
    print('Tworze tabele w bazie danych')
    db = Database(getenv('DB_NAME'))
    db.create_table('CREATE TABLE urls (id INTEGER PRIMARY KEY AUTOINCREMENT, category TEXT, url TEXT) ')

if len(argv) == 4 and argv[1] == 'add':
    print('Dodaję nowy adres url')
    category = argv[2]
    url = argv[3]
    db = Database(getenv('DB_NAME'))
    db.insert('urls', None, category, url)
