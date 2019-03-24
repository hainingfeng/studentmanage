from django.shortcuts import render,HttpResponse,redirect
from app01 import models
# Create your views here.
# 班级列表
def classes_list(request):
    all_classes = models.Classes.objects.all()
    return render(request,'classes_list.html',{'all_classes':all_classes})
# 添加班级
def add_class(request):
    class_name,err_msg = '',''
    if request.method == 'POST':
        class_name = request.POST.get('class_name').strip()
        class_obj = models.Classes.objects.filter(name=class_name).first()
        if not class_name:
            err_msg = '班级不能为空'
        if class_obj:
            err_msg = '该班级已存在'
        if class_name and not class_obj:
            res = models.Classes.objects.create(name=class_name)
            return redirect('/classes_list/')
    return render(request,'add_class.html',{'err_msg':err_msg,'class_name':class_name })
# 删除班级
def del_class(request):
    pk = request.GET.get('pk')
    class_obj = models.Classes.objects.filter(pk=pk)
    print(models.Classes.objects.filter(pk=pk))
    print(class_obj)
    if not class_obj:
        return HttpResponse('该班级不存在')
    res = models.Classes.objects.filter(pk=pk).delete()
    print(res)
    return redirect('/classes_list/')
    # return render(request,'del_class.html')
# 编辑班级
def edit_class(request):
    err_msg = ''
    pk = request.GET.get('pk')
    class_obj = models.Classes.objects.filter(pk=pk).first()
    print(class_obj,type(class_obj))
    if request.method == 'POST':
        class_name = request.POST.get('class_name').strip()
        obj = models.Classes.objects.filter(name=class_name).first()
        print(class_name,obj,type(obj))
        if obj:
            err_msg = '该班级已存在'
        if not class_name:
            err_msg = '班级名称不能为空'
        if not obj and class_name:
            class_obj.name = class_name
            class_obj.save()
            return redirect('/classes_list/')
    return render(request,'edit_class.html',{'class_obj':class_obj,'err_msg':err_msg})

# 学生列表
def students_list(request):
    all_students = models.Students.objects.all()
    return render(request,'students_list.html',locals())
# 添加学生
def add_student(request):
    err_msg = ''
    if request.method == 'POST':
        student_name = request.POST.get('student_name').strip()
        gender_id = request.POST.get('gender_id')
        class_id = request.POST.get('class_id')
        student_obj = models.Students.objects.filter(sname=student_name)
        print(student_name,class_id,type(student_name))
        print(student_obj,type(student_obj))
        if not student_name:
            err_msg = '姓名不能为空'
        if  student_obj:
            err_msg = '该学生已存在'
        if student_name and not student_obj:
            res = models.Students.objects.create(sname=student_name,gender=gender_id,classes_id=class_id)
            print(res,type(res))
            return redirect('/students_list/')

    all_classes = models.Classes.objects.all()
    return render(request,'add_student.html',locals())
# 删除学生
def del_student(request):
    student_id = request.GET.get('pk')
    student_obj = models.Students.objects.filter(pk=student_id)
    if not student_obj:
        return HttpResponse('该学生不存在')
    res = models.Students.objects.filter(pk=student_id).delete()
    print(res,type(res))
    return redirect('/students_list/')
# 编辑学生列表
def edit_student(request):
    err_msg = ''
    pk = request.GET.get('pk')
    student_obj = models.Students.objects.filter(pk=pk).first()
    print(student_obj.classes)
    # gender = ['男','女']
    if request.method == 'POST':
        student_name = request.POST.get('student_name').strip()
        gender_id = request.POST.get('gender_id')
        class_id = request.POST.get('class_id')
        obj = models.Students.objects.filter(sname=student_name).first()
        if not student_name:
            err_msg = '不能为空'
        if obj:
            err_msg = '该学生已存在'
        # if obj != student_obj:
        #     err_msg = '该学生已存在'
        # else:
        #     # return redirect('/students_list/')
        #     return HttpResponse('error')
        if student_name and not obj:
            student_obj.sname = student_name
            # student_obj.gender = gender_id
            student_obj.classes_id = class_id
            student_obj.save()
            return redirect('/students_list/')
    all_classes = models.Classes.objects.all()
    return render(request,'edit_student.html',locals())

# 老师列表
def teachers_list(request):
    all_teachers = models.Teachers.objects.all()
    return render(request,'teachers_list.html',locals())
