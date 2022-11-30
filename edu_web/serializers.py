from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from edu_web.models import Students, Groups, Discipline, Direction, Curator


class CuratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curator
        # fields= '__all__'
        fields = (
            'first_name',
            'middle_name',
            'last_name',
            'phone_number',
            'mail_address',
        )

#

class StudentsSerializer(serializers.ModelSerializer):
    #TODO:
    # это еще что у тебя нет юзера в модели студентов
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Students
        fields = (
            'first_name',
            'middle_name',
            'last_name',
            'free_place', #этого нет у студента эта што
            'num_student',#этого нет у студента эта што
            'num_student_f',#этого нет у студента эта што
            'num_student_m',#этого нет у студента эта што
        )


class GroupsSerializer(serializers.ModelSerializer):
    # num_student = serializers.IntegerField()
    # num_student_f = serializers.IntegerField()
    # num_student_m = serializers.IntegerField()
    name = serializers.CharField()

    # а имя какого студента из группы ты хочш показать? их там до 20 штук
    student = serializers.SlugRelatedField(slug_field='first_name', read_only=True, many=True)

    #ты в группе хочш сериализовать и показать name у группы связанной с этой? а, many, значит их еще и много
    group = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)

    class Meta:
        model = Groups
        fields = (
            'curator', #этого не должно быть у группы
            'curator_id',#этого не должно быть у группы
            'group',#этого не должно быть у группы
            'id',
            'max_number_students',
            'num_groups', #у группы номер групп?
            'student', # какой из 20
            # 'num_student',
            # 'num_student_f',
            # 'num_student_m',
            'name',
        )


class DirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direction
        fields = '__all__'


class DisciplineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discipline
        fields = '__all__'


class RepDirectionSerializer(serializers.ModelSerializer):
    dir = serializers.CharField(read_only=True)
    directiondisciplines = DisciplineSerializer(read_only=True, many=True)
    curator = CuratorSerializer(read_only=True)

    class Meta:
        model = Direction
        # fields = '__all__'
        fields = ('name_dir','dir','directiondisciplines','curator',)


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


#Паша страшно - вырубай
class RepGroupsSerializer(serializers.ModelSerializer):
    free_place = serializers.IntegerField()
    num_student = serializers.IntegerField()
    num_student_f = serializers.IntegerField()
    num_student_m = serializers.IntegerField()
    name = serializers.CharField()
    # curator = CuratorSerializer(read_only=True)
    direction = RepDirectionSerializer(read_only=True)
    directions = serializers.SlugRelatedField(slug_field='name_dir', read_only=True, many=True)
    # disciplines = serializers.SlugRelatedField(slug_field='name_dis', read_only=True, many=True)
    studygroup = serializers.SlugRelatedField(slug_field='first_name', read_only=True, many=True)
    group = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)

    class Meta:
        model = Groups
        # fields = '__all__'
        fields = ('name', 'group', 'num_groups','max_number_students',
                  'curator','free_place','num_student',
                  'num_student_f','num_student_m','studygroup',
                  'directions','direction',
                  )
        # read_only_fields = ('name_dir','directiondisciplines','dir',)
