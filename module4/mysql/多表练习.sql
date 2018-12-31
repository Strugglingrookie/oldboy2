-- 1、查询所有的课程的名称以及对应的任课老师姓名
SELECT
    c.cname,
    t.tname
FROM
    course c
LEFT JOIN teacher t ON c.teacher_id = t.tid;

-- 2、查询学生表中男女生各有多少人
SELECT
    gender,
    count(sid)count
FROM
    student
GROUP BY
    gender;

-- 3、查询物理成绩等于100的学生的姓名
SELECT
    a.sid,
    b.sname
FROM
    score a
LEFT JOIN student b ON a.student_id = b.sid
WHERE
    a.num = 100
AND a.course_id =(
    SELECT
        c.cid
    FROM
        course c
    WHERE
        c.cname = "物理"
);

-- 4、查询平均成绩大于八十分的同学的姓名和平均成绩
SELECT
    a.sname,
    c.avg_score
FROM
    student a
INNER JOIN(
    SELECT
        b.*, AVG(b.num)avg_score
    FROM
        score b
    GROUP BY
        b.student_id
    HAVING
        avg_score > 80
)c ON a.sid = c.student_id;

-- 5、查询所有学生的学号，姓名，选课数，总成绩
SELECT
    a.sid,
    a.sname,
    c.count_course,
    c.sum_score
FROM
    student a
LEFT JOIN(
    SELECT
        b.student_id,
        count(b.course_id)count_course,
        SUM(b.num)sum_score
    FROM
        score b
    GROUP BY
        b.student_id
)c ON a.sid = c.student_id;

-- 6、 查询姓李老师的个数
SELECT
    count(tid)
FROM
    teacher t
WHERE
    t.tname LIKE "李%";

-- 7、 查询没有报李平老师课的学生姓名
SELECT
    a.sname
FROM
    student a
WHERE
    a.sid NOT IN(
        SELECT
            b.student_id
        FROM
            score b
        WHERE
            course_id IN(
                SELECT
                    c.cid
                FROM
                    course c
                WHERE
                    c.teacher_id IN(
                        SELECT
                            d.tid
                        FROM
                            teacher d
                        WHERE
                            d.tname = "李平老师"
                    )
            )
    );

-- 8、 查询物理课程比生物课程高的学生的学号
SELECT
    c.student_id
FROM
    (
        SELECT
            *
        FROM
            score a
        WHERE
            a.course_id =(
                SELECT
                    b.cid
                FROM
                    course b
                WHERE
                    b.cname = "物理"
            )
    )c
INNER JOIN(
    SELECT
        *
    FROM
        score d
    WHERE
        d.course_id =(
            SELECT
                f.cid
            FROM
                course f
            WHERE
                f.cname = "生物"
        )
)g ON c.student_id = g.student_id
AND c.num > g.num;

-- 9、 查询没有同时选修物理课程和体育课程的学生姓名
SELECT
    a.sname
FROM
    student a
WHERE
    a.sid NOT IN(
        SELECT
            d.student_id
        FROM
            (
                SELECT
                    *
                FROM
                    score b
                WHERE
                    b.course_id =(
                        SELECT
                            c.cid
                        FROM
                            course c
                        WHERE
                            c.cname = "物理"
                    )
            )d
        INNER JOIN(
            SELECT
                *
            FROM
                score f
            WHERE
                f.course_id =(
                    SELECT
                        g.cid
                    FROM
                        course g
                    WHERE
                        g.cname = "体育"
                )
        )h ON d.student_id = h.student_id
    );

-- 10、查询挂科超过两门(包括两门)的学生姓名和班级
SELECT
    c.sname,
    c.caption
FROM
    (
        SELECT
            *
        FROM
            student a
        LEFT JOIN class b ON a.class_id = b.cid
    )c
INNER JOIN(
    SELECT
        d.student_id,
        count(d.student_id)count
    FROM
        score d
    WHERE
        d.num < 60
    GROUP BY
        d.student_id
    HAVING
        count >= 2
)e ON c.sid = e.student_id;

-- 11、查询选修了所有课程的学生姓名
SELECT
    s.sname
FROM
    student s
INNER JOIN(
    SELECT
        a.student_id,
        count(a.course_id)count_course
    FROM
        score a
    GROUP BY
        a.student_id
    HAVING
        count_course =(SELECT count(*) FROM course)
)b ON s.sid = b.student_id;

-- 12、查询李平老师教的课程的所有成绩记录
SELECT
    a.*
FROM
    score a
WHERE
    a.course_id IN(
        SELECT
            b.cid
        FROM
            course b
        WHERE
            b.teacher_id =(
                SELECT
                    c.tid
                FROM
                    teacher c
                WHERE
                    c.tname = "李平老师"
            )
    )

-- 13、查询全部学生都选修了的课程号和课程名
    SELECT
        c.cid,
        c.cname
    FROM
        course c
    INNER JOIN(
        SELECT
            a.course_id,
            count(a.student_id)count_student
        FROM
            score a
        GROUP BY
            a.course_id
        HAVING
            count_student =(SELECT count(*) FROM student)
    )b ON c.cid = b.course_id;

-- 14、查询每门课程被选修的次数
SELECT
    c.cid,
    c.cname,
    b.count_student
FROM
    course c
LEFT JOIN(
    SELECT
        a.course_id,
        count(a.student_id)count_student
    FROM
        score a
    GROUP BY
        a.course_id
)b ON c.cid = b.course_id;

-- 15、查询只选修了一门课程的学生姓名和学号
SELECT
    s.sname