# 添加老师
def add_teacher(request):
    err_msg = ''
    if request.method == 'POST':
        teacher_name = request.POST.get('teacher_name').strip()
        teacher_obj = models.Teachers.objects.filter(tname=teacher_name)
        if not teacher_name:
            err_msg = '不能为空'
        if  teacher_obj:
           err_msg = '该老师已存在'
        if not teacher_obj:
            res = models.Teachers.objects.create(tname=teacher_name)
            print(res)
            return redirect('/teachers_list/')
    return render(request,'add_teacher.html',locals())
# 删除老师
def del_teacher(request):
    err_msg = ''
    pk = request.GET.get('pk')
    teacher_obj = models.Teachers.objects.filter(pk=pk)
    if not teacher_obj:
        return HttpResponse('该老师不存在')
    teacher_obj.delete()
    return redirect('/teachers_list/')
# 编辑老师
def edit_teacher(request):
    err_msg = ''
    pk = request.GET.get('pk')
    teacher_obj = models.Teachers.objects.filter(pk=pk).first()
    if request.method == 'POST':
        teacher_name = request.POST.get('teacher_name').strip()
        obj = models.Teachers.objects.filter(tname=teacher_name).first()
        if not teacher_name:
            err_msg = '不能为空'
        if obj != teacher_obj:
            err_msg = '该老师已存在'
        else:
            return redirect('/teachers_list/')
        if teacher_name and not obj:
            teacher_obj.tname = teacher_name
            teacher_obj.save()
            return redirect('/teachers_list/')
    return render(request,'edit_teacher.html',locals())

def courses_list(request):
    all_courses = models.Courses.objects.all()
    # for course in all_courses:
    #     print(course.cname)
    #     print(course.teacher,type(course.teacher))
    #     print(course.teacher.tname,type(course.teacher.tname))
    #     print(course.student,type(course.student))
    #     print(course.student.all(),type(course.student.all()))
    #     print('*'*30)
    # return HttpResponse('OK')
    return render(request,'courses_list.html',locals())

def add_course(request):
    err_msg = ''
    all_students = models.Students.objects.all()
    all_teacher = models.Teachers.objects.all()
    if request.method =='POST':
        course_name = request.POST.get('course_name').strip()
        teacher_id = request.POST.get('teacher_id')
        student_id = request.POST.getlist('student_id')
        print(request.POST)
        # print(course_name,type(course_name))
        # print(teacher_id,type(teacher_id))
        # print(student_id,type(student_id))
        # print('*'*30)
        # return HttpResponse('OK')
        course_obj = models.Courses.objects.filter(cname=course_name).first()
        print(course_obj)
        if not course_name:
            err_msg = '课程不能为空'
        if course_obj:
            err_msg = '课程已存在'
        if course_name and not course_obj:
            # 第一种方法，通过Courses数据库中的teacher_id字段进行插入
            # course_obj = models.Courses.objects.create(cname=course_name,teacher_id=teacher_id)
            # 第二种方法，通过models中Courses类的teacher属性字段进行插入
            teacher_obj = models.Teachers.objects.filter(pk=teacher_id).first()
            course_obj = models.Courses.objects.create(cname=course_name, teacher=teacher_obj)
            course_obj.student.set(student_id)
            return redirect('/courses_list/')

    return render(request,'add_course.html',locals())

def del_course(request):
    pk = request.GET.get('pk')
    course_id = models.Courses.objects.filter(pk=pk)
    if not course_id:
        return HttpResponse('该课程不存在')
    res = models.Courses.objects.filter(pk=pk).delete()
    return redirect('/courses_list/')

def edit_course(request):
    pk = request.GET.get('pk')
    course_obj = models.Courses.objects.filter(pk=pk).first()
    if request.method == 'POST':
        course_name = request.POST.get('course_name').strip()
        teacher_id = request.POST.get('teacher_id')
        student_id = request.POST.getlist('student_id')

        obj = models.Courses.objects.filter(cname=course_name).first()
        print(obj)
        if not course_name:
            err_msg = '课程不能为空'
        if obj:
            err_msg = '课程已存在'
        if course_name and not obj:
            # 第一种方法，通过models中Courses类的teacher属性字段进行插入
            teacher_obj = models.Teachers.objects.filter(pk=teacher_id).first()
            course_obj.cname = course_name
            course_obj.teacher = teacher_obj
            course_obj.student.set(student_id)
            course_obj.save()
            # 第二种方法，通过Courses数据库中的teacher_id字段进行插入
            # course_obj.cname = course_name
            # course_obj.teacher_id = teacher_id
            # course_obj.save()
            # course_obj.student.set(student_id)
            return redirect('/courses_list/')
    all_teachers = models.Teachers.objects.all()
    all_students = models.Students.objects.all()
    return render(request,'edit_course.html',locals())
