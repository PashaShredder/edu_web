from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers


from edu_web import views
from edu_web.report import views_rep


router = routers.SimpleRouter()
router.register(r'disciplines', views.DisciplineAPIListDetail)
router.register(r'directions', views.DirectionAPIListDetail)
router.register(r'students', views.StudentsAPIListDetail)
router.register(r'groups', views.GroupsAPIListDetail)
router.register(r'curator', views.CuratorAPIListDetail)
router.register(r'report', views_rep.RepGroupsAPIListDetail)
router.register(r'rep-dir', views.RepDirectionAPIListDetail)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/drf-auth/', include('rest_framework.urls')),
    path('api/rep-task/',  views_rep.hello_world, name='api_view'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [
    path('api/', include(router.urls)),
    path('__debug__/', include('debug_toolbar.urls')),

]
