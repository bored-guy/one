#!/usr/bin/env python
# -*- coding:utf-8 -*-


"""
@author: 崔博凯
@contact: 2232652509@qq.com
@contact: dioxincreature@163.com
@file: models.py
@time: 2021/1/23/8:10
"""

from django.db import models


class User(models.Model):
    email = models.EmailField(max_length=50, verbose_name="邮箱")
    password = models.CharField(max_length=20, verbose_name="密码")
    identify_code = models.CharField(max_length=20)
    yanzheng_code = models.IntegerField(null=True)
    if_yanzheng = models.BooleanField(null=True)
    if_person_inform = models.BooleanField(null=True, default=False)
    if_person_pic = models.BooleanField(null=True, default=False)
    if_person_money = models.BooleanField(null=True, default=False)
    if_person = models.BooleanField(null=True, default=False)
    if_team_num = models.BooleanField(null=True, default=False)
    if_team_inform = models.BooleanField(null=True, default=False)
    if_team_money = models.BooleanField(null=True, default=False)
    if_team = models.BooleanField(null=True, default=False)
    if_team_fenpei = models.BooleanField(null=True, default=False)


class Student(models.Model):
    name = models.CharField(max_length=5, verbose_name="姓名")
    sex = models.IntegerField(verbose_name="性别", choices=((0, "女"), (1, "男")))
    telephone = models.CharField(max_length=20, verbose_name="电话号")
    email = models.EmailField(max_length=50, verbose_name="邮箱")
    qq = models.CharField(max_length=20, verbose_name="QQ号")
    id_number = models.CharField(max_length=20, verbose_name="身份证号")
    school_name = models.CharField(max_length=30, verbose_name="学校名称")
    school_name_in_english = models.CharField(max_length=100, verbose_name="学校名称（英文）")
    place = models.IntegerField(verbose_name="所选会场",
                                choices=((1, "安全理事会"), (2, "世界卫生组织"), (3, "历史委员会"), (4, "特殊委员会：哈利波特联动委员会"),
                                         (5, "特殊委员会：1956西迁"),(6,"经社理事会"),(7,"主新闻中心")))
    identify_code = models.CharField(max_length=20, verbose_name="代码逻辑需要，请直接忽略")
    belongs_user = models.CharField(max_length=20, verbose_name="代码逻辑需要，请直接忽略")
    belongs_team = models.CharField(max_length=20, verbose_name="代码逻辑需要，请直接忽略")
    state = models.CharField(max_length=100, verbose_name="免责声明位置")
    if_room = models.IntegerField(null=True, verbose_name="是否住宿", choices=((0, "否"), (1, "是")))
    if_paid = models.BooleanField(null=True, verbose_name="是否已经付款", choices=((0, "否"), (1, "是")))
    if_email = models.BooleanField(null=True, default=False, verbose_name="发送邮件，选择”是“后发送", choices=((0, "否"), (1, "是")))


class Team(models.Model):
    school_name = models.CharField(max_length=20, verbose_name="学校名称")
    school_name_in_english = models.CharField(max_length=100, verbose_name="学校名称（英文）")
    first_name = models.CharField(max_length=10, verbose_name="第一联系人姓名")
    first_sex = models.IntegerField(null=True, verbose_name="第一联系人性别", choices=((0, "女"), (1, "男")))
    first_phone = models.CharField(max_length=20, verbose_name="第一联系人电话")
    first_mail = models.CharField(max_length=50, verbose_name="第一联系人邮箱")
    second_name = models.CharField(max_length=10, verbose_name="第二联系人姓名")
    second_sex = models.IntegerField(null=True, verbose_name="第二联系人性别", choices=((0, "女"), (1, "男")))
    second_phone = models.CharField(max_length=20, verbose_name="第二联系人电话")
    second_mail = models.CharField(max_length=50, verbose_name="第二联系人邮箱")
    teacher_num = models.IntegerField(null=True, verbose_name="指导教师人数")
    xiqian_num = models.IntegerField(null=True, verbose_name="1957西迁人数")
    harry_num = models.IntegerField(null=True, verbose_name="哈利波特特委人数")
    anli_num = models.IntegerField(null=True, verbose_name="安理会人数")
    San_num = models.IntegerField(null=True, verbose_name="历史委员会人数")
    jingshe_num = models.IntegerField(null=True, verbose_name="经社理事会人数")
    news_num = models.IntegerField(null=True, verbose_name="主新闻中心人数")
    shiwei_num = models.IntegerField(null=True, verbose_name="世界卫生组织人数")
    room_num = models.IntegerField(null=True, verbose_name="订房间人数")
    all_number = models.IntegerField(null=True, verbose_name="参会者总人数")
    finished_num = models.IntegerField(null=True)
    identify_code = models.CharField(max_length=30)
    if_fenpei = models.BooleanField(null=True, verbose_name="是否已经分配名额，分配完名额请将其改为是", choices=((0, "否"), (1, "是")))
    if_paid = models.BooleanField(null=True, verbose_name="是否已经付费", choices=((0, "否"), (1, "是")))
    if_email = models.BooleanField(null=True, default=False, verbose_name="发送邮件，选择”是“后发送", choices=((0, "否"), (1, "是")))
