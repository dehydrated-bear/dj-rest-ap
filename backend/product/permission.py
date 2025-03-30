from rest_framework import permissions

class IsStaffEditorPermission(permissions.DjangoModelPermissions):

    def has_permissions(self,request,view):
        user=request.user  
        print(user.get_all_permissions())
        print("*.*")
        if user.is_staff:
            if user.has_perm("product.add_product"):#"appname.verb_modelname
                return True
            if user.has_perm("product.delete_product"):
                return True
            if user.has_perm("product.view_product"):
                return True
            if user.has_perm("product.change_product"):
                return True

            return False
        
        
      
        return False
    

