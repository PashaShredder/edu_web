from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from edu_web.permissions import IsAdminOrReadOnly, IsCuratorOrReadOnly
from edu_web.models import Discipline, Direction, Students, Groups, Curator
from edu_web.serializers import DisciplineSerializer, DirectionSerializer, CuratorSerializer, StudentsSerializer, \
    GroupsSerializer, RepDirectionSerializer


class APIListPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 50


class DisciplineAPIListDetail(
    viewsets.ModelViewSet
):
    queryset = Discipline.objects.all()
    serializer_class = DisciplineSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = APIListPagination


class CuratorAPIListDetail(
    viewsets.ModelViewSet
):
    queryset = Curator.objects.all()
    serializer_class = CuratorSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = APIListPagination


class DirectionAPIListDetail(
    viewsets.ModelViewSet,
):
    queryset = Direction.objects.all()
    serializer_class = DirectionSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = APIListPagination


class StudentsAPIListDetail(
    viewsets.ModelViewSet
):
    queryset = Students.objects.all()

    serializer_class = StudentsSerializer
    permission_classes = (IsAdminOrReadOnly, IsCuratorOrReadOnly,)
    pagination_class = APIListPagination


class GroupsAPIListDetail(
    viewsets.ModelViewSet
):
    queryset = Groups.objects.all()
    serializer_class = GroupsSerializer
    permission_classes = (IsCuratorOrReadOnly,)
    pagination_class = APIListPagination


#
#
# class RepGroupsAPIListDetail(
#     viewsets.ModelViewSet
# ):
#     queryset = Groups.objects.select_related('direction__curator').\
#         annotate(
#         free_place=20 - Count('students'),
#         num_student=Count('students'),
#         num_student_f=Count('students', filter=Q(students__gender='F')),
#         num_student_m=Count('students', filter=Q(students__gender='M')),)
#
#     serializer_class = RepGroupsSerializer
#     permission_classes = (IsAdminOrReadOnly,)
#     pagination_class = APIListPagination

class RepDirectionAPIListDetail(
    viewsets.ModelViewSet,
):
    queryset = Direction.objects.prefetch_related('curator__user')
    serializer_class = RepDirectionSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = APIListPagination


# @api_view(["GET", ])
# def hello_world(request):
#     report_create.delay()
#     sleep(2)
#     return Response({"message": "Hello, world!"})
