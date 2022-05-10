from rest_framework import permissions

from users.models import User

class IsCandidate(permissions.IsAuthenticated):
    """
    Permissions to allow Candidates
    """

    def has_permission(self, req, view):
        user = req.user
        return allow_login(user, 'user') or allow_login(user, 'admin')

class IsHr(permissions.IsAuthenticated):
    """
    Permissions to allow HR of company
    """

    def has_permission(self, req, view):
        user = req.user
        return allow_login(user, 'hr') or allow_login(user, 'admin')

class IsAdmin(permissions.IsAuthenticated):
    """
    Permissions to allow Admin of Company
    """

    def has_permission(self, req, view):
        user = req.user
        return allow_login(user, 'admin')

def allow_login(user=None, role=''):
    if not hasattr(user, 'role'):
        return False
    if role!='user' and not (hasattr(user, role) and getattr(user, role).allow_login):
        return False
    if role=='user' and not hasattr(user, 'candidate'):
        return False
    if user.role == getattr(User.Roles, role.upper()):
        return True
    return False
