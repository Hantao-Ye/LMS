from django.conf import settings
from django.shortcuts import render


# Create your views here.
def donate_page(request):
    return render(request, 'account/donate/view.html', {
        'user': request.user,
        'tab': 'donate',
        'local_css_urls': settings.SB_ADMIN_2_CSS_LIBRARY_URLS,
        'local_js_urls': settings.SB_ADMIN_2_JS_LIBRARY_URLS,
    })
