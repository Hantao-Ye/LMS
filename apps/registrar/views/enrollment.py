import json

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from apps.registrar.models import Course
from apps.registrar.models import Student


@login_required(login_url='/login')
def enrollment_page(request):
    # Create our student account which will build our registration around.
    try:
        student = Student.objects.get(user=request.user)
    except Student.DoesNotExist:
        student = Student.objects.create(user=request.user)
    try:
        courses = Course.objects.filter(students__student_id=student.student_id)
    except Course.DoesNotExist:
        courses = None
    return render(request, 'registrar/enrollment/view.html', {
        'student': student,
        'courses': courses,
        'user': request.user,
        'tab': 'enrollment',
        'HAS_ADVERTISMENT': settings.APPLICATION_HAS_ADVERTISMENT,
        'local_css_urls': settings.SB_ADMIN_2_CSS_LIBRARY_URLS,
        'local_js_urls': settings.SB_ADMIN_2_JS_LIBRARY_URLS
    })


@login_required()
def enrollment_table(request):
    # Create our student account which will build our registration around.
    try:
        student = Student.objects.get(user=request.user)
    except Student.DoesNotExist:
        student = Student.objects.create(user=request.user)
    try:
        courses = Course.objects.filter(students__student_id=student.student_id)
    except Course.DoesNotExist:
        courses = None
    return render(request, 'registrar/enrollment/table.html', {
        'student': student,
        'courses': courses,
        'user': request.user,
        'tab': 'enrollment',
    })


@login_required()
def disenroll_modal(request):
    # Create our student account which will build our registration around.
    try:
        student = Student.objects.get(user=request.user)
    except Student.DoesNotExist:
        student = Student.objects.create(user=request.user)

    course_id = int(request.POST['course_id'])
    try:
        course = Course.objects.get(id=course_id)
    except Course.DoesNotExist:
        course = None
    return render(request, 'registrar/enrollment/disenroll_modal.html', {
        'student': student,
        'course': course,
        'user': request.user,
    })


@login_required()
def disenroll(request):
    response_data = {'status': 'failure', 'message': 'unsupported request format'}
    if request.is_ajax():
        course_id = int(request.POST['course_id'])
        student = Student.objects.get(user=request.user)
        try:
            course = Course.objects.get(id=course_id)
            course.students.remove(student)
            response_data = {'status': 'success', 'message': 'disenrolled'}
        except Course.DoesNotExist:
            response_data = {'status': 'failed', 'message': 'record does not exist'}
    return HttpResponse(json.dumps(response_data), content_type="application/json")
