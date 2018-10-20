from django.db import models

# Create your models here.


# 图书管理系统，书，作者，出版社


# 出版社
class Publisher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, null=False, unique=True)

    def __str__(self):
        return "<Publisher Object: {}>".format(self.name)


# 书
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64, null=False, unique=True)
    publisher = models.ForeignKey(to="Publisher")

    def __str__(self):
        return "<Book Object: {}>".format(self.title)


# 作者
class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=16, null=False, unique=True)
    # 多对多的对应关系
    book = models.ManyToManyField(to="Book")

    def __str__(self):
        return "<Author Object: {}>".format(self.name)

