-- 选择数据库
USE mysql_homework;

-- 1、自行创建测试数据；
-- 详见  作业初始化数据信息.sql
-- 2、查询学生总人数；
SELECT
    count(sid) 学生总人数
FROM
    student;

-- 3、查询“生物”课程和“物理”课程成绩都及格的学生id和姓名；
SELECT
    sid,
    sname
FROM
    student
WHERE
    sid IN (
        SELECT
            student_id
        FROM
            score
        WHERE
            score >= 60
        AND course_id IN (
            SELECT
                cid
            FROM
                course
            WHERE
                cname IN ("生物", "物理")
        )
        GROUP BY
            student_id
        HAVING
            count(student_id) = 2
    );

-- 4、查询每个年级的班级数，取出班级数最多的前三个年级；
SELECT
    *
FROM
    class_grade a
LEFT JOIN (
    SELECT
        grade_id,
        count(grade_id) count_class
    FROM
        class
    GROUP BY
        grade_id
) b ON a.gid = b.count_class
ORDER BY
    b.count_class DESC
LIMIT 3;

-- 5、查询平均成绩最高和最低的学生的id和姓名以及平均成绩；
-- 解题思路：首先查到最大和最小平均值，然后找到平均值等于最大最小的学生id，然后再根据id查学生姓名。因为最高和最低平均值可能存在多个人，所以要这样查。
SELECT
    d.sname,
    f.avg_score
FROM
    student d
INNER JOIN (
    SELECT
        b.*
    FROM
        (
            SELECT
                student_id,
                avg(score) avg_score
            FROM
                score
            GROUP BY
                student_id
        ) b
    INNER JOIN (
        SELECT
            MAX(a.avg_score) max_avg,
            MIN(a.avg_score) min_avg
        FROM
            (
                SELECT
                    student_id,
                    avg(score) avg_score
                FROM
                    score
                GROUP BY
                    student_id
            ) a
    ) c ON 1 = 1
    WHERE
        b.avg_score = c.max_avg
    OR b.avg_score = c.min_avg
) f ON d.sid = f.student_id;

-- 6、查询每个年级的学生人数；
SELECT
    a.gname,
    count(a.gname) count_stus
FROM
    (
        class_grade a
        INNER JOIN class b ON a.gid = b.grade_id
    )
INNER JOIN student c ON b.cid = c.class_id
GROUP BY
    a.gname;

-- 7、查询每位学生的学号，姓名，选课数，平均成绩；
SELECT
    a.sid,
    a.sname,
    b.count_course,
    b.avg_score
FROM
    student a
INNER JOIN (
    SELECT
        student_id,
        count(course_id) count_course,
        avg(score) avg_score
    FROM
        score
    GROUP BY
        student_id
) b ON a.sid = b.student_id;

-- 8、查询学生编号为“2”的学生的姓名、该学生成绩最高的课程名、成绩最低的课程名及分数；
-- 解题思路：先找到学生编号为“2”的最高成绩和最低成绩，因为最高或最多可能存在多个科目，所以要考虑这种情况。
SELECT
    c.sname,
    f.cname,
    d.score
FROM
    (
        student c
        INNER JOIN (
            SELECT
                a.*
            FROM
                score a
            INNER JOIN (
                SELECT
                    student_id,
                    max(score) score
                FROM
                    score
                WHERE
                    student_id = 2
                UNION
                    SELECT
                        student_id,
                        min(score) score
                    FROM
                        score
                    WHERE
                        student_id = 2
            ) b ON a.student_id = b.student_id
            AND a.score = b.score
        ) d ON c.sid = d.student_id
    )
INNER JOIN course f ON d.course_id = f.cid;

-- 9、查询姓“李”的老师的个数和所带班级数；
-- 解题思路：关联5张表查询，将姓“李”的老师的笛卡尔积查出来，然后进行统计。
SELECT
    count(DISTINCT(tname)),
    count(DISTINCT(course_id))
