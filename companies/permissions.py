from operator import truediv

from rest_framework import permissions
from rest_framework.views import Request, View

from .models import Company


class IsCompanyOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, company: Company):
        if request.user.is_company:
            return True

        if request.user.id == company.id:
            return True

        if request.user.is_superuser:
            return True


class IsCompanyOrAdmin(permissions.BasePermission):
    def has_permission(self, request: Request, view: View):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_company or request.user.is_superuser
