from django.contrib.auth.models import User
from api.models import Department,PatientProfile
from rest_framework import serializers


class UserDoctorSerializeers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['first_name','last_name','username','email','password']

    def create(self, validated_data):
        return User.objects.create_superuser(**validated_data)
    
class UserPatientSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['first_name','last_name','username','email','password']
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
class PatientProfileSerializer(serializers.ModelSerializer):
    user=UserPatientSerializer(read_only=True,many=False)
    class Meta:
        model=PatientProfile
        fields="__all__"