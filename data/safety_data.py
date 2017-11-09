#!usr/bin/python3
# coding:utf-8
from __future__ import print_function
from common.use_mysql import UseMysql
from common.log import Log

# 安全巡检测试账号：18912656465    12345678

mysql = UseMysql()
log = Log()



def insert_inspection_point1():
    """
    添加巡检点1
    :return:
    """
    mysql.insert_data('safety_inspection_point', 'RP_ID,POINT_NAME,DELETED,CREATED_BY,CREATED_TIME,VERSION',"'1','point1','0','47849','2017-11-03 14:16:49','1'")


def insert_inspection_point2():
    """
    添加巡检点2
    :return:
    """
    mysql.insert_data('safety_inspection_point', 'RP_ID,POINT_NAME,DELETED,CREATED_BY,CREATED_TIME,VERSION',"'1','point2','0','47849','2017-11-03 14:16:49','1'")


def delete_inspection_point():
    """
    删除巡检点
    :return:
    """
    mysql.delete_data('safety_inspection_point', "RP_ID = '1'")


def insert_inspection_team_team():
    """
    添加班组(组)
    :return:
    """
    mysql.insert_data('safety_team', 'RP_ID,TEAM_NAME,DELETED,CREATED_BY,CREATED_TIME,VERSION', "'1','testTeam','0','47849','2017-11-03 14:16:49','1'")


def delete_inspection_team_team():
    """
    删除班组(组)
    :return:
    """
    mysql.delete_data('safety_team', "RP_ID = '1'")


def select_inspection_team_team():
    """
    查询到safety_team的 TEAM_ID
    :return:
    """
    team_id = mysql.select_data('TEAM_ID', 'safety_team', "TEAM_NAME = 'testTeam'")
    return team_id[0][0]


def select_inspection_team_user():
    """
    查询到 safety_user_team的USER_ID
    :return:
    """
    user_id = mysql.select_data('USER_ID', 'safety_user_team', "RP_ID = '1' AND DELETED = '0' AND TEAM_ID = %s" % select_inspection_team_team())
    return user_id[0][0]


def insert_inspection_team_user():
    """
    添加班组（人员）
    :return:
    """
    mysql.insert_data('safety_user_team', 'RP_ID,TEAM_ID,USER_ID,DELETED,CREATED_BY,CREATED_TIME,VERSION', "'1',%s,'54497','0','47849','2017-11-03 16:02:24','1'" % select_inspection_team_team())


def delete_inspection_team_user():
    """
    删除班组（人员）
    :return:
    """
    mysql.delete_data('safety_user_team', "RP_ID = '1' ")


def insert_inspection_time():
    """
    添加时段
    :return:
    """
    mysql.insert_data('safety_inspection_setting', 'RP_ID,TIME_FRAME_LENGTH,TIME_FRAME_NAME,IS_ACROSS_DAY,BEGIN_TIME,END_TIME,DELETED,CREATED_BY,CREATED_TIME,VERSION', "'1','23','testTime','1','2017-11-10 01:00:00','2017-11-10 01:00:00','0','47849','2017-11-03 15:16:59','1'")


def delete_inspection_time():
    """
    删除时段
    :return:
    """
    mysql.delete_data('safety_inspection_setting', "RP_ID = '1'")


def select_inspection_time():
    """
    查询到safety_inspection_setting表中的 SETTING_ID
    :return:
    """
    setting_id = mysql.select_data('SETTING_ID', 'safety_inspection_setting', "RP_ID = '1' AND DELETED = '0'")
    return setting_id[0][0]


def insert_inspection_plan():
    """
    添加排版计划-计划
    :return:
    """
    mysql.insert_data('safety_inspection_plan', 'RP_ID,PLAN_NAME,COLOR,SETTING_ID,FREQUENCY,IS_ALL_POINT,IS_TEMPLATE,DELETED,CREATED_BY,CREATED_TIME,VERSION', "'1','planTest','#E08283',%s,'1','1','1','0','47849','2017-11-03 17:34:49','1'" % select_inspection_time())


