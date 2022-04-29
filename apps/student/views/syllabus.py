from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from apps.registrar.models import Course
from apps.registrar.models import Syllabus


# Developer Notes:
# (1) Templates
# https://docs.djangoproject.com/en/1.7/ref/templates
#
# (2) JSON
# https://docs.djangoproject.com/en/1.7/topics/serialization/


@login_required(login_url='/login')
def syllabus_page(request, course_id):
    course = Course.objects.get(id=course_id)
    try:
        syllabus = Syllabus.objects.get(course=course)
    except Syllabus.DoesNotExist:
        syllabus = None
    return render(request, 'course/syllabus/view.html', {
        'course': course,
        'syllabus': syllabus,
        'user': request.user,
        'tab': 'syllabus',
        'HAS_ADVERTISMENT': settings.APPLICATION_HAS_ADVERTISMENT,
        'local_css_urls': settings.SB_ADMIN_2_CSS_LIBRARY_URLS,
        'local_js_urls': settings.SB_ADMIN_2_JS_LIBRARY_URLS,
    })