FROM
    (
        (
            (
                class a
                INNER JOIN student b ON a.cid = b.class_id
            )
            INNER JOIN score c ON b.sid = c.student_id
        )
        INNER JOIN course d ON c.course_id = d.cid
    )
INNER JOIN (
    SELECT
        *
    FROM
        teacher
    WHERE
        tname LIKE "张%"
) f ON d.teacher_id = f.tid;

-- 10、查询班级数小于5的年级id和年级名；
SELECT
    a.gid,
    a.gname,
    count(gid) count_class
FROM
    class_grade a
INNER JOIN class b ON a.gid = b.grade_id
GROUP BY
    a.gid
HAVING
    count(gid) < 5;

-- 11、查询班级信息，包括班级id、班级名称、年级、年级级别(12为低年级，34为中年级，56为高年级)，示例结果如下
-- 班级id    班级名称    年级      年级级别
-- 1        一年一班    一年级    低
SELECT
    c.cid,
    c.caption,
    c.grade_id,
    CASE
WHEN c.gid IN (1, 2) THEN
    "低年级"
WHEN c.gid IN (3, 4) THEN
    "中年级"
WHEN c.gid IN (5, 6) THEN
    "高年级"
ELSE
    "无"
END "年级级别"
FROM
    (
        SELECT
            *
        FROM
            class a
        INNER JOIN class_grade b ON a.grade_id = b.gid
    ) c;

-- 12、查询学过“张三”老师2门课以上的同学的学号、姓名；
SELECT
    a.sid,
    a.sname
FROM
    student a
INNER JOIN (
    SELECT
        student_id,
        count(course_id)
    FROM
        score
    WHERE
        course_id IN (
            SELECT
                cid
            FROM
                course
            WHERE
                teacher_id = (
                    SELECT
                        tid
                    FROM
                        teacher
                    WHERE
                        tname = "张三"
                )
        )
    GROUP BY
        student_id
    HAVING
        count(course_id) >= 2
) b ON a.sid = b.student_id;

-- 13、查询教授课程超过2门的老师的id和姓名；
SELECT
    a.tid,
    a.tname
FROM
    teacher a
INNER JOIN (
    SELECT
        teacher_id,
        count(teacher_id) count_course
    FROM
        course
    GROUP BY
        teacher_id
) b ON a.tid = b.teacher_id
WHERE
    b.count_course >= 2;

-- 14、查询学过编号“1”课程和编号“2”课程的同学的学号、姓名；
SELECT
    a.sid,
    a.sname
FROM
    student a
INNER JOIN (
    SELECT
        *
    FROM
        score
    WHERE
        course_id IN (1, 2)
    GROUP BY
        student_id
    HAVING
        count(student_id) = 2
) b ON a.sid = b.student_id;

-- 15、查询没有带过高年级的老师id和姓名；
SELECT
    *
FROM
    teacher
WHERE
    tid NOT IN (
        SELECT
            a.tid
        FROM
            (
                (
                    teacher a
                    INNER JOIN teach2cls b ON a.tid = b.tid
                )
                INNER JOIN class c ON b.cid = c.cid
            )
        INNER JOIN class_grade d ON c.grade_id = d.gid
        WHERE
            d.gid IN (5, 6)
    );

-- 16、查询学过“张三”老师所教的所有课的同学的学号、姓名；
SELECT
    a.sid,
    a.sname
FROM
    (
        student a
        INNER JOIN score b ON a.sid = b.student_id
    )
INNER JOIN (
    SELECT
        *
    FROM
        course
    WHERE
        teacher_id = (
            SELECT
                tid
            FROM
                teacher
            WHERE
                tname = "张三"
        )
) c ON b.course_id = c.cid
GROUP BY
    a.sid
HAVING
    count(a.sid) = (
        SELECT
            count(cid)
        FROM
            course
        WHERE
            teacher_id = (
                SELECT
                    tid
                FROM
                    teacher
                WHERE
                    tname = "张三"
            )
    );