def delete_inspection_plan():
    """
    删除排版计划-计划
    :return:
    """
    mysql.delete_data('safety_inspection_plan', "RP_ID = '1'")


def select_inspection_plan():
    """
    查询到safety_inspection_plan表中的PLAN_ID
    :return:
    """
    plan_id = mysql.select_data('PLAN_ID', 'safety_inspection_plan', "RP_ID = '1' AND DELETED ='0'")
    return plan_id[0][0]


def select_inspection_plan_new():
    """
    查询到safety_inspection_plan表中最新记录的PLAN_ID
    :return:
    """
    plan_id = mysql.select_data('PLAN_ID', 'safety_inspection_plan', "RP_ID = '1' ORDER BY PLAN_ID DESC LIMIT 1")
    return plan_id[0][0]


def insert_inspection_plan_team():
    """
    添加-排版计划-组
    :return:
    """
    mysql.insert_data('safety_inspection_plan_team_user', 'PLAN_ID,RP_ID,REF_ID,REF_NAME,TYPE,DELETED,CREATED_BY,CREATED_TIME,VERSION', "%s,'1',%s,'testTeam','1','0','47849','2017-11-06 19:11:49','1'" % (select_inspection_plan(), select_inspection_team_team()))


def insert_inspection_day_plan_team():
    """
    添加-日历计划-组
    :return:
    """
    mysql.insert_data('safety_inspection_plan_team_user', 'PLAN_ID,RP_ID,REF_ID,REF_NAME,TYPE,DELETED,CREATED_BY,CREATED_TIME,VERSION', "%s,'1',%s,'testTeam','1','0','47849','2017-11-06 19:11:49','1'" % (select_inspection_plan_new(), select_inspection_team_team()))


def delete_inspection_plan_team():
    """
    删除-排版计划-组
    :return:
    """
    mysql.delete_data('safety_inspection_plan_team_user', "RP_ID = '1' ")


def insert_inspection_plan_today():
    """
    添加-排版-日历
    :return:
    """
    mysql.insert_data('safety_inspection_plan', 'RP_ID,PLAN_NAME,COLOR,SETTING_ID,FREQUENCY,IS_ALL_POINT,TEMPLATE_ID,IS_TEMPLATE,TIME_LENGTH,BEGIN_TIME,END_TIME,DELETED,CREATED_BY,CREATED_TIME,VERSION', "'1','planTest','#E08283',%s,'1','1',%s,'0','23','2017-11-07 01:00:00','2017-11-08 01:00:00','0','47849','2017-11-06 20:08:41','1'" % (select_inspection_time(), select_inspection_plan()))


def safety_insert():
    """
    安全巡检计划新增
    :return:
    """
    insert_inspection_point1()
    insert_inspection_point2()
    insert_inspection_team_team()
    insert_inspection_team_user()
    insert_inspection_time()
    insert_inspection_plan()
    insert_inspection_plan_team()
    insert_inspection_plan_today()
    insert_inspection_day_plan_team()
    log.info('Add inspection data success')


def safety_delete():
    """
    安全巡检计划删除
    :return:
    """
    delete_inspection_point()
    delete_inspection_team_team()
    delete_inspection_team_user()
    delete_inspection_time()
    delete_inspection_plan()
    delete_inspection_plan_team()
    log.info('Delete inspection data success')


if __name__ == '__main__':
    # insert_inspection_point()
    # delete_inspection_point()
    # insert_inspection_team_team()
    # delete_inspection_team_team()
    # print(select_inspection_team_team())
    # insert_inspection_time()
    # delete_inspection_time()
    # insert_inspection_team_user()
    # print(select_inspection_time())
    # insert_inspection_plan()
    # delete_inspection_plan()
    # print(select__inspection_plan())
    # print(select_inspection_team_user)
    # insert_inspection_plan_team()
    safety_delete()
    safety_insert()
