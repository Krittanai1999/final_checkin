from django.contrib import admin
from school.models import Student, Parent , Teacher, Course, Regis_school, Enroll, Attendance
from django.contrib.auth.models import Permission
# Register your models here.

admin.site.register(Permission)

admin.site.register(Student)

admin.site.register(Parent)

admin.site.register(Teacher)

admin.site.register(Course)

admin.site.register(Regis_school)

admin.site.register(Enroll)

admin.site.register(Attendance)