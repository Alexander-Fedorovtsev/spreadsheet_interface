import sqlite3
import datetime


class SQLighter:
    def __init__(self, database, df):
        """Подключаемся к БД и сохраняем курсор соединения"""
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()
        self.df = df

    def update_db(self):
        """Добавляем данные в таблицу"""
        for i, row in self.df.iterrows():
            if not self.get_order(row[1]):
                with self.connection:
                    self.cursor.execute(
                        "INSERT INTO `spreadsheet_orders` (`number`,`order_number`,`cost_usd`, `cost_rub`, `delivery_date`) VALUES(?,?,?,?,?)",
                        (row[0], row[1], row[2], row[2] * 65, datetime.datetime.strptime(row[3],'%d.%m.%Y')),
                    )

    def get_order(self, order_num):
        with self.connection:
            result = self.cursor.execute(
                "SELECT number FROM `spreadsheet_orders` WHERE `order_number` = ?",
                (order_num,),
            ).fetchall()
            return bool(len(result))

    def close(self):
        """Закрываем соединение с БД"""
        self.connection.close()
