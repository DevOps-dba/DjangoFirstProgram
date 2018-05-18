# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import connections
# Create your models here.


def query(sql, source):
    cursor = connections[source].cursor()  # 获得一个游标(cursor)对象
    cursor.execute(sql)
    raw_data = cursor.fetchall()
    col_names = [desc[0] for desc in cursor.description]

    result = []
    for row in raw_data:
        obj_dict = {}
        # 把每一行的数据遍历出来放到Dict中
        for index, value in enumerate(row):
            obj_dict[col_names[index]] = value

        result.append(obj_dict)

    return result