-- 17、查询带过超过2个班级的老师的id和姓名；
SELECT
    a.*
FROM
    teacher a
INNER JOIN (
    SELECT
        tid
    FROM
        teach2cls
    GROUP BY
        tid
    HAVING
        count(cid) >= 2
) b ON a.tid = b.tid;

-- 18、查询课程编号“2”的成绩比课程编号“1”课程低的所有同学的学号、姓名；
SELECT
    c.sid,
    c.sname
FROM
    student c
INNER JOIN (
    SELECT
        a.*
    FROM
        score a
    INNER JOIN (
        SELECT
            *
        FROM
            score
        WHERE
            course_id = 2
    ) b ON a.student_id = b.student_id
    WHERE
        a.course_id = 1
    AND b.score < a.score
) d ON c.sid = d.student_id;

-- 19、查询所带班级数最多的老师id和姓名；
SELECT
    a.*
FROM
    teacher a
INNER JOIN (
    SELECT
        tid
    FROM
        teach2cls
    GROUP BY
        tid
    HAVING
        count(cid) = (
            SELECT
                max(a.count_course)
            FROM
                (
                    SELECT
                        tid,
                        count(cid) count_course
                    FROM
                        teach2cls
                    GROUP BY
                        tid
                ) a
        )
) b ON a.tid = b.tid;

-- 20、查询有课程成绩小于60分的同学的学号、姓名；
SELECT
    a.sid,
    a.sname
FROM
    student a
INNER JOIN (
    SELECT
        student_id
    FROM
        score
    WHERE
        score < 60
    GROUP BY
        student_id
) b ON a.sid = b.student_id;

-- 21、查询没有学全所有课的同学的学号、姓名；
SELECT
    a.sid,
    a.sname
FROM
    student a
INNER JOIN (
    SELECT
        student_id,
        count(course_id) count_course
    FROM
        score
    GROUP BY
        student_id
    HAVING
        count_course < (SELECT count(cid) FROM course)
) b ON a.sid = b.student_id;

-- 22、查询至少有一门课与学号为“1”的同学所学相同的同学的学号和姓名；
SELECT
    c.sid,
    c.sname
FROM
    student c
INNER JOIN (
    SELECT DISTINCT
        (a.student_id)
    FROM
        score a
    INNER JOIN (
        SELECT
            course_id
        FROM
            score
        WHERE
            student_id = 1
    ) b ON a.course_id = b.course_id
) d ON c.sid = d.student_id;

-- 23、查询至少学过学号为“1”同学所选课程中任意一门课的其他同学学号和姓名；
SELECT
    c.sid,
    c.sname
FROM
    student c
INNER JOIN (
    SELECT DISTINCT
        (a.student_id)
    FROM
        score a
    INNER JOIN (
        SELECT
            course_id
        FROM
            score
        WHERE
            student_id = 1
    ) b ON a.course_id = b.course_id
    WHERE
        a.student_id != 1
) d ON c.sid = d.student_id;

-- 24、查询和“2”号同学学习的课程完全相同的其他同学的学号和姓名；
SELECT
    c.sid,
    c.sname
FROM
    student c
INNER JOIN (
    SELECT
        a.student_id,
        count(a.student_id) count_course
    FROM
        score a
    INNER JOIN (
        SELECT
            course_id
        FROM
            score
        WHERE
            student_id = 2
    ) b ON a.course_id = b.course_id
    WHERE
        a.student_id != 2
    GROUP BY
        a.student_id
    HAVING
        count_course = (
            SELECT
                count(course_id)
            FROM
                score
            WHERE
                student_id = 2
        )
) d ON c.sid = d.student_id;

-- 25、删除学习“张三”老师课的score表记录；
DELETE
FROM
    score
WHERE
    course_id IN (
        SELECT
            cid
        FROM
            course
        WHERE
            teacher_id = (
                SELECT
                    tid
                FROM
                    teacher
                WHERE
                    tname = "张三"
            )
    );

