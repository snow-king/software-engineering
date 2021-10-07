import connector
from mysql.connector import Error
from jinjasql import JinjaSql


class DB_modify(object):
    j = JinjaSql()

    def __init__(self, bd):
        self.bd = bd

    def execute_query(self, query, data):
        cursor = self.bd.cursor()
        try:
            cursor.execute(query, data)
            self.bd.commit()
            print("Query executed successfully")
        except Error as e:
            print(f"The error '{e}' occurred")

    def append_professor(self, name):
        template = """INSERT INTO software_engineering.professors(last_name)""" \
                   """values ({{name_p}} )"""
        data = {
            'name_p': name,
        }
        query, bind_params = self.j.prepare_query(template, data)
        self.execute_query(query, bind_params)

    def update_classroom(self, location, day):
        template = """UPDATE software_engineering.classroom set day ={{day_c}} where location = {{loc}}"""
        data = {
            "loc": location,
            "day_c": day
        }
        query, bind_params = self.j.prepare_query(template, data)
        self.execute_query(query, bind_params)

    def delete_subject(self, el):
        template = """DELETE FROM software_engineering.professors WHERE last_name = {{name_p}} """
        data = {
            "name_p": el
        }
        query, bind_params = self.j.prepare_query(template, data)
        self.execute_query(query, bind_params)


if __name__ == '__main__':
    db = connector.DB_connector("127.0.0.1", "root", "", "software_engineering")
    connect = db.create_connection()
    show = DB_modify(connect)

