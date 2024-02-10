from rest_framework import permissions

class advertiseronly(permissions.BasePermission):


    def has_permission(self, request,view,*args, **kwargs):

      try:
        return  request.user['group']=='advertiser'
      except:
         return False