-- 26、向score表中插入一些记录，这些记录要求符合以下条件：①没有上过编号“2”课程的同学学号；②插入“2”号课程的平均成绩；
INSERT INTO score (student_id, course_id, score) SELECT
    *
FROM
    (
        (
            SELECT
                sid
            FROM
                student
            WHERE
                sid NOT IN (
                    SELECT
                        student_id
                    FROM
                        score
                    WHERE
                        course_id = 2
                )
        ) a
        LEFT JOIN (
            SELECT
                cid
            FROM
                course
            WHERE
                cid = 2
        ) b ON 1 = 1
    )
INNER JOIN (
    SELECT
        avg(score)
    FROM
        score
    WHERE
        course_id = 2
) c ON 1 = 1;

-- 27、按平均成绩从低到高显示所有学生的“语文”、“数学”、“英语”三门的课程成绩，按如下形式显示： 学生ID,语文,数学,英语,有效课程数,有效平均分；
SELECT
    a.student_id 学生ID,
    d.score 语文,
    c.score 数学,
    d.score 英语,
    a.count_course 有效课程数,
    a.avg_score 有效平均分
FROM
    (
        (
            (
                (
                    SELECT
                        student_id,
                        count(score) count_course,
                        avg(score) avg_score
                    FROM
                        score
                    GROUP BY
                        student_id
                    ORDER BY
                        avg_score DESC
                ) a
                LEFT JOIN (
                    SELECT
                        student_id,
                        score
                    FROM
                        score
                    WHERE
                        course_id = (
                            SELECT
                                cid
                            FROM
                                course
                            WHERE
                                cname = "生物"
                        )
                ) b ON a.student_id = b.student_id
            )
            LEFT JOIN (
                SELECT
                    student_id,
                    score
                FROM
                    score
                WHERE
                    course_id = (
                        SELECT
                            cid
                        FROM
                            course
                        WHERE
                            cname = "体育"
                    )
            ) c ON b.student_id = c.student_id
        )
    )
LEFT JOIN (
    SELECT
        student_id,
        score
    FROM
        score
    WHERE
        course_id = (
            SELECT
                cid
            FROM
                course
            WHERE
                cname = "物理"
        )
) d ON c.student_id = d.student_id
ORDER BY
    a.avg_score DESC;

-- 28、查询各科成绩最高和最低的分：以如下形式显示：课程ID，最高分，最低分；
SELECT
    a.course_id,
    a.max_score,
    b.min_score
FROM
    (
        SELECT
            course_id,
            MAX(score) max_score
        FROM
            score
        GROUP BY
            course_id
    ) a
INNER JOIN (
    SELECT
        course_id,
        min(score) min_score
    FROM
        score
    GROUP BY
        course_id
) b ON a.course_id = b.course_id;

-- 29、按各科平均成绩从低到高和及格率的百分数从高到低顺序
SELECT
    a.sid,
    a.course_id,
    a.avg_score,
    (b.count_pass / a.count_all) * 100 pass_percent
FROM
    (
        SELECT
            sid,
            course_id,
            avg(score) avg_score,
            count(student_id) count_all
        FROM
            score
        GROUP BY
            course_id
    ) a
INNER JOIN (
    SELECT
        course_id,
        count(student_id) count_pass
    FROM
        score
    WHERE
        score > 60
    GROUP BY
        course_id
) b ON a.course_id = b.course_id
ORDER BY
    a.avg_score,
    pass_percent DESC;

-- 30、课程平均分从高到低显示（显示任课老师）；
SELECT
    b.cname,
    a.tname,
    c.avg_score
FROM
    (
        teacher a
        INNER JOIN course b ON a.tid = b.teacher_id
    )
INNER JOIN (
    SELECT
        course_id,
        avg(score) avg_score
    FROM
        score
    GROUP BY
        course_id
) c ON b.cid = c.course_id
ORDER BY
    c.avg_score DESC;

