from rest_framework_recursive.fields import RecursiveField
from rest_framework import serializers

from edu_web.models import Students, Groups, Discipline, Direction, Curator


class CuratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curator
        fields = ('first_name', 'middle_name', 'last_name')


class StudentsSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Students
        fields = "__all__"


class GroupsSerializer(serializers.ModelSerializer):
    # num_student = serializers.IntegerField()
    # num_student_f = serializers.IntegerField()
    # num_student_m = serializers.IntegerField()
    name = serializers.CharField()
    student = serializers.SlugRelatedField(slug_field='first_name', read_only=True, many=True)
    group = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)

    class Meta:
        model = Groups
        fields = ('curator', 'curator_id', 'group', 'id',
                  'max_number_students', 'num_groups', 'student',
                  # 'num_student', 'num_student_f', 'num_student_m',
                  'name',)




class DirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direction
        fields = "__all__"


class DisciplineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discipline
        fields = '__all__'


class RepDirectionSerializer(serializers.ModelSerializer):
    discipline = DisciplineSerializer(read_only=True, many=True)
    curator = CuratorSerializer(read_only=True)

    class Meta:
        model = Direction
        fields = ("id", "name_dir", "curator", "discipline",)

class RepGroupsSerializer(serializers.ModelSerializer):
    free_place = serializers.IntegerField()
    num_student = serializers.IntegerField()
    num_student_f = serializers.IntegerField()
    num_student_m = serializers.IntegerField()
    name = serializers.CharField()
    curator = CuratorSerializer(read_only=True)

    student = serializers.SlugRelatedField(slug_field='first_name', read_only=True, many=True)
    group = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)

    class Meta:
        model = Groups
        fields = ('curator', 'curator_id', 'group', 'id',
                  'max_number_students', 'num_groups', 'student',
                  'num_student', 'num_student_f', 'num_student_m',
                  'name', 'free_place')
