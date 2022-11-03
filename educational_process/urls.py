
from django.contrib import admin
from django.urls import path, include
from edu_web.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/drf-auth/', include('rest_framework.urls')),
    path('api/admin/discipline/', AdminDisciplineAPIList.as_view()),
    path('api/admin/discipline/detail/<int:pk>/', AdminDisciplineAPIDetail.as_view()),
    path('api/admin/direction/', AdminDirectionAPIList.as_view()),
    path('api/admin/direction/detail/<int:pk>/', AdminDirectionAPIDetail.as_view()),
    path('api/curator/students/', CuratorStudentsAPIList.as_view()),
    path('api/curator/students/detail/<int:pk>/', CuratorStudentsAPIDetail.as_view()),
    path('api/groups/', CuratorGroupsAPIList.as_view()),
    path('api/curator/groups/detail/<int:pk>/', CuratorGroupsAPIDetail.as_view()),
    ]
