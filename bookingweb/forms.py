from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from api.models import DocLeave,DoctorProfile,PatientProfile,Appointment


class DoctorRegistrationForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["first_name","last_name","email","username","password"]
        widgets={
            "first_name":forms.TextInput(attrs={"class":"form-control"}),
            "last_name":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "username":forms.TextInput(attrs={"class":"form-control"}),
            "password":forms.PasswordInput(attrs={"class":"form-control"})
          

       }

class DoctorLoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput())


class DoctorProfileForm(forms.ModelForm):
    class Meta:
        model=DoctorProfile
        fields=["specialization","license_number","qualification","contact_number","bio","d_image","age","gender","is_active"]


class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput())

class PatientProfileForm(forms.ModelForm):
    class Meta:
        model=PatientProfile
        fields=["birth_date","age","bloodgroup","gender","addres","contact_number","p_image"]
    
        widgets = {
        'birth_date':forms.DateTimeInput(attrs={'type': 'date'})
    }
class PatientRegistrationForm(UserCreationForm):
      
       class Meta:
        model=User
        fields=["username","email","password1","password2"]
        widgets={
            "username":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "password1":forms.PasswordInput(attrs={"class":"form-control"}),
            "password2":forms.PasswordInput(attrs={"class":"form-control"})
          

       }


class AppointmentForm(forms.ModelForm):
    class Meta:
        model=Appointment
        fields=["doctor","appointment_date","appointment_reason"]
        widgets = {
        'appointment_date':forms.DateTimeInput(attrs={'type': 'date'})
        }
    
class DotorLeaveForm(forms.ModelForm):
    class Meta:
        model=DocLeave
        fields=["start_date","end_date"]
        widgets = {
        'start_date':forms.DateTimeInput(attrs={'type': 'date'}),
         'end_date':forms.DateTimeInput(attrs={'type': 'date'})
        }

