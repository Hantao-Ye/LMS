from django.shortcuts import render


def privacy_page(request):
    return render(request, 'offlandpage/page/privacy.html', {
        'tab': 'privacy',
        'local_css_urls': ["css/offlandpage.css",
                           "bower_components/bootstrap/dist/css/bootstrap.min.css"],
        'local_js_urls': ["bower_components/jquery/dist/jquery.min.js",
                          "bower_components/bootstrap/dist/js/bootstrap.min.js", ],
    })
