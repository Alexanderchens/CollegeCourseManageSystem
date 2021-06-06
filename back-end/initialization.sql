CREATE DATABASE CollegeCourseManageSystem;

use CollegeCourseManageSystem;

CREATE TABLE student(
s_id varchar(20),
name varchar(20),
password varchar(50),
primary key (s_id)
);
alter table student add class_name varchar(20);
alter table student add constraint student_ibfk_1 foreign key (class_name) references class(name);

CREATE TABLE class(
name varchar(20),
primary key (name)
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
i_id varchar(20),
name varchar(20),
password varchar(50),
primary key (i_id)
);

CREATE TABLE classroom(
building varchar(10),
room_number varchar(20),
capacity numeric(4,0),
primary key (building,room_number)
);

CREATE TABLE course(
c_id varchar(20),
course_name varchar(50),
credits numeric(2,0) check(credits>0),
type varchar(20),
hour int,
dept_name varchar(20),
started bit,
primary key (c_id),
foreign key (dept_name) references department(dept_name) on delete set null
);


create table teaches
	(i_id varchar(5),
	 c_id varchar(8),
	 semester varchar(6),
	 year numeric(4,0),
	 primary key (i_id, c_id, semester, year),
	 foreign key (c_id) references course(c_id),
	 foreign key (i_id) references instructor (i_id)
		on delete cascade
	);
alter table teaches add class_name varchar(20);
alter table teaches add constraint teaches_ibfk_3 foreign key (class_name) references class(name);

CREATE TABLE time_slot(
weeknumber numeric(2,0),
weekday numeric(1,0),
time_slot_number numeric(2,0),
primary key (weeknumber, weekday, time_slot_number)
);

CREATE TABLE system_manager(
m_id varchar(20),
name varchar(20),
password varchar(50),
primary key (m_id)
);

# 未执行
CREATE TABLE student_pick(
s_id varchar(20),
c_id varchar(20),
year numeric(4,0),
semester varchar(6),
foreign key (s_id) references student(s_id),
foreign key (c_id) references course(c_id),
primary key (s_id,c_id,year,semester)
);


# 任课老师
CREATE TABLE teacher_rel(
i_id varchar(20),
c_id varchar(20),
year numeric(4,0),
semester varchar(6),
foreign key (i_id) references instructor(i_id),
foreign key (c_id) references course(c_id),
primary key (i_id,c_id,year,semester)
);

CREATE TABLE lesson(
c_id varchar(20),
year numeric(4,0),
semester varchar(6),
weeknumber numeric(2,0),
weekday numeric(1,0),
time_slot_number numeric(2,0),
building varchar(10),
room_number varchar(20),
foreign key (c_id) references course(c_id),
foreign key (weeknumber, weekday, time_slot_number) references time_slot(weeknumber, weekday, time_slot_number),
foreign key (building, room_number) references classroom(building, room_number),
primary key (c_id, year, semester, weeknumber, weekday, time_slot_number, building, room_number)
);