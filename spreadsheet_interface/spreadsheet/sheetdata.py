import gspread
from oauth2client.service_account import ServiceAccountCredentials as sac
import pandas as pd
from .SQLint import SQLighter
import datetime


class Gsheet2df():
    def __init__(self, spreadsheet_name, sheet_num=0):
        self.spreadsheet_name = spreadsheet_name
        self.sheet_num = sheet_num
        self.df = self.getsheet()

    def getsheet(self):
        scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
        credentials_path = 'spreadsheet_interface/templates/python-project-357307-45177e0edc6f.json'
        credentials = sac.from_json_keyfile_name(credentials_path, scope)
        client = gspread.authorize(credentials)
        sheet = client.open(self.spreadsheet_name).get_worksheet(self.sheet_num).get_all_records()
        df =  pd.DataFrame.from_dict(sheet)
        return df

    def add_in_db(self, db):
        """Добавляем данные в таблицу БД"""
        for i, row in self.df.iterrows():
            if not db.get_city_names(row[0]):
                db.add_city(row[0],row[1],row[2])


if __name__=="__main__":
    df = Gsheet2df("Kanal_test").df
    base = SQLighter("spreadsheet_interface/db.sqlite3",df)
    base.update_db()
    for i in range(0,1):
        for col_name, data in df.items():
            print("colname", col_name, "\ndata", data[i])

    

