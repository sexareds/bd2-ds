import preparation.clstbl as ct
import querying.query1 as q1

def get_students_EIU():
    return ct.get_table(q1.get_students_EIU)

def get_students_gender():
    return ct.get_table(q1.get_students_gender)

def get_students_semester():
    return ct.get_table(q1.get_students_semester)

def get_students_semester_2():
    return ct.get_table(q1.get_students_semester_2)

def get_students_career():
    return ct.get_table(q1.get_students_career)

def get_students_career_2():
    return ct.get_table(q1.get_students_career_2)