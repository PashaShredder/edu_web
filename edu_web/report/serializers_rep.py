from rest_framework import serializers
from edu_web.models import Groups
from edu_web.serializers import RepDirectionSerializer, StudentsSerializer


class ReportSerializer(serializers.ModelSerializer):
    group_name = serializers.CharField()
    direction = RepDirectionSerializer(read_only=True)
    student = StudentsSerializer(read_only=True)
    students = serializers.SlugRelatedField(slug_field='first_name', read_only=True, many=True)
    group = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Groups
        fields = '__all__'
