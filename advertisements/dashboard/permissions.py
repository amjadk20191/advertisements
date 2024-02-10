from rest_framework import permissions

class adminonly(permissions.BasePermission):


    def has_permission(self, request,view,*args, **kwargs):

        try:

         return  request.user['group']=='admin'
        except:
          return False




