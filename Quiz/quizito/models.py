
from django import forms
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# class User(forms.ModelForm):
#     pass

# Task:
# Design a prototype Backend for Public QUIZ 
# interface with login, register and public leader board system in django

class Category(models.Model):
    categoryid = models.IntegerField(default=1)
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=225)


    def __str__(self):
        return self.name


class Question(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    quesid = models.IntegerField(default=1)
    marks = models.IntegerField(default=0)
    question = models.CharField(max_length=225)
    op1 = models.CharField(max_length=200,null=True)
    op2 = models.CharField(max_length=200,null=True)
    op3 = models.CharField(max_length=200,null=True)
    op4 = models.CharField(max_length=200,null=True)
    ans = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.question

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    number_of_options = models.IntegerField(default=4)
    

class Leaderboard(models.Model):
    # user = models.ManyToOneRel(User, on_delete=models.CASCADE)
    # marks = models.ForeignKey(Marks, on_delete=models.CASCADE)y
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.marks