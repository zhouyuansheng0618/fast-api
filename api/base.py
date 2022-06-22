"""
@Author:zhouys
@Email:zhouys618@163.com
@FileName:base.py
@DateTime:2022/6/22 22:04
@SoftWare:PyCharm
基础路由
"""

from fastapi import APIRouter, Request

from api.login import index

router = APIRouter()


@router.get("/")
async def home(req: Request):
    return "hello"


# router.get('/index')(index)