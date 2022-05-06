from rest_framework import serializers

from apps.account.models import Student
from apps.account.models import Teacher
from apps.account.models import PrivateMessage


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ['student_id']


class TeacherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Teacher
        fields = ['teacher_id']


class PrivateMessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PrivateMessage
        fields = ['id', 'to_address', 'from_address', 'title', 'text', 'sent_date']
