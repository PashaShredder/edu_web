from time import sleep
from turtle import delay

from django.db.models import Count, Q
from rest_framework import mixins, viewsets
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response

from edu_web.permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from edu_web.models import Discipline, Direction, Students, Groups, Curator, MyReport
from edu_web.serializers import DisciplineSerializer, DirectionSerializer, CuratorSerializer, StudentsSerializer, \
    GroupsSerializer, RepGroupsSerializer, RepDirectionSerializer
from edu_web.tasks import report_create


class APIListPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 50


class DisciplineAPIListDetail(
    viewsets.ModelViewSet
):
    queryset = Discipline.objects.all()
    serializer_class = DisciplineSerializer
    permission_classes = (IsOwnerOrReadOnly,)
    pagination_class = APIListPagination


class CuratorAPIListDetail(
    viewsets.ModelViewSet
):
    queryset = Curator.objects.all()
    serializer_class = CuratorSerializer
    permission_classes = (IsOwnerOrReadOnly,)
    pagination_class = APIListPagination


class DirectionAPIListDetail(
    viewsets.ModelViewSet,
):
    queryset = Direction.objects.all()
    serializer_class = DirectionSerializer
    permission_classes = (IsOwnerOrReadOnly,)
    pagination_class = APIListPagination


class StudentsAPIListDetail(
    viewsets.ModelViewSet
):
    queryset = Students.objects.all()

    serializer_class = StudentsSerializer
    permission_classes = (IsOwnerOrReadOnly,)
    pagination_class = APIListPagination


class GroupsAPIListDetail(
    viewsets.ModelViewSet
):
    queryset = Groups.objects.all()
    serializer_class = GroupsSerializer
    permission_classes = (IsOwnerOrReadOnly,)
    pagination_class = APIListPagination


class RepGroupsAPIListDetail(
    viewsets.ModelViewSet
):
    queryset = Groups.objects.annotate(
        free_place=20 - Count('student'),
        num_student=Count('student'),
        num_student_f=Count('student', filter=Q(student__gender='F')),
        num_student_m=Count('student', filter=Q(student__gender='M')),
    )
    serializer_class = RepGroupsSerializer
    permission_classes = (IsOwnerOrReadOnly,)
    pagination_class = APIListPagination


class RepDirectionAPIListDetail(
    viewsets.ModelViewSet,
):
    queryset = Direction.objects.all()
    serializer_class = RepDirectionSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = APIListPagination


@api_view(["GET",])
def hello_world(request):
    report_create.delay()
    sleep(2)
    return Response({"message": "Hello, world!"})
