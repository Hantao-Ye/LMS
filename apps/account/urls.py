from django.urls import path, re_path, include

from rest_framework.routers import DefaultRouter

from apps.account.views import donate
from apps.account.views import mail
from apps.account.views import profile
from apps.account.views import setting

from apps.account.views.viewset import StudentViewSet, TeacherViewSet, PrivateMessageViewSet

router = DefaultRouter()
router.register('student', StudentViewSet)
router.register('teacher', TeacherViewSet)
router.register('private-message', PrivateMessageViewSet)


urlpatterns = [
    # path('api/', include(router.urls), name='account'),
    re_path(r'^profile', profile.profile_page),
    re_path(r'^update_user', profile.update_user),
    re_path(r'^inbox', mail.mail_page),
    re_path(r'^send_private_message', mail.send_private_message),
    re_path(r'^view_private_message', mail.view_private_message),
    re_path(r'^delete_private_message', mail.delete_private_message),
    re_path(r'^settings', setting.settings_page),
    re_path(r'^update_password', setting.update_password),
    re_path(r'^donate', donate.donate_page, name='donate'),
]
