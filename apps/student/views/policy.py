from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from apps.registrar.models import Course
from apps.registrar.models import Policy


# Developer Notes:
# (1) Templates
# https://docs.djangoproject.com/en/1.7/ref/templates
#
# (2) JSON
# https://docs.djangoproject.com/en/1.7/topics/serialization/


@login_required(login_url='/login')
def policy_page(request, course_id):
    course = Course.objects.get(id=course_id)
    try:
        policy = Policy.objects.get(course=course)
    except Policy.DoesNotExist:
        policy = None
    return render(request, 'course/policy/view.html', {
        'course': course,
        'user': request.user,
        'policy': policy,
        'tab': 'policy',
        'HAS_ADVERTISMENT': settings.APPLICATION_HAS_ADVERTISMENT,
        'local_css_urls': settings.SB_ADMIN_2_CSS_LIBRARY_URLS,
        'local_js_urls': settings.SB_ADMIN_2_JS_LIBRARY_URLS,
    })
