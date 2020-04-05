

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Group, User
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.db.models import Q

from school.models import Student, Parent, Teacher


# Create your views here.
def my_login(request):
    context = {}

    if request.method == 'POST': #รับค่า POST จาก from
        username = request.POST.get('username') # รับ user
        password = request.POST.get('password') # รับ password

        user = authenticate(request, username=username, password=password) # เปรียนเทียบuesrname password

        if user: 
            login(request, user) 

            next_url = request.POST.get('next_url')
            if next_url:
                return redirect(next_url)
            else:
                return redirect('index')
        else:
            context['username'] = username
            context['password'] = password
            context['error'] = 'Wrong username or password!'

    next_url = request.GET.get('next')
    if next_url:
        context['next_url'] = next_url

    return render(request, template_name='login.html', context=context)

def my_logout(request):
    logout(request)
    return redirect('login') #พอกด logout ก้จะไปหน้า login

def index(request):
    """
        Index page - หน้าจอรายการนักเรียนทั้งหมด
    """
    student = Student.objects.all()
    parent = Parent.objects.all()
    search = request.GET.get('search', '')
    context ={}
    students = User.objects.filter(
        Q(first_name__icontains=search) | # | คือ หรือ(or) Q คือ Q object
        Q(last_name__icontains=search) | 
        Q(username__icontains=search)
    ).order_by('username')
   
    return render(request, 'school/index.html', context={
        'student': student,
        'parent' : parent
    })

def student_add(request):
    """
        เพิ่มข้อมูล นักเรียน ใหม่เข้าสู่ฐานข้อมูล
    """
    student = Student.objects.all()
    parent = Parent.objects.all()
    teacher = Teacher.objects.all()
    msg = ''

    if request.method == 'POST':
        
        user = User.objects.create_user(
            request.POST.get('username'),
            request.POST.get('email'),
            '1234',
        )
        group = Group.objects.get(name='student')
        user.groups.add(group)
        user.save()
        
        
        birthday = request.POST.get('date_of_birth').split('/')[::-1]
        birthday[1], birthday[2] = birthday[2], birthday[1]
        birthday = '-'.join(birthday)
        
        student = Student.objects.create(
            fname = request.POST.get('first_name'),
            lname = request.POST.get('last_name'),
            stu_code = request.POST.get('username'),
            date_of_birth = birthday,
            age = request.POST.get('age'),
            gender = request.POST.get('gender'),
            tel = request.POST.get('tel'),
            email = request.POST.get('email'),
            address = request.POST.get('address'),
            class_room = request.POST.get('class'),
            stu_no = request.POST.get('stu_no'),
            track = request.POST.get('track'),
            parent_id = Parent.objects.get(pk=request.POST.get('parent')),
            teacher_id = Teacher.objects.get(pk=request.POST.get('teacher')),
            user=user
        )
       
        
        msg = 'SUCCESSFULLY CREATE NEW STUDENT - ID : %s' % (student.id)
    else:
        student = Student.objects.none()
    context = {
        'student': student,
        'parent':parent,
        'teacher':teacher,
        'gender': Student.GENDERS,
        'msg': msg
    }

    return render(request, 'school/student_add.html', context=context)

def parent_add(request):
    """
        เพิ่มข้อมูล นักเรียน ใหม่เข้าสู่ฐานข้อมูล
    """
    parent = Parent.objects.all()
    msg = ''
    if request.method == 'POST':
        parent = Parent.objects.create(
            fname = request.POST.get('first_name1'),
            lname = request.POST.get('last_name1'),
            relation = request.POST.get('relation'),
            work = request.POST.get('work'),
            income = request.POST.get('income'),
            tel = request.POST.get('tel1'),
            email = request.POST.get('email1'),
            address = request.POST.get('address1'),
            type_house = request.POST.get('type_house'),
            
        )
        msg = 'SUCCESSFULLY CREATE NEW PARENT ID : %s' % (parent.id)
    else:
        
        parent = Parent.objects.none()
    context = {
        'parent': parent,
        'msg': msg
    }

    return render(request, 'school/parent_add.html', context=context)

def parent_update(request, parent_id):
    """
        #Update ข้อมูลนักเรียนที่มี id = parent_id
    """
    
    try:
        parent = Parent.objects.get(pk=parent_id)
        parent = Parent.objects.all()
        msg = ''
    except parent.DoesNotExist: #ถ้าส่งidบะหาไม่เจอ ให้rediect to room_list
        return redirect('index')

    if request.method == 'POST':
        parent.parent_id=request.POST.get('parent_id')
        parent.fname=request.POST.get('first_name1')
        parent.lname=request.POST.get('last_name1')
        parent.relation=request.POST.get('relation')
        parent.work=request.POST.get('work')
        parent.income=request.POST.get('income')
        parent.tel=request.POST.get('tel1')
        parent.email=request.POST.get('email1')
        parent.address=request.POST.get('address1')
        parent.type_house=request.POST.get('type_house')

        parent.save()
        msg = 'SUCCESSFULLY UPDATE PARENT ID : %s' % (parent.id)
    
    context = {
        'parent': parent,    
        'msg': msg
    }

    return render(request, 'school/parent_add.html', context=context)

