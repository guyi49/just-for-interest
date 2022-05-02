
'''表： Employee

+--------------+---------+
| 列名          | 类型    |
+--------------+---------+
| id           | int     |
| name         | varchar |
| salary       | int     |
| departmentId | int     |
+--------------+---------+
id是此表的主键列。
departmentId是Department表中ID的外键。
此表的每一行都表示员工的ID、姓名和工资。它还包含他们所在部门的ID。
 

表： Department

+-------------+---------+
| 列名         | 类型    |
+-------------+---------+
| id          | int     |
| name        | varchar |
+-------------+---------+
id是此表的主键列。
此表的每一行都表示一个部门的ID及其名称。
 


按 任意顺序 返回结果表。
查询结果格式如下例所示。

 

示例 1:

输入：
Employee 表:
+----+-------+--------+--------------+
| id | name  | salary | departmentId |
+----+-------+--------+--------------+
| 1  | Joe   | 70000  | 1            |
| 2  | Jim   | 90000  | 1            |
| 3  | Henry | 80000  | 2            |
| 4  | Sam   | 60000  | 2            |
| 5  | Max   | 90000  | 1            |
+----+-------+--------+--------------+
Department 表:
+----+-------+
| id | name  |
+----+-------+
| 1  | IT    |
| 2  | Sales |
+----+-------+
输出：
+------------+----------+--------+
| Department | Employee | Salary |
+------------+----------+--------+
| IT         | Jim      | 90000  |
| Sales      | Henry    | 80000  |
| IT         | Max      | 90000  |
+------------+----------+--------+

解释：Max 和 Jim 在 IT 部门的工资都是最高的，Henry 在销售部的工资最高。
编写SQL查询以查找每个部门中薪资最高的员工。
'''
select  Department,ee.employee_name, ee.salary
from (select e.id as employee_id, e.name, max(salary) as max_salary, d.name as Department, d.id
      from Employee e
               left join Department d on e.departmentId = d.id
      group by d.id) c
         right join Employee ee on c.id = ee.departmentId
where ee.salary = max_salary;


select ee.employee_id, ee.employee_name, ee.job_grade_id, department_name
from (select e.employee_id, e.employee_name, min(job_grade_id) as min_job_grade_id, d.department_name, d.department_id
      from hrm.hr_employee e
               left join hrm.hr_department d on e.department_id = d.department_id
      group by d.department_id) c
         right join hrm.hr_employee ee on c.department_id = ee.department_id
where ee.job_grade_id = min_job_grade_id;