from time import sleep

from django.db.models import Count, Q
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from edu_web.models import Groups
from edu_web.permissions import IsAdminOrReadOnly
from edu_web.report.serializers_rep import ReportSerializer
from edu_web.views import APIListPagination
from edu_web.report.tasks import report_create


class RepGroupsAPIListDetail(
    viewsets.ModelViewSet
):
    queryset = Groups.objects.select_related('direction__curator'). \
        annotate(
        free_place=20 - Count('students'),
        num_student=Count('students'),
        num_student_f=Count('students', filter=Q(students__gender='F')),
        num_student_m=Count('students', filter=Q(students__gender='M')), )

    serializer_class = ReportSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = APIListPagination


0


@api_view(["GET", ])
def hello_world(request):
    report_create.delay()
    sleep(2)
    return Response({"message": "Hello, world!"})
