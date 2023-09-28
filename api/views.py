from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet,GenericViewSet
from api.serializers import UserDoctorSerializeers,UserPatientSerializer,PatientProfileSerializer
from django.contrib.auth.models import User
from rest_framework.mixins import CreateModelMixin
from api.models import Department,PatientProfile
from rest_framework import authentication,permissions
from rest_framework import serializers

# Create your views here.

class UserDoctorView(GenericViewSet,CreateModelMixin):
    serializer_class=UserDoctorSerializeers
    queryset=User.objects.all()

class UserPatientView(GenericViewSet,CreateModelMixin):
    serializer_class=UserPatientSerializer
    queryset=User.objects.all()

class PatientProfileView(ModelViewSet):
    serializer_class=PatientProfileSerializer
    queryset=PatientProfile.objects.all()
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user) 
    
    def destroy(self, request, *args, **kwargs):
        profile=self.get_object()
        if profile.user != request.user:
            raise serializers.ValidationError("not allowed to perform this method")
        else:
            return super().destroy(request,*args,**kwargs)