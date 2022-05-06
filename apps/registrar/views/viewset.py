from rest_framework import viewsets

from apps.registrar.serializers import *


class FileUploadViewSet(viewsets.ModelViewSet):
    queryset = FileUpload.objects.all()
    serializer_class = FileUploadSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseSubmissionViewSet(viewsets.ModelViewSet):
    queryset = CourseSubmission.objects.all()
    serializer_class = CourseSubmissionSerializer


class CourseSettingViewSet(viewsets.ModelViewSet):
    queryset = CourseSetting.objects.all()
    serializer_class = CourseSettingSerializer


class CourseFinalMarkViewSet(viewsets.ModelViewSet):
    queryset = CourseFinalMark.objects.all()
    serializer_class = CourseFinalMarkSerializer


class AnnouncementViewSet(viewsets.ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer


class SyllabusViewSet(viewsets.ModelViewSet):
    queryset = Syllabus.objects.all()
    serializer_class = SyllabusSerializer


class PolicyViewSet(viewsets.ModelViewSet):
    queryset = Policy.objects.all()
    serializer_class = PolicySerializer


class LectureViewSet(viewsets.ModelViewSet):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer


class ExamViewSet(viewsets.ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer


class ExamSubmissionViewSet(viewsets.ModelViewSet):
    queryset = ExamSubmission.objects.all()
    serializer_class = ExamSubmissionSerializer


class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer


class QuizSubmissionViewSet(viewsets.ModelViewSet):
    queryset = QuizSubmission.objects.all()
    serializer_class = QuizSubmissionSerializer


class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer


class AssignmentSubmissionViewSet(viewsets.ModelViewSet):
    queryset = AssignmentSubmission.objects.all()
    serializer_class = AssignmentSubmissionSerializer


class EssayQuestionViewSet(viewsets.ModelViewSet):
    queryset = EssayQuestion.objects.all()
    serializer_class = EssayQuestionSerializer


class PeerReviewViewSet(viewsets.ModelViewSet):
    queryset = PeerReview.objects.all()
    serializer_class = PeerReviewSerializer


class EssaySubmissionViewSet(viewsets.ModelViewSet):
    queryset = EssaySubmission.objects.all()
    serializer_class = EssaySubmissionSerializer


class MultipleChoiceQuestionViewSet(viewsets.ModelViewSet):
    queryset = MultipleChoiceQuestion.objects.all()
    serializer_class = MultipleChoiceQuestionSerializer


class MultipleChoiceSubmissionViewSet(viewsets.ModelViewSet):
    queryset = MultipleChoiceSubmission.objects.all()
    serializer_class = MultipleChoiceSubmissionSerializer


class TrueFalseQuestionViewSet(viewsets.ModelViewSet):
    queryset = TrueFalseQuestion.objects.all()
    serializer_class = TrueFalseQuestionSerializer


class TrueFalseSubmissionViewSet(viewsets.ModelViewSet):
    queryset = TrueFalseSubmission.objects.all()
    serializer_class = TrueFalseSubmissionSerializer


class ResponseQuestionViewSet(viewsets.ModelViewSet):
    queryset = ResponseQuestion.objects.all()
    serializer_class = ResponseQuestionSerializer


class ResponseSubmissionViewSet(viewsets.ModelViewSet):
    queryset = ResponseSubmission.objects.all()
    serializer_class = ResponseSubmissionSerializer