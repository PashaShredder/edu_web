from django.template.defaultfilters import first
from rest_framework import generics, request, mixins, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from edu_web.permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from edu_web.models import *
from edu_web.serializers import *


class APIListPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 20


class AdminDisciplineAPIListDetail(
    viewsets.ModelViewSet
):
    queryset = Discipline.objects.all()
    serializer_class = AdminDisciplineSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = APIListPagination


class AdminDirectionAPIListDetail(
    viewsets.ModelViewSet,
):
    queryset = Direction.objects.all()
    serializer_class = AdminDirectionSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = APIListPagination


class CuratorStudentsAPIListDetail(
    viewsets.ModelViewSet
):
    queryset = Students.objects.all()
    serializer_class = CuratorStudentsSerializer
    permission_classes = (IsOwnerOrReadOnly,)
    pagination_class = APIListPagination


class CuratorGroupsAPIListDetail(
    viewsets.ModelViewSet
):
    queryset = Groups.objects.all()
    serializer_class = CuratorGroupsSerializer
    permission_classes = (IsOwnerOrReadOnly,)
    pagination_class = APIListPagination
