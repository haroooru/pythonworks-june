 create database education_db;

 use education_db;


 create table Course(
 course_id int primary key auto_increment,
 course_name varchar(100) not null unique,
 duration int,
 fee int
 );
 insert into Course(course_name,duration,fee)
 values
 ('Python',3,15000),
 ('Django',2,12000),
 ('Data Analytics',4,20000),
 ('SQL',2,10000);

 create table Student(
 student_id int primary key auto_increment,
 student_name varchar(100) not null,
 email varchar(100) unique,
 age int,
 gender varchar(20),
 mark int,
 course_id int,
 foreign key(course_id) references Course(course_id)
 );


 insert into Course(course_name,duration,fee)
 values
 ('Python',3,15000),
 ('Django',2,12000),
 ('Data Analytics',4,20000),
 ('SQL',2,10000);


 insert into Student(student_name,email,age,gender,mark,course_id)
 values
 ('Anu','anu@gmail.com',21,'Female',92,1),
 ('Rahul','rahul@gmail.com',22,'Male',85,1),
 ('Meera','meera@gmail.com',20,'Female',78,2),
 ('Arjun','arjun@gmail.com',24,'Male',95,2),
 ('Diya','diya@gmail.com',19,'Female',88,3),
 ('Vishnu','vishnu@gmail.com',23,'Male',72,3),
 ('Asha','asha@gmail.com',25,'Female',91,3),
 ('Nikhil','nikhil@gmail.com',18,'Male',67,4),
 ('Sneha','sneha@gmail.com',21,'Female',83,1),
 ('Amal','amal@gmail.com',26,'Male',76,2);


 -- 1

 select *
 from Student
 where mark > 80
 order by mark desc;


 -- 2

 select max(mark),min(mark),avg(mark)
 from Student;


 -- 3

 select *
 from Student
 order by mark desc
 limit 5;


 -- 4

 select student_name,mark
 from Student
 where age between 18 and 25
 order by age;


 -- 5

 select Course.course_name,count(Student.student_id)
 from Course
 join Student
 on Course.course_id=Student.course_id
 group by Course.course_name;


 -- 6

 select Course.course_name,count(Student.student_id)
 from Course
 join Student
 on Course.course_id=Student.course_id
 group by Course.course_name
 having count(Student.student_id)>2;


 -- 7

 select Student.student_name,Student.mark,Course.course_name
 from Student
 inner join Course
 on Student.course_id=Course.course_id;


 -- 8

 select Course.course_name,Student.student_name
 from Course
 left join Student
 on Course.course_id=Student.course_id;


 -- 9

 select *
 from Student
 where mark > (
 select avg(mark)
 from Student
 );


 -- 10

 select Student.student_name,Student.mark,Course.course_name
 from Student
 join Course
 on Student.course_id=Course.course_id
 where Student.mark=(
 select max(mark)
 from Student
 where Student.mark<(
 select max(mark)
 from Student
 )
 );