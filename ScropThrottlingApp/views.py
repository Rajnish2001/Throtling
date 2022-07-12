from django.shortcuts import render
from throttleapp.models import User
from throttleapp.serializers import UserSerializer
from rest_framework.generics import ListAPIView,RetrieveAPIView,CreateAPIView,UpdateAPIView,DestroyAPIView
from rest_framework.throttling import ScopedRateThrottle
# Create your views here.

class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'viewstu'

class UserRetrive(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'viewstu'

class UserCreate(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'viewstu'


class UserUpdate(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'viewstu'


class UserDelete(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'viewstu'

