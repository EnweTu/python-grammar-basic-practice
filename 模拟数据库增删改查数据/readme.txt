staff_id          name            age            phone            dept        enroll_date
   1             AlexLi            25         13651054608          IT          2013-04-01
   2            JackWang           30         13304320533          HR          2015-05-03
   3            RainLiu            25         13832356822        Sales         2016-04-22
   4            MackCao            40         13561587524          HR          2009-03-01
   5           RachelChen          23         13351024606          IT          2013-03-16
   6            EricLiu            19         18531054602      Marketing       2012-12-01
   7           ChaoZhang           21         13235324334    Administration    2011-08-08
   8           KevinChen           22         13151054603        Sales         2013-04-01
   9            ShitWen            20         13351024602          IT          2017-07-03
   10          ShanshanDu          26         13698424612      Operation       2017-07-02


对形如上的表将其按如下形式存储在文件中

staff_id,name,age,phone,dept,enroll_date
1,AlexLi,25,13651054608,IT,2013-04-01
2,JackWang,30,13304320533,HR,2015-05-03
3,RainLiu,25,13832356822,Sales,2016-04-22
4,MackCao,40,13561587524,HR,2009-03-01
5,RachelChen,23,13351024606,IT,2013-03-16
6,EricLiu,19,18531054602,Marketing,2012-12-01
7,ChaoZhang,21,13235324334,Administration,2011-08-08
8,KevinChen,22,13151054603,Sales,2013-04-01
9,ShitWen,20,13351024602,IT,2017-07-03
10,ShanshanDu,26,13698424612,Operation,2017-07-02

写程序，实现数据的增删改查

查询
find name,age from staff_table where age > 22
find * from staff_table where dept = IT
find * from staff_table where enroll_date like 2013

增加
add staff_table EnweTu,18,18355328778,IT,2018-10-16

删除
delete from staff_table where staff_id = 11

更新
update staff_table set dept = Market where dept = IT
update staff_table set age = 1000 where name = AlexLi
