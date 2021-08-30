import sqlite3

class DB():
    def __init__(self, name, mysql=False):
        if ( not mysql ):
            self.connection = sqlite3.connect(name)
            self.cursor = self.connection.cursor()
            self.type='sqlite3'
        else:
            import pymysql
            self.connection = pymysql.connect(host=mysql['host'], user=mysql['user'], 
    password=mysql['password'], db=mysql['db'])
            self.cursor = self.connection.cursor()
            self.type='mysql'

    def save(self):
        self.connection.commit()
    def create(self, name:str, vars:str):
        # Создание таблицы name с колумнами vars.
        self.cursor.execute(f"""CREATE TABLE IF NOT EXISTS {name} {vars}""")
        self.save()
    def get(self, table, column, uslovie='', fetch='all'):
        # Получение значения column из базы данных table с условием sort_type
        self.cursor.execute(f'SELECT {column} FROM {table} {uslovie}')

        if fetch=='all':
            return self.cursor.fetchall()
        else:
            return self.cursor.fetchone()
    def update(self, table, column, value, uslovie=''):
        # Просто обновить значение column в table на value с условием uslovie
        self.cursor.execute(f'UPDATE {table} SET {column} = {value} {uslovie}')
    def add(self, table, values, uslovie=''):
        # Ввод новых данных values в table с условием uslovie
        if self.type=='sqlite3':
            self.cursor.execute(f"""INSERT INTO {table} VALUES {str(tuple(["?" for i in values.split(",")])).replace("'", "")} {uslovie}""", values.split(','))
        elif self.type=='mysql':
            self.cursor.execute(f'INSERT INTO {table}  VALUES {values} {uslovie}')
        self.save()