from jinjasql import JinjaSql
import connector
from mysql.connector import Error


class DB_modification(object):
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

    def execute_read_query(self, query, data):
        cursor = self.bd.cursor()
        result = None
        try:
            cursor.execute(query, data)
            result = cursor.fetchall()
            return result
        except Error as e:
            print(f"The error '{e}' occurred")

    def send_query(self, template, data, method="edit"):
        query, bind_params = self.j.prepare_query(template, data)
        if method == "get":
            return self.execute_read_query(query, bind_params)
        elif method == "edit":
            return self.execute_query(query, bind_params)

    # search day in timetable
    def get_classroom(self):
        template = """
                    SELECT
                        l.*,
                        w.day
                    from software_engineering.lessons l
                    join software_engineering.classroom c on c.id = l.classroom
                    join software_engineering.week w on w.id = c.day_of_week
                """
        data = {
        }
        return self.send_query(template, data, "get")

    def del_lesson(self, days):
        for day in days:
            template = """
                        DELETE from software_engineering.lessons where id = {{ id_l }}
            """
            data = {
                "id_l": day[0]
            }
            self.send_query(template, data, "edit")

    def add_lesson(self, days):
        template = """
                    INSERT INTO software_engineering.lessons(professor, `group`, classroom) 
                    values ({{ professor }}, {{ group }}, {{ classroom }})
        """

        for i in days:
            data = {
                "professor": i[1],
                "group": i[2],
                "classroom": i[3]
            }
            self.send_query(template, data, "edit")

    # Move the first lessons of the given days of the week to the last place
    def swap_subject(self, *days):
        days = list(days)
        table = list(self.get_classroom())
        new_table = []
        for i in table:
            day = i[4]
            if day in days:
                table.remove(i)
                new_table.append(i)
                days.remove(day)
        self.del_lesson(new_table)
        self.add_lesson(new_table)

    # Display information about teachers working on a given day of the week in a given classroom
    def print_busy_teacher(self, time, location):
        template = """
        SELECT  
            p.last_name,
            s.subject_name,
            c.location,
            w.day,
            sg.name_group,
            sg.number
        from software_engineering.lessons   
            join software_engineering.classroom c on c.id = lessons.classroom
            join software_engineering.professors p on p.id = lessons.professor
            join software_engineering.study_groups sg on sg.id = lessons.`group`
            join software_engineering.week w on w.id = c.day_of_week
            join software_engineering.subjects s on s.id = c.subject
        where day =  {{ time_s }}  and  location = {{ loc }}
        """
        data = {
            "time_s": time,
            "loc": location
        }
        teachers = self.send_query(template, data)
        for teacher in teachers:
            print(f'------------------------------------------------\n'
                  f'Professor : {teacher[0]} \n'
                  f'Subject: {teacher[1]} \n'
                  f'Location: {teacher[2]} \n'
                  f'Day: {teacher[3]} \n'
                  f'Name group: {teacher[4]} \n'
                  f'Number group: {teacher[5]} \n'
                  f'------------------------------------------------\n')

    # Display information about teachers who do not teach classes in the given day of the week.
    def print_free_teacher(self, time):
        template = """
           SELECT  
               p.last_name,
               s.subject_name,
               c.location,
               w.day,
               sg.name_group,
               sg.number
           from software_engineering.lessons   
                join software_engineering.professors p on lessons.professor = p.id
                join software_engineering.classroom c on c.id = lessons.classroom
                join software_engineering.subjects s on s.id = c.subject
                join software_engineering.study_groups sg on sg.id = lessons.`group`
                join software_engineering.week w on w.id = c.day_of_week
           where day <> {{ time_s }} 
           """
        data = {
            "time_s": time
        }
        teachers = self.send_query(template, data)
        print("Free teacher:")
        for teacher in teachers:
            print(f'------------------------------------------------\n'
                  f'Professor :{teacher[0]} \n'
                  f'Subject: {teacher[1]} \n'
                  f'Location: {teacher[2]} \n'
                  f'Day: {teacher[3]} \n'
                  f'Name group: {teacher[4]} \n'
                  f'Number group: {teacher[5]} \n'
                  f'------------------------------------------------\n')


if __name__ == '__main__':
    db = connector.DB_connector("127.0.0.1", "root", "", "software_engineering")
    connect = db.create_connection()
    show = DB_modification(connect)
    # show.print_busy_teacher('Wednesday', 'Д-305')
    # show.print_free_teacher('Thursday')
    show.swap_subject("Wednesday", "Friday")
    connect.close()
