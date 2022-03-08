from django.shortcuts import render
from .serializers import UserProfileSerializer, UserTokenSerializer
from .authentication_mixins import Authentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from userprofile.models import UserProfile
from rest_framework.views import APIView
from django.contrib.sessions.models import Session
from datetime import datetime
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class Login(ObtainAuthToken):
    def get(self,request,*args, **kwargs):
        print("SSS")
        return Response({'message':'Ok'}, status.HTTP_200_OK)
    
    def post(self,request,*args,**kwargs):
        login_serializer = self.serializer_class(data = request.data, context = {'request':request})
        if login_serializer.is_valid():
            user = login_serializer.validated_data['user']
            token,created = Token.objects.get_or_create(user = user)
            user_serializer = UserTokenSerializer(user)
            userprofile = UserProfile.objects.get(user__username=user_serializer.data['username'])
            user_profile_serializer = UserProfileSerializer(userprofile)
            if userprofile.active:
                if created:
                    return Response({
                        'token': token.key,
                        'user': user_serializer.data,
                        'user_profile': user_profile_serializer.data,
                        'message': 'Inicio Exitóso',
                    }, status = status.HTTP_201_CREATED)
                else:
                    token.delete()
                    token = Token.objects.create(user = user)
                    return Response({
                        'token': token.key,
                        'user': user_serializer.data,
                        'user_profile': user_profile_serializer.data,
                        'message': 'Inicio Exitóso'
                    }, status = status.HTTP_201_CREATED)
                    # return Response(
                    #     {'error':'Usuario Ya tiene sesión activa', 'token':token.key}, status=status.HTTP_409_CONFLICT
                    # )
            else:
                return Response({'error':'Su usuario ha sido suspendido'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'error':'Usuario o contraseña incorrecta'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message':'Error Interno'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class Logout(APIView):
    def post(self,request,*args,**kwargs):
        token = request.GET.get('token', '1')
        token = Token.objects.filter(key = token).first()

        if token:
            user = token.user

            all_sessions = Session.objects.filter(expire_date__gte = datetime.now())
            if all_sessions.exists():
                for session in all_sessions:
                    session_data = session.get_decoded()
                    if user.id == int(session_data.get('_auth_user_id')):
                        session.delete()
            
            token.delete()

            session_message = 'Sesión cerrada'
            token_message = 'Token eliminado'
            return Response(
                {'session_message':session_message, 'token_message':token_message},
                status = status.HTTP_200_OK)
        else:
            return Response(
                {'error':'No se ha encontrado usuario con estas credenciales'},
                status = status.HTTP_400_BAD_REQUEST)