def parent_delete(request, parent_id):
    """
        #ลบข้อมูล classparent โดยลบข้อมูลที่มี id = class_id
    """
    parent = Parent.objects.get(id = parent_id)
    parent.delete()
    return redirect(to='index')

'''
def student_update(request, student_id):
    """
        #Update ข้อมูลนักเรียนที่มี id = student_id
    """
    
    try:
        student = Student.objects.get(pk=student_id)
        student = Student.objects.all()
        
        msg = ''
    except Student.DoesNotExist: #ถ้าส่งidบะหาไม่เจอ ให้rediect to room_list
        return redirect('index')

    if request.method == 'POST':
        student.student_id=request.POST.get('student_id')
        student.name=request.POST.get('name')
        student.open_time=request.POST.get('open_time')
        student.close_time=request.POST.get('close_time')
        student.capacity=request.POST.get('capacity')

        student.save()
        msg = 'SUCCESSFULLY UPDATE STUDENT : %s' % (student.name)
    
    context = {
        'student': student,    
        'msg': msg
    }

    return render(request, 'school/school_add.html', context=context)
'''
'''
def student_delete(request, student_id):
    """
        #ลบข้อมูล classstudent โดยลบข้อมูลที่มี id = class_id
    """
    student = Student.objects.get(id = student_id)
    student.delete()
    return redirect(to='index')
'''
def teacher(request):
    
    teacher = Teacher.objects.all()
    
    
    return render(request, template_name='school/teacher.html', context={
        'teacher' : teacher
    })

def teacher_add(request):
    """
        เพิ่มข้อมูล room ใหม่เข้าสู่ฐานข้อมูล
    """
    teacher = Teacher.objects.all()
    msg = ''
    if request.method == 'POST':
        user = User.objects.create_user(
            request.POST.get('username'),
            request.POST.get('email'),
            '1234',
        )
        group = Group.objects.get(name='teacher')
        user.groups.add(group)
        user.save()
        teacher = Teacher.objects.create(
            fname = request.POST.get('fname'),
            lname = request.POST.get('lname'),
            tel = request.POST.get('tel'),
            email = request.POST.get('email'),
            room = request.POST.get('room'),
            tea_code = request.POST.get('tea_code'),
            user=user
            
        )
        msg = 'SUCCESSFULLY CREATE NEW TEACHER NAME : %s' % (teacher.fname)
    else:
        
        teacher = Teacher.objects.none()
    context = {
        'teacher' : teacher,
        'msg': msg
    }

    return render(request, 'school/teacher_add.html', context=context)

def teacher_update(request, teacher_id):
    """
        #Update ข้อมูลนักเรียนที่มี id = parent_id
    """
    
    try:
        teacher = Teacher.objects.get(pk=teacher_id)
        teacher = Teacher.objects.all()
        msg = ''
    except teacher.DoesNotExist:
        return redirect('index')

    if request.method == 'POST':
        teacher.teacher_id=request.POST.get('teacher_id'),
        teacher.fname=request.POST.get('fname'),
        teacher.lname=request.POST.get('lname'),
        teacher.tel=request.POST.get('tel1'),
        teacher.email=request.POST.get('email1'),
        teacher.tea_code=request.POST.get('tea_code'),
        
        teacher.save()
        msg = 'SUCCESSFULLY UPDATE TEACHER ID : %s' % (teacher.id)
    
    context = {
        'teacher': teacher,    
        'msg': msg
    }

    return render(request, 'school/teacher.html', context=context)

def teacher_delete(request, teacher_id):
    
    teacher = Teacher.objects.get(id = teacher_id)
    teacher.delete()
    return redirect(to='index')


def course(request):
    

    context = {}

    
    return render(request, template_name='school/course.html', context=context)

def course_add(request):
    """
        เพิ่มข้อมูล room ใหม่เข้าสู่ฐานข้อมูล
    """
    context = {}

    return render(request, 'school/course_add.html', context=context)

def school_list(request):
    """
        เพิ่มข้อมูล room ใหม่เข้าสู่ฐานข้อมูล
    """
    context = {}

    return render(request, 'school/school.html', context=context)

def check_school(request):
    """
        เพิ่มข้อมูล room ใหม่เข้าสู่ฐานข้อมูล
    """
    context = {}

    return render(request, 'school/check_school.html', context=context)

def class_list(request):
    """
        เพิ่มข้อมูล room ใหม่เข้าสู่ฐานข้อมูล
    """
    context = {}

    return render(request, 'school/class.html', context=context)

def check_class(request):
    """
        เพิ่มข้อมูล room ใหม่เข้าสู่ฐานข้อมูล
    """
    context = {}

    return render(request, 'school/check_class.html', context=context)

def detailclass(request):
    """
        เพิ่มข้อมูล room ใหม่เข้าสู่ฐานข้อมูล
    """
    context = {}

    return render(request, 'school/detailclass.html', context=context)

def score(request):
    """
        เพิ่มข้อมูล room ใหม่เข้าสู่ฐานข้อมูล
    """
    context = {}

    return render(request, 'school/score.html', context=context)

def scoreedit(request):
    """
        เพิ่มข้อมูล room ใหม่เข้าสู่ฐานข้อมูล
    """
    context = {}

    return render(request, 'school/scoreedit.html', context=context)