-- 31、查询各科成绩前三名的记录(不考虑成绩并列情况)
SELECT
    *
FROM
    (
        SELECT
            *
        FROM
            score
        WHERE
            course_id = 1
        ORDER BY
            score DESC
        LIMIT 3
    ) a
UNION ALL
    SELECT
        *
    FROM
        (
            SELECT
                *
            FROM
                score
            WHERE
                course_id = 2
            ORDER BY
                score DESC
            LIMIT 3
        ) b
    UNION ALL
        SELECT
            *
        FROM
            (
                SELECT
                    *
                FROM
                    score
                WHERE
                    course_id = 3
                ORDER BY
                    score DESC
                LIMIT 3
            ) c
        UNION ALL
            SELECT
                *
            FROM
                (
                    SELECT
                        *
                    FROM
                        score
                    WHERE
                        course_id = 4
                    ORDER BY
                        score DESC
                    LIMIT 3
                ) d;

-- 32、查询每门课程被选修的学生数；
SELECT
    course_id,
    count(student_id) count_stus
FROM
    score
GROUP BY
    course_id;

-- 33、查询选修了2门以上课程的全部学生的学号和姓名；
SELECT
    a.sid,
    a.sname
FROM
    student a
INNER JOIN (
    SELECT
        *
    FROM
        score
    GROUP BY
        student_id
    HAVING
        count(course_id) >= 2
) b ON a.sid = b.student_id;

-- 34、查询男生、女生的人数，按倒序排列；
SELECT
    gender,
    count(sid) counts
FROM
    student
GROUP BY
    gender
ORDER BY
    counts DESC;

-- 35、查询姓“张”的学生名单；
SELECT
    *
FROM
    student
WHERE
    sname LIKE "张%";

-- 36、查询同名同姓学生名单，并统计同名人数；
SELECT
    sname,
    count(sid) counts
FROM
    student
GROUP BY
    sname
HAVING
    counts >= 2;

-- 37、查询每门课程的平均成绩，结果按平均成绩升序排列，平均成绩相同时，按课程号降序排列；
SELECT
    course_id,
    avg(score) avg_score
FROM
    score
GROUP BY
    course_id
ORDER BY
    avg_score,
    course_id DESC;

-- 38、查询课程名称为“数学”，且分数低于60的学生姓名和分数；
SELECT
    a.sid,
    a.sname
FROM
    student a
INNER JOIN (
    SELECT
        *
    FROM
        score
    WHERE
        score < 60
    AND course_id IN (
        SELECT
            cid
        FROM
            course
        WHERE
            cname = "数学"
    )
) b ON a.sid = b.student_id;

-- 39、查询课程编号为“3”且课程成绩在80分以上的学生的学号和姓名；
SELECT
    a.sid,
    a.sname
FROM
    student a
INNER JOIN (
    SELECT DISTINCT
        (student_id)
    FROM
        score
    WHERE
        score > 80
    AND course_id = 3
) b ON a.sid = b.student_id;

-- 40、求选修了课程的学生人数
SELECT
    count(*)
FROM
    (
        SELECT DISTINCT
            (student_id)
        FROM
            score
    ) a;

-- 41、查询选修“王五”老师所授课程的学生中，成绩最高和最低的学生姓名及其成绩；
SELECT
    c.sid,
    c.sname,
    d.score
FROM
    student c
INNER JOIN (
    SELECT
        *
    FROM
        score a
    INNER JOIN (
        SELECT
            MAX(score) max_score,
            MIN(score) min_score
        FROM
            score
        WHERE
            course_id IN (
                SELECT
                    cid
                FROM
                    course
                WHERE
                    teacher_id = (
                        SELECT
                            tid
                        FROM
                            teacher
                        WHERE
                            tname = "王五"
                    )
            )
    ) b ON a.score = b.max_score
    OR a.score = b.min_score
    WHERE
        course_id IN (
            SELECT
                cid
            FROM
                course
            WHERE
                teacher_id = (
                    SELECT
                        tid
                    FROM
                        teacher
                    WHERE
                        tname = "王五"
                )
        )
) d ON c.sid = d.student_id
ORDER BY
    d.score DESC;

