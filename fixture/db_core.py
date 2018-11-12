from db import DB


class DBcore:
    def __init__(self):
        self.db = DB(username='webdeploy', password='123Abc+-=', hostname='phxm1bappd34\\tsop', dbtype='mssql')

    def get_configurable_values_category(self):
        new_set = []
        query = 'SELECT [Category] FROM [PCAD].[dbo].[ConfigurableValue]'
        lst = self.db.query(query)
        for item in lst.values:
            new_set.append(item[0])
        return sorted(set(new_set), key=lambda s: s.lower())

#
# if __name__ == "__main__":
#     Data = DBcore()
#     print(Data.get_configurable_values_category())
