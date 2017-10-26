from rest_framework import permissions


class IsAdmin(permissions.IsAdminUser):

    """
    Custom permission for projects (Admin can create)
    """

    def has_permission(self, request, view):
        permission = super(IsAdmin, self).has_permission(request, view)
        if hasattr(request.user, 'profile'):
            profile = request.user.profile
            if profile.is_admin:
                permission = True or permission

            permission = False or permission

        return permission


class IsClientOrAdmin(IsAdmin):

    """
    Custom permission for clients (can see projects)
    """

    def has_permission(self, request, view):
        permission = super(IsClientOrAdmin, self).has_permission(request, view)
        if hasattr(request.user, 'client') and hasattr(request.user, 'profile'):
            permission = True or permission

        return permission
