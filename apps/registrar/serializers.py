from rest_framework import serializers

from apps.registrar.models import *

class FileUploadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FileUpload
        fields = ['upload_id', 'type', 'title', 'description', 'upload_date', 'file']


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'title', 'sub_title', 'category', 'description', 'start_date', 'finish_date', 'finish_date', 'status', 'image']


class CourseSubmissionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CourseSubmission
        fields = ['review_id', 'status', 'from_submitter', 'from_reviewer', 'review_date', 'submission_date', 'course']


class CourseSettingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CourseSetting
        fields = ['settings_id', 'course', 'final_exam_percent', 'course_percent']


class CourseFinalMarkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CourseFinalMark
        fields = ['credit_id', 'percent', 'is_public', 'course']


class AnnouncementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Announcement
        fields = ['announcement_id', 'title', 'body', 'post_date', 'course']


class SyllabusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Syllabus
        fields = ['syllabus_id', 'file', 'course']


class PolicySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Policy
        fields = ['policy_id', 'file', 'course']


class LectureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lecture
        fields = ['lecture_id', 'lecture_num', 'week_num', 'title', 'description', 'youtube_url', 'vimeo_url', 'preferred_service', 'course', 'notes']


class ExamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Exam
        fields = ['exam_id', 'exam_num', 'title', 'description', 'start_date', 'due_date', 'worth', 'is_final', 'course']


class ExamSubmissionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ExamSubmission
        fields = ['submission_id', 'percent', 'earned_marks', 'total_marks', 'submission_date', 'is_finished', 'exam']


class QuizSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Quiz
        fields = ['quiz_id', 'quiz_num', 'title', 'description', 'start_date', 'due_date', 'worth', 'course']


class QuizSubmissionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = QuizSubmission
        fields = ['submission_id', 'percent', 'earned_marks', 'total_marks', 'submission_date', 'is_finished', 'quiz']


class AssignmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Assignment
        fields = ['assignment_id', 'assignment_num', 'title', 'description', 'start_date', 'due_date', 'worth', 'course']


class AssignmentSubmissionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AssignmentSubmission
        fields = ['submission_id', 'percent', 'earned_marks', 'total_marks', 'submission_date', 'is_finished', 'assignment']


class EssayQuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EssayQuestion
        fields = ['question_id', 'question_num', 'title', 'description', 'marks', 'question_type', 'assignment', 'quiz', 'exam']


class PeerReviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PeerReview
        fields = ['review_id', 'marks', 'text', 'date']


class EssaySubmissionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EssaySubmission
        fields = ['submission_id', 'file', 'submission_date', 'marks', 'question']


class MultipleChoiceQuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MultipleChoiceQuestion
        fields = ['question_id', 'question_num', 'title', 'description', 'marks', 'assignment', 'quiz', 'exam']


class MultipleChoiceSubmissionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MultipleChoiceSubmission
        fields = ['submission_id', 'marks', 'submission_date', 'question']


class TrueFalseQuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TrueFalseQuestion
        fields = ['question_id', 'question_num', 'title', 'description', 'marks', 'assignment','quiz', 'exam']


class TrueFalseSubmissionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TrueFalseSubmission
        fields = ['submission_id', 'answer', 'submission_date', 'marks', 'question']


class ResponseQuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ResponseQuestion
        fields = ['question_id', 'question_num', 'title', 'description', 'marks', 'assignment', 'quiz', 'exam']


class ResponseSubmissionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ResponseSubmission
        fields = ['submission_id', 'answer', 'submission_date', 'marks', 'question']
