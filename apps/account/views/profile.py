import json

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from apps.account.forms import UserForm


@login_required(login_url='/login')
def profile_page(request):
    return render(request, 'account/profile/view.html', {
        'user': request.user,
        'form': UserForm(instance=request.user),
        'tab': 'profile',
        'local_css_urls': settings.SB_ADMIN_2_CSS_LIBRARY_URLS,
        'local_js_urls': settings.SB_ADMIN_2_JS_LIBRARY_URLS,
    })


@login_required()
def update_user(request):
    response_data = {
        'status': 'failed',
        'message': 'unknown deletion error'
    }

    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
        if request.method == 'POST':
            form = UserForm(instance=request.user, data=request.POST)
            if form.is_valid():
                form.instance.username = form.instance.email
                form.save()
                response_data = {'status': 'success', 'message': 'updated user'}
            else:
                response_data = {'status': 'failed', 'message': json.dumps(form.errors)}
    return HttpResponse(json.dumps(response_data), content_type="application/json")
