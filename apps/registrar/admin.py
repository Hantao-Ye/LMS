from django.contrib import admin

## Special Thanks:
## http://www.djangobook.com/en/2.0/chapter06.html
#
from apps.registrar.models import FileUpload
from apps.registrar.models import Course
from apps.registrar.models import CourseSubmission
from apps.registrar.models import CourseDiscussionPost
from apps.registrar.models import CourseDiscussionThread
from apps.registrar.models import CourseSetting
from apps.registrar.models import CourseFinalMark
from apps.registrar.models import Announcement
from apps.registrar.models import Syllabus
from apps.registrar.models import Policy
from apps.registrar.models import Lecture
from apps.registrar.models import Assignment
from apps.registrar.models import AssignmentSubmission
from apps.registrar.models import Exam
from apps.registrar.models import ExamSubmission
from apps.registrar.models import Quiz
from apps.registrar.models import QuizSubmission
from apps.registrar.models import EssayQuestion
from apps.registrar.models import EssaySubmission
from apps.registrar.models import MultipleChoiceQuestion
from apps.registrar.models import MultipleChoiceSubmission
from apps.registrar.models import TrueFalseQuestion
from apps.registrar.models import TrueFalseSubmission
from apps.registrar.models import ResponseQuestion
from apps.registrar.models import ResponseSubmission
from apps.registrar.models import PeerReview

admin.site.register(FileUpload)
admin.site.register(Course)
admin.site.register(CourseSubmission)
admin.site.register(CourseDiscussionPost)
admin.site.register(CourseDiscussionThread)
admin.site.register(CourseSetting)
admin.site.register(CourseFinalMark)
admin.site.register(Announcement)
admin.site.register(Syllabus)
admin.site.register(Policy)
admin.site.register(Lecture)
admin.site.register(Assignment)
admin.site.register(AssignmentSubmission)
admin.site.register(Exam)
admin.site.register(ExamSubmission)
admin.site.register(Quiz)
admin.site.register(QuizSubmission)
admin.site.register(PeerReview)
admin.site.register(EssayQuestion)
admin.site.register(EssaySubmission)
admin.site.register(MultipleChoiceQuestion)
admin.site.register(MultipleChoiceSubmission)
admin.site.register(TrueFalseQuestion)
admin.site.register(TrueFalseSubmission)
admin.site.register(ResponseQuestion)
admin.site.register(ResponseSubmission)