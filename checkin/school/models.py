from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Parent(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    relation = models.CharField(max_length=25)
    work = models.TextField(null=True, blank=True)
    income = models.IntegerField(null=True, blank=True)
    address = models.TextField()
    type_house = models.CharField(max_length=25)
    tel = models.CharField(max_length=12)
    email = models.EmailField(max_length=254)



class Teacher(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.SmallIntegerField()
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    tel = models.CharField(max_length=12,  null=True) #เพิ่มเบอร์ครู
    tea_code = models.CharField(max_length=6, null=True) #เพิ่มรหัสครู
    image = models.ImageField(upload_to='uploads/', null=True)

class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False)
    age = models.SmallIntegerField()
    tel = models.CharField(max_length=12)
    address = models.TextField()
    GENDERS = (
        ('M', 'Male'),
        ('Fe', 'Female')
    )
    gender = models.CharField(max_length=2, choices=GENDERS)
    class_room = models.CharField(max_length=6)
    stu_no = models.SmallIntegerField()
    track = models.CharField(max_length=25)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    stu_code = models.CharField(max_length=5, null=True)
    parent_id = models.ForeignKey(Parent, on_delete=models.PROTECT)
    teacher_id = models.ForeignKey(Teacher, on_delete=models.PROTECT)

class Regis_school(models.Model):
    datetime = models.DateTimeField(auto_now=False, auto_now_add=False)
    TYPE = (
        ('IN', 'in'),
        ('OUT', 'out')
    )
    check_type =  models.CharField(max_length=3, choices=TYPE)
    score = models.SmallIntegerField()
    student = models.ForeignKey(Student, on_delete=models.PROTECT)

class Course(models.Model):
    name = models.CharField(max_length=50)
    teach_course = models.ManyToManyField(Teacher)

class Enroll(models.Model):
    course = models.ForeignKey(Course, on_delete=models.PROTECT)
    student = models.ForeignKey(Student, on_delete=models.PROTECT)

class Attendance(models.Model):
    score = models.SmallIntegerField()
    score_percent = models.SmallIntegerField()
    session = models.SmallIntegerField()
    enroll = models.ForeignKey(Enroll, on_delete=models.PROTECT)