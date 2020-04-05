from django.urls import path
from . import views

urlpatterns = [
    #path('', views.my_login, name='login'),
    #path('logout/', views.my_logout, name='logout'),
    path('index/', views.index, name='index'),
    path('logout/', views.my_logout, name='logout'),
    path('student_add/', views.student_add, name='student_add'),
    #path('update/<int:student_id>/', views.student_update, name='student_update'),
    #path('delete/<int:student_id>/', views.student_delete, name='student_delete'),
    path('update/<int:parent_id>/', views.parent_update, name='parent_update'),
    path('parent_add/', views.parent_add, name='parent_add'),
    path('delete/<int:parent_id>/', views.parent_delete, name='parent_delete'),
    path('teacher/', views.teacher, name='teacher'),
    path('teacher_add/', views.teacher_add, name='teacher_add'),
    path('update/<int:teacher_id>/', views.teacher_update, name='teacher_update'),
    path('delete/<int:teacher_id>/', views.teacher_delete, name='teacher_delete'),
    path('course/', views.course, name='course'),
    path('course_add/', views.course_add, name='course_add'),
    path('school_list/', views.school_list, name='school_list'),
    path('school_list/check_school', views.check_school, name='check_school'),
    path('class_list', views.class_list, name='class_list'),
    path('class_list/check_class', views.check_class, name='check_class'),
    path('class_list/detail', views.detailclass, name='detailclass'),
    path('score/', views.score, name='score'),
    path('score/edit', views.scoreedit, name='scoreedit'),
]