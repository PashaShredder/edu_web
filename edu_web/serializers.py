from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from edu_web.models import Students, Groups, Discipline, Direction, Curator


class CuratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curator
        fields = ('first_name', 'middle_name', 'last_name','phone_number','mail_address')


class StudentsSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    free_place = serializers.IntegerField()
    num_student = serializers.IntegerField()
    num_student_f = serializers.IntegerField()
    num_student_m = serializers.IntegerField()
    class Meta:
        model = Students
        fields = ('first_name', 'middle_name', 'last_name',)


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
    direction = serializers.SlugRelatedField(slug_field='name_dir', read_only=True, many=True)
    class Meta:
        model = Direction
        fields = ('name_dir',)


class DisciplineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discipline
        fields = '__all__'


class RepDirectionSerializer(serializers.ModelSerializer):
    discipline = DisciplineSerializer(read_only=True, many=True)
    # curator = CuratorSerializer(read_only=True, many=True)

    class Meta:
        model = Direction
        # fields = "__all__"
        fields = ('name_dir','discipline',)

# class RepGroupsSerializer(serializers.ModelSerializer):
#     free_place = serializers.IntegerField()
#     num_student = serializers.IntegerField()
#     num_student_f = serializers.IntegerField()
#     num_student_m = serializers.IntegerField()
#     name = serializers.CharField()
#     curator = CuratorSerializer(read_only=True)
#
#     student = serializers.SlugRelatedField(slug_field='first_name', read_only=True, many=True)
#     group = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
#
#     class Meta:
#         model = Groups
#         fields = ('curator', 'curator_id', 'group', 'id',
#                   'max_number_students', 'num_groups', 'student',
#                   'num_student', 'num_student_f', 'num_student_m',
#                   'name', 'free_place')


class RepGroupsSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    curator = CuratorSerializer(read_only=True)
    students = StudentsSerializer(read_only=True)
    directions = DirectionSerializer(read_only=True)
    disciplines = serializers.SlugRelatedField(slug_field='name_dis', read_only=True, many=True)
    studygroup = serializers.SlugRelatedField(slug_field='first_name' ,read_only=True, many=True)
    group = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)

    class Meta:
        model = Groups
        fields = '__all__'

