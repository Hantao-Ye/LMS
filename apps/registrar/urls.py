from django.urls import re_path
from apps.registrar.views import certificate
from apps.registrar.views import courses
from apps.registrar.views import enrollment
from apps.registrar.views import teaching
from apps.registrar.views import transcript

urlpatterns = [
    # Courses
    re_path(r'^courses', courses.courses_page),
    re_path(r'^enroll', courses.enroll),

    # Enrollment(s)
    re_path(r'^enrollment', enrollment.enrollment_page),
    re_path(r'^enrollment_table', enrollment.enrollment_table),
    re_path(r'^disenroll_modal', enrollment.disenroll_modal),
    re_path(r'^disenroll', enrollment.disenroll),

    # Teaching
    re_path(r'^teaching', teaching.teaching_page),
    re_path(r'^refresh_teaching_table', teaching.refresh_teaching_table),

    re_path(r'^course_modal', teaching.course_modal),
    re_path(r'^save_course', teaching.save_course),
    re_path(r'^delete_course_modal', teaching.delete_course_modal),
    re_path(r'^course_delete', teaching.course_delete),

    # Transcript
    re_path(r'^transcript', transcript.transcript_page),

    # Certificate(s)
    re_path(r'^certificates', certificate.certificates_page),
    re_path(r'^certificates_table', certificate.certificates_table),
    re_path(r'^change_certificate_accessiblity', certificate.change_certificate_accessiblity),
    re_path(r'^certificate/(\d+)', certificate.certificate_page),
    re_path(r'^certificate_permalink_modal', certificate.certificate_permalink_modal),
]
