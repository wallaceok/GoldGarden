/*注意事项*/
/*
1.关于时间字段，一律使用time模块生成当前时间  YYYY-mm-dd HH:MM:SS  2017-11-03 17:34:49，不然每次跑脚本之前都要手动去改，很傻比*/

/*--------------------创建巡检点------------------------------------------------------------------*/

/*巡检点-[查询]*/
SELECT * FROM safety_inspection_point WHERE RP_ID = '1'

/*巡检点-[统计safety_inspection_point存在多少数据]*/
SELECT COUNT(*) FROM safety_inspection_point WHERE RP_ID = '1'

/*巡检点-[清空]*/
truncate table  safety_inspection_point   /*MMP？*/

/*巡检点-[删除]*/
DELETE FROM safety_inspection_point WHERE RP_ID = '1' /*还好能delete*/


/*巡检点-[新增]*/
INSERT INTO  safety_inspection_point(RP_ID,POINT_NAME,DELETED,CREATED_BY,CREATED_TIME,VERSION) VALUES ('1','point1','0','47849','2017-11-03 14:16:49','1')


/*--------------------创建班组------------------------------------------------------------------*/
/*TMD 就两个字段还分两张表？逗我？？？*/
/*班组-组-[查询]*/
/*
脚本中的步骤
1.insert 班组-组 数据
2.select 根据班组名找到班组id
3.insert班组-人员，班组id关联，（%s）%TEAM_ID
*/
SELECT * FROM safety_team WHERE RP_ID = '1'
/*班组-组-[查询-TEAM_ID] */
SELECT TEAM_ID FROM safety_team WHERE TEAM_NAME = 'testTeam'

/*班组-组-[删除]*/
DELETE FROM safety_team WHERE RP_ID = '1'

/*班组-组-[新增]*/
INSERT INTO safety_team(RP_ID,TEAM_NAME,DELETED,CREATED_BY,CREATED_TIME,VERSION) VALUES ('1','testTeam','0','47849','2017-11-03 14:16:49','1')

/*班组-人员-[查询]*/
SELECT * FROM safety_user_team WHERE RP_ID = '1'

/*班组-人员-[USER_ID 查询]*/
SELECT USER_ID FROM safety_user_team WHERE RP_ID = '1' AND DELETED = '0' AND TEAM_ID = '104'

/*班组-人员-[删除]*/
DELETE FROM safety_user_team WHERE RP_ID = '1' 

/*班组-人员-[新增]*/
INSERT INTO safety_user_team(RP_ID,TEAM_ID,USER_ID,DELETED,CREATED_BY,CREATED_TIME,VERSION) VALUES ('1','104','54372','0','47849','2017-11-03 16:02:24','1')

/*--------------------创建时段------------------------------------------------------------------*/
/*时段-[查询]*/
SELECT * FROM safety_inspection_setting WHERE RP_ID = '1' AND DELETED = '0'

/*时间-[setting_id 查询]*/
SELECT SETTING_ID FROM safety_inspection_setting WHERE RP_ID = '1' AND DELETED = '0'

/*时段-[删除]*/
DELETE FROM safety_inspection_setting WHERE RP_ID = '1'

/*时段-[新增]*/
INSERT INTO safety_inspection_setting(RP_ID,TIME_FRAME_LENGTH,TIME_FRAME_NAME,IS_ACROSS_DAY,BEGIN_TIME,END_TIME,DELETED,CREATED_BY,CREATED_TIME,VERSION) 
VALUES ('1','23','testTime','1','2017-11-10 01:00:00','2017-11-10 01:00:00','0','47849','2017-11-03 15:16:59','1')


/*--------------------创建排版计划------------------------------------------------------------------*/
/*safety_inspection_plan 不包括 接受班组，接受用户，巡检点 （接受班组 or 接受用户 插入一种一个字段即可）*/
/*排版计划-计划-[查询]*/
SELECT * FROM safety_inspection_plan WHERE RP_ID = '1'

/*排版计划-计划-[plan_id 查询]*/
SELECT PLAN_ID FROM safety_inspection_plan WHERE RP_ID = '1' AND DELETED ='0'

/*排版计划-计划-[删除]*/
DELETE FROM safety_inspection_plan WHERE RP_ID = '1'

/*排版计划-计划-[新增]*/
INSERT INTO safety_inspection_plan(RP_ID,PLAN_NAME,COLOR,SETTING_ID,FREQUENCY,IS_ALL_POINT,IS_TEMPLATE,DELETED,CREATED_BY,CREATED_TIME,VERSION) 
VALUES ('1','planTest','#E08283','152','1','1','1','0','47849','2017-11-03 17:34:49','1')

/*排版计划-用户、组-[查询]*/
SELECT * FROM safety_inspection_plan_team_user WHERE RP_ID = '1' and PLAN_ID = '638'

/*排版计划-用户、组-[删除]*/
DELETE FROM safety_inspection_plan_team_user WHERE RP_ID = '1' 

/*排版计划-用户、组-[组- 添加]*/
INSERT INTO safety_inspection_plan_team_user(PLAN_ID,RP_ID,REF_ID,REF_NAME,TYPE,DELETED,CREATED_BY,CREATED_TIME,VERSION)
VALUES('670','1','104','testTeam','1','0','47849','2017-11-06 19:11:49','1');

/*排版计划-用户、组-[人员- 添加]*/
INSERT INTO safety_inspection_plan_team_user(PLAN_ID,RP_ID,REF_ID,REF_NAME,TYPE,DELETED,CREATED_BY,CREATED_TIME,VERSION)
VALUES('638','1','54372','测试','2','0','47849','2017-11-06 19:11:49','1')


/*--------------------巡检计划[日历排程]------------------------------------------------------------------*/
SELECT * FROM safety_inspection_plan WHERE RP_ID = '1';
SELECT * FROM safety_inspection_plan_team_user WHERE RP_ID = '1'; 

/*safety_inspection_plan最新的一条记录*/
SELECT * FROM safety_inspection_plan WHERE RP_ID = '1' ORDER BY PLAN_ID DESC LIMIT 1

SELECT * FROM safety_inspection_setting WHERE RP_ID = '1' AND DELETED = '0';

SELECT PLAN_ID FROM safety_inspection_plan WHERE PLAN_NAME = 'planTest'
INSERT INTO safety_inspection_plan(RP_ID,PLAN_NAME,COLOR,SETTING_ID,FREQUENCY,IS_ALL_POINT,TEMPLATE_ID,IS_TEMPLATE,TIME_LENGTH,BEGIN_TIME,END_TIME,DELETED,CREATED_BY,CREATED_TIME,VERSION)
VALUES('1','planTest','#E08283','154','1','1','647','0','23','2017-11-06 01:00:00','2017-11-07 01:00:00','0','47849','2017-11-06 20:08:41','1')


/*--------------------app巡检-巡检点添加-----------------------------------------------------------------*/


/*巡检情况-[查询]*/
SELECT * FROM safety_inspection
SELECT COUNT(*) FROM safety_inspection
/*安全巡检情况-[删除]*/
DELETE FROM safety_inspection

SELECT * FROM safety_inspection_plan_point WHERE RP_ID = '1'

DELETE FROM safety_inspection_plan_point





