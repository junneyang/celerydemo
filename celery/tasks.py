#!/usr/bin/python
# -*- coding: utf-8 -*-

from celery import Celery
app = Celery('task', backend='redis://localhost', broker='redis://localhost:6379/0')

@app.task
def add(x, y):
    return x + y

