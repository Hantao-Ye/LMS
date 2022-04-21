from django.contrib import admin

from apps.account.models import PrivateMessage
from apps.account.models import Student
from apps.account.models import Teacher

admin.site.register(PrivateMessage)
admin.site.register(Student)
admin.site.register(Teacher)
