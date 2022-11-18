from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers


from edu_web import views


router = routers.SimpleRouter()
router.register(r'disciplines', views.DisciplineAPIListDetail)
router.register(r'directions', views.DirectionAPIListDetail)
router.register(r'students', views.StudentsAPIListDetail)
router.register(r'groups', views.GroupsAPIListDetail)
router.register(r'curator', views.CuratorAPIListDetail)
router.register(r'rep-group', views.RepGroupsAPIListDetail)
router.register(r'rep-dir', views.RepDirectionAPIListDetail)
# router.register(r'api/rep/', views.hello_world, basename='rep')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/drf-auth/', include('rest_framework.urls')),
    path('api/rep/',  views.hello_world, name='api_view'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [
    path('api/', include(router.urls)),
]
