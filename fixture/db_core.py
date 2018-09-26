from db import DB

class DataBaseHelper:
    def __init__(self):
        self.db = DB(username='webdeploy', password='123Abc+-=', hostname='phxm1bappd34\\tsop',dbtype='mssql')



# if __name__ == "__main__":
#     query = 'SELECT TOP (1000) [UserId] '\
#       ',[Name]'\
#   'FROM [LTC].[dbo].[User]'
#     datab = DataBaseHelper()
#     print (datab.db.query(query))

