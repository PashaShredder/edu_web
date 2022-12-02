from rest_framework import serializers
from edu_web.models import Students, Groups, Discipline, Direction, Curator


class CuratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curator
        fields = (
            'first_name',
            'middle_name',
            'last_name',
            'phone_number',
            'mail_address'
        )


#

class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'


class GroupsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Groups
        fields = '__all__'


class DirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direction
        fields = '__all__'


class DisciplineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discipline
        fields = '__all__'


class RepDirectionSerializer(serializers.ModelSerializer):
    name_dir = serializers.CharField()
    directiondisciplines = DisciplineSerializer(read_only=True, many=True)
    curator = CuratorSerializer(read_only=True)

    class Meta:
        model = Direction
        fields = ('name_dir', 'directiondisciplines', 'curator',)


# class RepGroupsSerializer(serializers.ModelSerializer):
#     group_name = serializers.CharField()
#     direction = RepDirectionSerializer(read_only=True)
#     student = StudentsSerializer(read_only=True)
#     students = serializers.SlugRelatedField(slug_field='first_name', read_only=True, many=True)
#     group = serializers.SlugRelatedField(slug_field='name', read_only=True)
#
#     class Meta:
#         model = Groups
#         fields = '__all__'
#
