from django import forms

from .models import Teacher, Course


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('name', 'course_id', 'room', 'weekday', 'capacity', 'start_time', 'end_time')
        labels = {
            'name': 'ชื่อวิชา',
            'course_id': 'รหัสวิชา',
            'room': 'ห้องเรียน',
            'weekday': 'วันที่เรียน',
            'capacity': 'จำนวนที่รับ',
            'start_time': 'เวลาเริ่ม',
            'end_time': 'เวลาสิ้นสุด'
        }
        widgets = {
            'title': forms.TextInput(attrs={ 'class' : 'form-control' })
        }