# csv_parser
Download CSV-file, read it and write data to db

1 Installation:

1) $ cd csv_parser

2) $ virtualenv .env

3) $ source .env/bin/activate

4) $ pip install -r requirements.txt

5) $ createuser -U postgres parser --interactive

6) $ createdb -U parser parser

7) $ ./manage.py migrate

8) $ ./manage.py collectstatic

9) $ ./manage.py runserver

10) http://localhost:8000/admin/main/parserdata/
    login: admin
    password: csv123456
    
11) "ЗАГРУЗИТЬ ИЗ SCV" (кнопка справа вверху)

12) Прикрепить файл parser_data.csv (во вложении), или подобный по структуре файл. Выполнить загрузку

13) http://localhost:8000 - графики
