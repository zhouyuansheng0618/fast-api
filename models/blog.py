# -*- coding: utf-8 -*-
"""
@Auth ： zhouys
@Email:zhouys618@163.com
@File ：blog.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
@Time ： 2022/6/29 23:10
"""
from base import TimestampMixin
from tortoise import fields


class Blog(TimestampMixin):

    title = fields.CharField(max_length=255, null=True, description="文章标题")
    first_picture = fields.CharField(max_length=255, null=True, description="文章首图，用于随机文章展示")
    content = fields.TextField(max_length=255, null=True, description="文章正文")
    description = fields.TextField(max_length=255, null=True, description="描述")
    is_published = fields.CharEnumField(default=1, description="公开或私密")
    class Meta:
        table_description = "博客"
        table = "blog"