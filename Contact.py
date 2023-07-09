import sqlite3 as sq

connect = sq.connect('students.db')

cursor = connect.cursor()


create_command = '''CREATE TABLE lessons ( 
	    	 lessonsID INTEGER PRIMARY KEY,
		     lesson TEXT NOT NULL,
		     Teacher TEXT NOT NULL)'''


create_command2 = '''CREATE TABLE Students ( 
studentID INTEGER PRIMARY KEY,
first_name TEXT NOT NULL,
last_name TEXT NOT NULL,
age INTEGER NOT NULL,
grade INTEGER NOT NULL,
date TEXT NOT NULL,
lessonsID  INTEGER ,
FOREIGN KEY (lessonsID) REFERENCES lessons (lessonsID))'''


cursor.close()


def add_student():
    first_name = input("الرجاء إدخال اسم الطالب الجديد:")
    last_name = input("الرجاء إدخال كنيه الطالب الجديد:")
    age = input("الرجاء إدخال عمر الطالب الجديد:")
    grade = input('الرجاء ادخال الصف:')
    date = input("ادخل  التاريخ:")
    lessonsID = input("الرجاء ادخال رقم الدرس:")
    connect = sq.connect('students.db')
    cursor = connect.cursor()
    sql = f"""INSERT INTO Students(first_name,last_name,age,grade,date,lessonsID)VALUES ('{first_name}','{last_name}','{age}','{grade}','{date}','{lessonsID}');"""
    cursor.execute(sql)
    connect.commit()
    connect.close()
    print("تم إضافة معلومات الطالب")


def delete_student():
    connect = sq.connect('students.db')
    cursor = connect.cursor()
    while True:
            studentID = input("الرجاء إدخال معرف الطالب الذي تريد حذفه:")
            sql = f"""DELETE FROM Students WHERE studentID='{studentID}'; """
            cursor.execute(sql)
            is_next = input('الرجاء الضغط على q لمتابعه العمليه او الضغط على Enter للخروج')
            print(" تم نجاح العملية ")
            if is_next == 'q':
                break
    connect.commit()
    connect.close()


def update_student():
    show_students()
    connect = sq.connect('students.db')
    cursor = connect.cursor()
    while True:
        studentID = input('* يرجى إدخال معرف الطالب ليتم تعديله:')
        first_name = input('الرجاء إدخال اسم الطالب الجديد:')
        last_name = input("الرجاء إدخال كنيه الطالب الجديد:")
        age = input("الرجاء إدخال عمر الطالب الجديد:")
        grade = input('الرجاء ادخال الصف:')
        date = input("ادخل  التاريخ:")

        sql=f"""UPDATE Students SET first_name='{first_name}',last_name='{last_name}',age='{age}',grade='{grade}',date='{date}' WHERE studentID='{studentID}';"""
        cursor.execute(sql)
        is_next = input('الرجاء الضغط على q لمتابعة التعديل  او الضغط على Enter للخروج ')
        print(" تم التعديل بنجاح ")
        if is_next == 'q':
            break
    connect.commit()
    connect.close()


def show_students():
    connect = sq.connect('students.db')
    cursor = connect.cursor()
    studentID = input("الرجاء إدخال معرف الطالب الذي تريد عرض معلوماته:")
    cursor.execute(f"""SELECT  studentID, first_name,last_name,age, grade, date , lesson
FROM lessons
INNER JOIN Students
on Students.lessonsID = lessons.lessonsID
 WHERE studentID ='{studentID}'; """)
    student_list = cursor.fetchall()
    for index, student in enumerate(student_list):
        print(f'{index+1}\t\t\t\t{student}')
    connect.commit()
    cursor.close()
    connect.close()


def Start():
    while True:
        print("""
                       ********مرحبا بك عزيزي المستخدم  ********         
                                 a لإضافة طالب إضغط على حرف *
                                  d لحذف طالب إضغط على حرف *
                        u لتعديل معلومات طالب إضغط على حرف * 
                          s لعرض معلومات طالب إضغط على حرف *
                  """)
        num = input("الرجاء اختيار العملية التي تريد إجرائها:")
        if not num.isalpha():
            print("يجب أن يكون الإدخال حرفا !!!")
            continue
        num = str(num)
        if num == 'a':
            add_student()
        elif num == 'd':
            delete_student()
        elif num == 'u':
            update_student()
        elif num == 's':
            show_students()
        else:
            print("الإدخال غير صحيح ، يرجى الاختيار مرة أخرى!")
            continue


if __name__ == '__main__':
    Start()