CREATE DATABASE CollegeCourseManageSystem;

use CollegeCourseManageSystem;

CREATE TABLE student(
s_id varchar(10),
name varchar(20),
primary key (s_id)
);

CREATE TABLE class(
name varchar(20)
);

CREATE TABLE major(
name varchar(20),
primary key (name)
);

CREATE TABLE department(
dept_name varchar(20),
primary key (dept_name)
);

CREATE TABLE instructor(
i_id varchar(10),
name varchar(20),
primary key (i_id)
);

CREATE TABLE classroom(
building varchar(10),
room_number varchar(20),
capacity numeric(4,0),
primary key (building,room_number)
);

CREATE TABLE course(
c_id varchar(10),
course_name varchar(50),
credits numeric(2,0) check(credits>0),
type varchar(20),
lesson int,
dept_name varchar(20),
primary key (c_id)
foreign key (dept_name) references department(dept_name) on delete set null
);

CREATE TABLE teaches(
year int,
semester varchar(10),
);