-- 42、查询各个课程及相应的选修人数；
SELECT
    course_id,
    count(course_id)
FROM
    score
GROUP BY
    course_id;

-- 43、查询不同课程但成绩相同的学生的学号、课程号、学生成绩；
SELECT
    student_id,
    course_id,
    score
FROM
    score
WHERE
    score IN (
        SELECT
            a.score
        FROM
            (
                SELECT
                    *
                FROM
                    score
                GROUP BY
                    course_id,
                    score
            ) a
        GROUP BY
            a.score
        HAVING
            count(a.score) > 1
    )
ORDER BY
    score;

-- 44、查询每门课程成绩最好的前两名学生id和姓名；
SELECT
    e.sname,
    f.course_id,
    f.score
FROM
    student e
INNER JOIN (
    SELECT
        c.*
    FROM
        score c
    INNER JOIN (
        SELECT
            *
        FROM
            (
                SELECT
                    course_id,
                    MAX(score) score
                FROM
                    score
                GROUP BY
                    course_id
                ORDER BY
                    course_id,
                    score DESC
            ) a
        UNION ALL
            (
                SELECT
                    a.course_id,
                    MAX(a.score) score
                FROM
                    score a
                INNER JOIN (
                    SELECT
                        course_id,
                        MAX(score) score
                    FROM
                        score
                    GROUP BY
                        course_id
                    ORDER BY
                        course_id,
                        score DESC
                ) b ON a.course_id = b.course_id
                WHERE
                    a.score < b.score
                GROUP BY
                    a.course_id
            )
    ) d ON c.course_id = d.course_id
    WHERE
        c.score = d.score
    ORDER BY
        c.course_id,
        c.score DESC
) f ON e.sid = f.student_id
ORDER BY
    f.course_id,
    f.score DESC;

-- 45、检索至少选修两门课程的学生学号；
SELECT
    student_id
FROM
    score
GROUP BY
    student_id
HAVING
    count(course_id) >= 2;

-- 46、查询没有学生选修的课程的课程号和课程名；
SELECT
    cid,
    cname
FROM
    course
WHERE
    cid NOT IN (SELECT course_id FROM score);

-- 47、查询没带过任何班级的老师id和姓名；
SELECT
    *
FROM
    teacher
WHERE
    tid NOT IN (SELECT tid FROM teach2cls);

-- 48、查询有两门以上课程超过80分的学生id及其平均成绩；
SELECT
    a.*
FROM
    (
        SELECT
            student_id,
            avg(score)
        FROM
            score
        GROUP BY
            student_id
    ) a
INNER JOIN (
    SELECT
        student_id
    FROM
        score
    WHERE
        score > 80
    GROUP BY
        student_id
    HAVING
        count(course_id) >= 2
) b ON a.student_id = b.student_id;

-- 49、检索“3”课程分数小于60，按分数降序排列的同学学号；
SELECT
    student_id
FROM
    score
WHERE
    course_id = 3
AND score < 60
ORDER BY
    score DESC;

-- 50、删除编号为“2”的同学的“1”课程的成绩；
DELETE
FROM
    score
WHERE
    course_id = 1
AND student_id = 2;

-- 51、查询同时选修了物理课和生物课的学生id和姓名；
SELECT
    a.sid,
    a.sname
FROM
    student a
INNER JOIN (
    SELECT
        *
    FROM
        score
    WHERE
        course_id IN (
            SELECT
                cid
            FROM
                course
            WHERE
                cname IN ("物理", "生物")
        )
    GROUP BY
        student_id
    HAVING
        count(course_id) = 2
) b ON a.sid = b.student_id;