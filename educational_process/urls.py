from django.contrib import admin
from django.urls import path, include
from rest_framework import routers


from edu_web import views


router = routers.SimpleRouter()
router.register(r'disciplines', views.AdminDisciplineAPIListDetail)
router.register(r'directions', views.AdminDirectionAPIListDetail)
router.register(r'students', views.CuratorStudentsAPIListDetail)
router.register(r'groups', views.CuratorGroupsAPIListDetail)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/drf-auth/', include('rest_framework.urls')),
]
urlpatterns += [
    path('api/', include(router.urls)),
]
