-- 建数据库判断是否已经存在，存在则删数据库
DROP DATABASE IF EXISTS mysql_homework;

-- 创建数据库
CREATE DATABASE mysql_homework DEFAULT CHARSET="utf8";

-- 切换到数据库mysql_homework
USE mysql_homework;

-- 建表判断是否已经存在表，存在则删表，然后建年级表
DROP TABLE IF EXISTS class_grade;
CREATE TABLE class_grade(
    gid int UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    gname CHAR(10) NOT NULL
);
-- 初始化年纪信息
INSERT INTO class_grade VALUES (1,"一年级"),(2,"二年级"),(3,"三年级");

-- 建表判断是否已经存在表，存在则删表，然后建老师表
DROP TABLE IF EXISTS teacher;
CREATE TABLE teacher(
    tid int UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    tname CHAR(10) NOT NULL
);
-- 初始化老师信息
INSERT INTO teacher VALUES (1,"张三"),(2,"李四"),(3,"王五"),('4', '朱云海老师'), ('5', '李杰老师');

-- 建表判断是否已经存在表，存在则删表，然后建班级表
DROP TABLE IF EXISTS class;
CREATE TABLE class(
    cid int UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    caption CHAR(10) NOT NULL,
    grade_id int UNSIGNED,
    FOREIGN KEY(grade_id) REFERENCES class_grade(gid) ON DELETE CASCADE ON UPDATE CASCADE
);
-- 初始化班级信息
INSERT INTO class VALUES (1,"一年一班",1),(2,"二年一班",2),(3,"三年二班",3), ('4', '二年九班',2);

-- 建表判断是否已经存在表，存在则删表，然后建课程表
DROP TABLE IF EXISTS course;
CREATE TABLE course(
    cid int UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    cname CHAR(10) NOT NULL,
    teacher_id int UNSIGNED,
    FOREIGN KEY(teacher_id) REFERENCES teacher(tid) ON DELETE CASCADE ON UPDATE CASCADE
);
-- 初始化课程信息
INSERT INTO course VALUES (1,"生物",1),(2,"体育",1),(3,"物理",3), ('4', '美术',4);

-- 建表判断是否已经存在表，存在则删表，然后建班级任职表
DROP TABLE IF EXISTS teach2cls;
CREATE TABLE teach2cls(
    tcid int UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    tid int UNSIGNED,
    cid int UNSIGNED,
    FOREIGN KEY(cid) REFERENCES class(cid) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY(tid) REFERENCES teacher(tid) ON DELETE CASCADE ON UPDATE CASCADE
);
-- 初始化班级任职信息
INSERT INTO teach2cls VALUES (1,1,1),(2,1,2),(3,2,1),(4,3,2),(5,4,4);

-- 建表判断是否已经存在表，存在则删表，然后建学生表
DROP TABLE IF EXISTS student;
CREATE TABLE student(
    sid int UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    sname CHAR(10) NOT NULL,
    gender enum("男","女") NOT NULL DEFAULT "男",
    class_id int UNSIGNED,
    FOREIGN KEY(class_id) REFERENCES class(cid) ON DELETE CASCADE ON UPDATE CASCADE
);
-- 初始化学生信息
INSERT INTO student(sid,gender,class_id,sname) VALUES
(1,"女",1,"乔丹"),(2,"女",1,"艾弗森"),(3,"男",2,"科比"), ('4', '男', '1', '张一'), ('5', '女', '1', '张二'), ('6', '男', '1', '张四'),
('7', '女', '2', '铁锤'), ('8', '男', '2', '李三'), ('9', '男', '2', '李一'), ('10', '女', '2', '李二'), ('11', '男', '2', '李四'),
('12', '女', '3', '如花'), ('13', '男', '3', '刘三'), ('14', '男', '3', '刘一'), ('15', '女', '3', '刘二'), ('16', '男', '3', '刘四');

-- 建表判断是否已经存在表，存在则删表，然后建成绩表
DROP TABLE IF EXISTS score;
CREATE TABLE score(
    sid int UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    student_id int UNSIGNED,
    course_id int UNSIGNED,
    score FLOAT(4) NOT NULL DEFAULT 0,
    FOREIGN KEY(student_id) REFERENCES student(sid) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY(course_id) REFERENCES course(cid) ON DELETE CASCADE ON UPDATE CASCADE
);
-- 初始化成绩信息
INSERT INTO score VALUES (1,1,1,60),(2,1,2,59),(3,2,2,99),('5', '1', '4', '66'), ('6', '2', '1', '8'), ('8', '2', '3', '68'), ('9', '2', '4', '99'),
('10', '3', '1', '77'), ('11', '3', '2', '66'), ('12', '3', '3', '87'), ('13', '3', '4', '99'), ('14', '4', '1', '79'), ('15', '4', '2', '11'),
('16', '4', '3', '67'), ('17', '4', '4', '100'), ('18', '5', '1', '79'), ('19', '5', '2', '11'), ('20', '5', '3', '67'), ('21', '5', '4', '100'),
('22', '6', '1', '9'), ('23', '6', '2', '100'), ('24', '6', '3', '67'), ('25', '6', '4', '100'), ('26', '7', '1', '9'), ('27', '7', '2', '100'),
('28', '7', '3', '67'), ('29', '7', '4', '88'), ('30', '8', '1', '9'), ('31', '8', '2', '100'), ('32', '8', '3', '67'), ('33', '8', '4', '88'),
('34', '9', '1', '91'), ('35', '9', '2', '88'), ('36', '9', '3', '67'), ('37', '9', '4', '22'), ('38', '10', '1', '90'), ('39', '10', '2', '77'),
('40', '10', '3', '43'), ('41', '10', '4', '87'), ('42', '11', '1', '90'), ('43', '11', '2', '77'), ('44', '11', '3', '43'), ('45', '11', '4', '87'),
('46', '12', '1', '90'), ('47', '12', '2', '77'), ('48', '12', '3', '43'), ('49', '12', '4', '87'), ('52', '13', '3', '87');