from rest_framework.authentication import TokenAuthentication 

class AuthenticateToken(TokenAuthentication):
    def authenticate_credentials(self, key):
        user,token,message = None,None,None
        model = self.get_model()
        try:
            token = model.objects.select_related('user').get(key=key)
            user = token.user
        except model.DoesNotExist:
            message = 'Token Invalido'
            
        if token is not None:
            if not token.user.is_active:
                message = 'Usuario inactivo o eliminado'

        return (user,token,message)