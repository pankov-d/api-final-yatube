from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Проверка прав пользователя (владельца)
    Если запрос отправляет автор поста или
    если отправлен GET запрос – возвращает True
    В остальных случаях – False
    """

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user)


class IsOwnerorAdminorReadOnly(permissions.BasePermission):
    """
    Проверка прав пользователя (владельца/админа)
    Если запрос отправляет автор поста/админ или
    если отправлен GET запрос – возвращает True
    В остальных случаях – False
    """
    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user
                or request.user.is_staff)
