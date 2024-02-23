from rest_framework import permissions


class IsAdminPermissions(permissions.BasePermission):

      #def has_permission(self, request, view):
      #      if request.method in permissions.SAFE_METHODS:
      #            return True


      def has_object_permission(self, request, view, obj):
            print('fgfggggggggggggg',request.user.is_staff)
            if request.user.is_staff:
                  return True
            elif request.method in permissions.SAFE_METHODS:
                  return True
            return False
                  
      