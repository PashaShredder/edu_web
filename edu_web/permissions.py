from rest_framework import permissions

from edu_web.models import Curator


class IsAdminOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_staff


class IsCuratorOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        #TODO тут бы дополнить чтот типа
        '''
        if type(obj) == Student:
            return obj.direction.curator.user == request.user
        elif type(obj) == Direction:
            return obj.curator.user == request.user
        итд
        а то как будто от балды написано, на допуск любого куратора куда угодно'''
        qs = Curator.objects
        qs = qs.filter(user=request.user)
        qs = qs.exists()
        return qs
