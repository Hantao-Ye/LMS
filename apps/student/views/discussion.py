import json

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from apps.registrar.models import Course
from apps.registrar.models import CourseDiscussionThread
from apps.student.forms import CourseDiscussionPostForm
from apps.student.forms import CourseDiscussionThreadForm


@login_required(login_url='/login')
def discussion_page(request, course_id):
    course = Course.objects.get(id=course_id)

    try:
        threads = CourseDiscussionThread.objects.filter(course=course).order_by('date')
    except:
        threads = None

    return render(request, 'course/discussion/threads_view.html', {
        'course': course,
        'threads': threads,
        'user': request.user,
        'tab': 'discussion',
        'HAS_ADVERTISMENT': settings.APPLICATION_HAS_ADVERTISMENT,
        'local_css_urls': settings.SB_ADMIN_2_CSS_LIBRARY_URLS,
        'local_js_urls': settings.SB_ADMIN_2_JS_LIBRARY_URLS,
    })


@login_required(login_url='/login')
def threads_table(request, course_id):
    course = Course.objects.get(id=course_id)

    try:
        threads = CourseDiscussionThread.objects.filter(course=course).order_by('date')
    except:
        threads = None

    return render(request, 'course/discussion/threads_table.html', {
        'course': course,
        'threads': threads,
        'user': request.user,
    })


@login_required(login_url='/login')
def new_thread_modal(request, course_id):
    course = Course.objects.get(id=course_id)
    form = CourseDiscussionThreadForm()
    return render(request, 'course/discussion/new_thread_modal.html', {
        'course': course,
        'form': form,
        'user': request.user,
    })


@login_required(login_url='/login')
def insert_thread(request, course_id):
    response_data = {'status': 'failed', 'message': 'unknown error detected.'}
    if request.is_ajax():
        if request.method == 'POST':
            course = Course.objects.get(id=course_id)
            form = CourseDiscussionThreadForm(request.POST)
            form.instance.user = request.user
            form.instance.course = course
            if form.is_valid():
                form.save()
                response_data = {'status': 'success', 'message': 'submitted'}
            else:
                response_data = {'status': 'failed', 'message': json.dumps(form.errors)}
    return HttpResponse(json.dumps(response_data), content_type="application/json")


@login_required()
def delete_thread(request, course_id):
    response_data = {'status': 'failed', 'message': 'unknown error with deletion'}
    if request.is_ajax():
        if request.method == 'POST':
            thread_id = int(request.POST['thread_id'])
            course = Course.objects.get(id=course_id)
            try:
                thread = CourseDiscussionThread.objects.get(
                    course=course,
                    thread_id=thread_id
                )
                if thread.user == request.user:
                    thread.delete()
                    response_data = {'status': 'success', 'message': 'thread was deleted'}
                else:
                    response_data = {'status': 'failed', 'message': 'unauthorized deletion'}
            except CourseDiscussionThread.DoesNotExist:
                response_data = {'status': 'failed', 'message': 'record does not exist'}
    return HttpResponse(json.dumps(response_data), content_type="application/json")


@login_required(login_url='/login')
def thread_page(request, course_id, thread_id):
    course = Course.objects.get(id=course_id)

    try:
        thread = CourseDiscussionThread.objects.get(
            course=course,
            thread_id=thread_id
        )
    except CourseDiscussionThread.DoesNotExist:
        thread = None

    return render(request, 'course/discussion/posts_view.html', {
        'course': course,
        'thread': thread,
        'user': request.user,
        'tab': 'thread',
        'HAS_ADVERTISMENT': settings.APPLICATION_HAS_ADVERTISMENT,
        'local_css_urls': settings.SB_ADMIN_2_CSS_LIBRARY_URLS,
        'local_js_urls': settings.SB_ADMIN_2_JS_LIBRARY_URLS,
    })


@login_required(login_url='/login')
def posts_table(request, course_id, thread_id):
    course = Course.objects.get(id=course_id)

    try:
        thread = CourseDiscussionThread.objects.get(
            course=course,
            thread_id=thread_id
        )
    except CourseDiscussionThread.DoesNotExist:
        thread = None

    return render(request, 'course/discussion/posts_table.html', {
        'course': course,
        'thread': thread,
        'user': request.user,
    })


@login_required(login_url='/login')
def new_post_modal(request, course_id, thread_id):
    course = Course.objects.get(id=course_id)
    thread = CourseDiscussionThread.objects.get(
        course=course,
        thread_id=thread_id
    )
    form = CourseDiscussionPostForm()
    return render(request, 'course/discussion/new_post_modal.html', {
        'course': course,
        'form': form,
        'thread': thread,
        'user': request.user,
    })


@login_required(login_url='/login')
def insert_post(request, course_id, thread_id):
    response_data = {'status': 'failed', 'message': 'unknown error detected.'}
    if request.is_ajax():
        if request.method == 'POST':
            course = Course.objects.get(id=course_id)
            thread = CourseDiscussionThread.objects.get(
                course=course,
                thread_id=thread_id
            )
            form = CourseDiscussionPostForm(request.POST)
            form.instance.user = request.user
            form.instance.course = course
            if form.is_valid():
                form.save()
                thread.posts.add(form.instance)
                response_data = {'status': 'success', 'message': 'submitted'}
            else:
                response_data = {'status': 'failed', 'message': json.dumps(form.errors)}
    return HttpResponse(json.dumps(response_data), content_type="application/json")