FROM
    student s
INNER JOIN(
    SELECT
        a.student_id,
        count(a.course_id)count_course
    FROM
        score a
    GROUP BY
        a.student_id
    HAVING
        count_course = 1
)b ON s.sid = b.student_id;

-- 16、查询所有学生考出的成绩并按从高到低排序（成绩去重）
SELECT DISTINCT
    (num)
FROM
    score a
ORDER BY
    a.num DESC

-- 17、查询平均成绩大于85的学生姓名和平均成绩
    SELECT
        a.sname
    FROM
        student a
    INNER JOIN(
        SELECT
            b.student_id,
            avg(b.num)avg_num
        FROM
            score b
        GROUP BY
            b.student_id
        HAVING
            avg_num > 85
    )c ON a.sid = c.student_id;

-- 18、查询生物成绩不及格的学生姓名和对应生物分数
SELECT
    a.sname,
    c.num
FROM
    student a
INNER JOIN(
    SELECT
        b.student_id,
        b.num
    FROM
        score b
    WHERE
        b.course_id =(
            SELECT
                cid
            FROM
                course
            WHERE
                cname = "生物"
        )
    AND b.num < 60
)c ON a.sid = c.student_id;

-- 19、查询在所有选修了李平老师课程的学生中，这些课程(李平老师的课程，不是所有课程)平均成绩最高的学生姓名
SELECT
    sname
FROM
    student
WHERE
    sid =(
        SELECT
            a.student_id
        FROM
            score a
        WHERE
            a.course_id IN(
                SELECT
                    b.cid
                FROM
                    course b
                WHERE
                    b.teacher_id =(
                        SELECT
                            c.tid
                        FROM
                            teacher c
                        WHERE
                            c.tname = "李平老师"
                    )
            )
        GROUP BY
            a.student_id
        ORDER BY
            avg(num)DESC
        LIMIT 1
    )

-- 20、查询每门课程成绩最好的前两名学生姓名
    SELECT
        e.sname,
        f.course_id,
        f.num
    FROM
        student e
    INNER JOIN(
        SELECT
            c.*
        FROM
            score c
        INNER JOIN(
            SELECT
                *
            FROM
                (
                    SELECT
                        course_id,
                        MAX(num)num
                    FROM
                        score
                    GROUP BY
                        course_id
                    ORDER BY
                        course_id,
                        num DESC
                )a
            UNION ALL
                (
                    SELECT
                        a.course_id,
                        MAX(a.num)num
                    FROM
                        score a
                    INNER JOIN(
                        SELECT
                            course_id,
                            MAX(num)num
                        FROM
                            score
                        GROUP BY
                            course_id
                        ORDER BY
                            course_id,
                            num DESC
                    )b ON a.course_id = b.course_id
                    WHERE
                        a.num < b.num
                    GROUP BY
                        a.course_id
                )
        )d ON c.course_id = d.course_id
        WHERE
            c.num = d.num
        ORDER BY
            c.course_id,
            c.num DESC
    )f ON e.sid = f.student_id
    ORDER BY
        f.course_id,
        f.num DESC

-- 21、查询不同课程但成绩相同的学号，课程号，成绩
        SELECT
            student_id,
            course_id,
            num
        FROM
            score
        WHERE
            num IN(
                SELECT
                    a.num
                FROM
                    (
                        SELECT
                            *
                        FROM
                            score
                        GROUP BY
                            course_id,
                            num
                    )a
                GROUP BY
                    a.num
                HAVING
                    count(a.num)> 1
            )
        ORDER BY
            num;

-- 22、查询没学过“叶平”老师课程的学生姓名以及选修的课程名称；
SELECT
    c.sname,
    GROUP_CONCAT(d.cname)
FROM
    (
        SELECT
            a.*, b.course_id
        FROM
            (
                SELECT
                    *
                FROM
                    student
                WHERE
                    sid NOT IN(
                        SELECT DISTINCT
                            (student_id)
                        FROM
                            score
                        WHERE
                            course_id IN(
                                SELECT
                                    cid
                                FROM
                                    course
                                WHERE
                                    teacher_id =(
                                        SELECT
                                            tid
                                        FROM
                                            teacher
                                        WHERE
                                            tname = "李平老师"
                                    )
                            )
                    )
            )a
        INNER JOIN score b ON a.sid = b.student_id
    )c
INNER JOIN course d ON c.course_id = d.cid
GROUP BY
    c.sname

-- 23、查询所有选修了学号为1的同学选修过的一门或者多门课程的同学学号和姓名；
    SELECT
        a.sid,
        a.sname
    FROM
        student a
    INNER JOIN(
        SELECT
            student_id
        FROM
            score
        WHERE
            student_id != 1
        AND course_id IN(
            SELECT
                course_id
            FROM
                score
            WHERE
                student_id = 1
        )
        GROUP BY
            student_id
    )b ON a.sid = b.student_id

-- 24、任课最多的老师中学生单科成绩最高的学生姓名
    SELECT
        sname
    FROM
        student
    WHERE
        sid =(
            SELECT
                student_id
            FROM
                score
            WHERE
                course_id IN(
                    SELECT
                        cid
                    FROM
                        course
                    WHERE
                        teacher_id =(
                            SELECT
                                teacher_id
                            FROM
                                course
                            GROUP BY
                                teacher_id
                            ORDER BY
                                count(teacher_id)DESC
                            LIMIT 1
                        )
                )
            ORDER BY
                num DESC
            LIMIT 1
        )