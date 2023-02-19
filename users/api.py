from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from dotenv import load_dotenv
import os 
from twilio.rest import Client

from random import randint

from .models import User
from .serializers import UserSerializer

load_dotenv()

account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
my_phone_number = os.environ.get('PHONE_NUMBER')
sid = os.environ.get('SID')

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_throttles(self):
        if self.action == 'update':
            # twilio credentials

            # aca decimos que use el throttle scope 
            self.throttle_scope = 'generate_code'

        return super().get_throttles()

    def update(self, request: Request, pk):
        code = randint(1000, 9999)
        user = User.objects.get(pk=pk)
        # si queremos aumentar datos al request tenemos que hacerlo mutable
        request.data._mutable = True
        request.data['code'] = code 
        serializer = UserSerializer(instance=user, data=request.data)
        
        if serializer.is_valid():
            # enviar el sms
            client = Client(account_sid, auth_token)
            message = client.messages.create(
                messaging_service_sid=sid,
                body=f'Your code: {code}',
                to=my_phone_number
            )

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewGenericViewSet(RetrieveModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'
    
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)