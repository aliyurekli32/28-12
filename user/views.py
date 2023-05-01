from .serializers import RegisterSerializer
from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView
from rest_framework.authtoken.models import Token

class RegisterView(CreateAPIView):
    queryset= User.objects.all()
    serializer_class = RegisterSerializer
    #create token
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        token = Token.objects.create(user_id=response.data['id'])
        response.data['token']=token.key
        print(response.data)
        return response

# Create your views here..


