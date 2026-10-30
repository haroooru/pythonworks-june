
#1.#Given a dictionary
student_grades={'Alice':98,'Bob':85,'Charlie':74,'Mike':70}



#print the grade of Charlie

print(student_grades['Charlie'])

#update the grade of Bob to 90
student_grades['Bob'] = 90
print(student_grades)

#Add new item 'Sam:75' to the dictionary
student_grades['Sam'] = 75
print(student_grades)

# #print the total number of students
print(len(student_grades))


#print all student names in the given dictionary
print(student_grades.keys())

#2.Given a dictionary

student_marks={'Arun':{'maths':30,'science':35,'english':40,'history':33},
                'Amal':{'maths':40,'science':45,'english':48,'history':43},
                'Anu':{'maths':45,'science':46,'english':47,'history':49}}

#print the mark of Amal in the subject History
print(student_marks['Amal']['history'])

#Update the mark of Arun in maths to 35
student_marks['Arun']['maths']=35
print(student_marks)

#print the marks of all students (in all subjects)
print(student_marks.values())