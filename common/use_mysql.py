#!/usr/bin/python3
# coding:utf-8
from __future__ import print_function
import pymysql
from config import global_parameters
'''
Created on 2017-10-19
@author: luting
Project:基础类UseMysql，对数据库进行增删改查
'''


class UseMysql(object):

    host = global_parameters.mysql_host
    port = int(global_parameters.mysql_port)
    user = global_parameters.mysql_user
    psw = global_parameters.mysql_passwd
    db = global_parameters.mysql_db

    @staticmethod
    def get_connect():
        """
        链接数据库
        :return:   数据库对象 conn
        """
        try:
            conn = pymysql.connect(host=UseMysql.host,
                                   port=UseMysql.port,
                                   user=UseMysql.user,
                                   passwd=UseMysql.psw,
                                   db=UseMysql.db)
            print(u"链接数据库 %s 成功" % UseMysql.db)
            return conn
        except pymysql.Error as e:
            print("Mysql Error:%s" % e)

    def execute_sql(self, sql):
        """
        操作的sql语句
        :param sql:   所要执行的sal语句
        :return:      获取执行结果 二进制
        """
        conn = self.get_connect()
        cursor = conn.cursor()
        try:
            cursor.execute(sql)
            conn.commit()
            print("执行sql语句：%s" % sql)
            global result
            result = cursor.fetchall()
            if len(result) == 0:
                print('不存在该数据')
            else:
                print("sql执行结果：%s" % str(result))
        except pymysql.Error as e:
            conn.rollback()
            print("Mysql Error:%s" % e)
        finally:
            cursor.close()
            conn.close()
            return result

    def delete_data(self, table_name, key):
        """
        删除表数据
        :param table_name:   表名
        :param key:          条件语句
        :return:
        """
        delete_sql = ('{0}'+'{2}'+table_name+'{2}'+'{1}'+'{2}'+key).format('delete from', 'where', ' ')
        self.execute_sql(delete_sql)

    def select_data(self, key, table_name, value):
        """
        查询表数据
        :param key:          字段名
        :param table_name:   表名
        :param value:        条件语句
        :return:             sql执行结果
        """
        select_sql = 'select %s from %s where %s' % (key, table_name, value)
        return self.execute_sql(select_sql)

    def update_data(self, table_name, key, value):
        """
        更新表数据
        :param table_name:   表名
        :param key:          更新内容
        :param value:        条件语句
        :return:
        """
        update_sql = 'update %s  set %s where %s  ' % (table_name, key, value)
        self.execute_sql(update_sql)

    def insert_data(self, tables_name, key, value):
        """
        新增表数据
        :param tables_name:   表名
        :param key:           字段名
        :param value:         新增的值
        :return:
        """
        insert_data = 'insert into %s(%s) values (%s)' % (tables_name, key, value)
        self.execute_sql(insert_data)

if __name__ == '__main__':
    mysql = UseMysql()
    # mysql.get_connect()
    mysql.execute_sql('show tables')
    # mysql.delete_data('contract', "CT_ID ='425'")
    # mysql.select_data('*', 'asset', "AST_ID='682500000'")
    # mysql.update_data('asset', "RP_ID='4'", "AST_ID='6825'")
    # mysql.insert_data('safety_inspection_point',
    #  'RP_ID,POINT_NAME,DELETED,CREATED_BY,CREATED_TIME,VERSION',"'1','python','0','50219','2017-03-14 13:58:07','1'")
