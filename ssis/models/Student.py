from ..extension import mysql

# CREATE TABLE IF NOT EXISTS student (
# 	id VARCHAR(20) PRIMARY KEY,
#     firstname VARCHAR(255) NOT NULL,
#     lastname VARCHAR(255) NOT NULL,
#     course_code VARCHAR(20) NOT NULL,
#     year INT NOT NULL,
#     size ENUM('Male', 'Female', 'Other') NOT NULL,
#     FOREIGN KEY (course_code) REFERENCES course(code) ON DELETE CASCADE ON UPDATE CASCADE
# );


class Student():
    def __init__(self, id=None, firstname=None, lastname=None, course_code= None, year=None, gender=None):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.course_code = course_code
        self.year=year
        self.gender = gender
        self.connection = mysql.connection

    def add(self):
        cursor = self.connection.cursor()
        cursor.execute(" INSERT INTO student (id, firstname, lastname, course_code, year, gender) VALUES (%s, %s, %s, %s, %s, %s)",
                            (self.id, self.firstname,self.lastname, self.course_code, self.year, self.gender))
        self.connection.commit()
        cursor.close()
    
    def update(self,id):
        cursor = self.connection.cursor()
        cursor.execute("UPDATE student SET id=%s, firstname=%s, lastname=%s, course_code=%s, year=%s, gender=%s WHERE id=%s" , (self.id, self.firstname,self.lastname, self.course_code, self.year, self.gender,id))
        self.connection.commit()
        cursor.close()

    def delete(self):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM student WHERE id=%s", (self.id,))
        self.connection.commit()
        cursor.close()

    @classmethod
    def search(cls, input,filter):
        cursor = mysql.connection.cursor()
        students = []
        if filter == "0":
            cursor.execute("SELECT * FROM student WHERE id LIKE %s OR firstname LIKE %s OR lastname LIKE %s OR course_code LIKE %s OR year LIKE %s OR gender LIKE %s", (f"%{input}%",f"%{input}%",f"%{input}%",f"%{input}%",f"%{input}%",f"%{input}%"))
        elif filter =="1":
            cursor.execute("SELECT * from student WHERE id LIKE %s", (f"%{input}%",))
        elif filter =="2":
            cursor.execute("SELECT * from student WHERE firstname LIKE %s", (f"%{input}%",))
        elif filter =="3":
            cursor.execute("SELECT * from student WHERE lastname LIKE %s", (f"%{input}%",))
        elif filter =="4":
            cursor.execute("SELECT * from student WHERE course_code LIKE %s", (f"%{input}%",))
        elif filter =="5":
            cursor.execute("SELECT * from student WHERE year LIKE %s", (f"%{input}%",))
        elif filter =="6":
            cursor.execute("SELECT * from student WHERE gender=%s", (f"{input}",))
        for student_data in cursor.fetchall():
            student = Student(id = student_data[0] , firstname = student_data[1], lastname=student_data[2], course_code=student_data[3], year=student_data[4], gender=student_data[5],)
            students.append(student)
        cursor.close()
        return students


    @classmethod
    def get_all(cls,table_name = 'student'):
        cursor = mysql.connection.cursor()
        cursor.execute(f"SELECT * FROM {table_name}")
        student = []
        for student_data in cursor.fetchall():
            courses = Student(id = student_data[0] , firstname = student_data[1], lastname=student_data[2], course_code=student_data[3], year=student_data[4], gender=student_data[5])
            student.append(courses)
        cursor.close()
        return student
    
    @classmethod
    def check_existing_id(cls,id):
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM student WHERE id = %s", (id,))
        student_data = cursor.fetchone()
        cursor.close()
        return student_data is not None
    
    @classmethod
    def get_one(clr, id):
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM student WHERE id = %s", (id,))
        student_data = cursor.fetchone()
        cursor.close

        if student_data:
            return Student(id = student_data[0] , firstname = student_data[1], lastname=student_data[2], course_code=student_data[3], year=student_data[4], gender=student_data[5])
        else:
            return None

    
    
