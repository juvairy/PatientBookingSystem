from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import View
from django.urls import reverse_lazy
from django.views.generic import View,CreateView,TemplateView,ListView,UpdateView,FormView
from bookingweb.forms import DoctorRegistrationForm,User,DoctorProfileForm,DoctorLoginForm,LoginForm, PatientProfileForm,PatientRegistrationForm,AppointmentForm,DotorLeaveForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from api.models import Department,DocLeave,DoctorProfile, PatientProfile,Appointment
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator
from rest_framework import permissions,authentication
# Create your views here.
def sigin_required(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            return redirect("signin")
        else:
            return fn(request,*args,**kwargs)
    return wrapper

decs=[sigin_required,never_cache]

class IndexView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"index.html")

class DoctorHomeView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"doctor_home.html")

class AboutUsView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"about_us.html")

class ContactUsView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"contact_us.html")

class GalleryView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"gallery.html")

class PatientHomeView(View):
    def get(self,request,*args,**kwargs):
        department=Department.objects.all
        return render(request,"patient_home.html",{"department":department})
    
    

class DocterSignUpView(View):
    def get (self,request,*args,**kwargs):
        form=DoctorRegistrationForm
        return render (request,"doctor_register.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=DoctorRegistrationForm(request.POST)
        if form.is_valid():
            User.objects.create_superuser(**form.cleaned_data)
            messages.success(request,"Your registration have been done succesfully")
            return redirect("doctor_home")
        else:
            messages.error(request,"sorry!try again")
            return render(request,"doctor_register.html",{"forms":form})


class DoctorSignInView(FormView):
    template_name="doctor_login.html"
    form_class=DoctorLoginForm

    def post(self,request,*args,**kwargs):
        form=DoctorLoginForm(request.POST)

        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                return redirect("doctor_home")
            else:
                
                return render(request,"doctor_login.html",{"form":form})

class SignInView(FormView):
    template_name="patient_login.html"
    form_class=LoginForm

    def post(self,request,*args,**kwargs):
        form=DoctorLoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                return redirect("doctor_home")
            else:
                return render(request,"patient_login.html",{"form":form})


    
class DoctorProfileView(CreateView):
    form_class=DoctorProfileForm
    model=DoctorProfile
    template_name="doctor_profile.html"
    success_url=reverse_lazy("home")
    context_object_name="doctorprofile"

    def form_valid(self,form):
        form.instance.user=self.request.user     
        return super().form_valid(form)
# 
class Doctor_ProfilDetailView(View):
    def get(self,request,*args,**kwargs):
        qs=DoctorProfile.objects.filter(user=request.user)
        return render(request,"view_doctor.html",{"doctorprofile":qs})
    
    
class DoctorSignoutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect ("signindoc")

class PatientSignoutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect ("signin")

class SignInView(FormView):
    template_name="patient_login.html"
    form_class=LoginForm

    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                return redirect("patient_home")
            else:
                return render(request,"patient_login.html",{"form":self.form_class})



class PatientProfileView(CreateView):
    form_class=PatientProfileForm
    model=PatientProfile
    template_name="patient_profile.html"
    success_url=reverse_lazy("home")

    def form_valid(self,form):
        form.instance.user=self.request.user     
        return super().form_valid(form)

class Patient_ProfilDetailView(View):
    def get(self,request,*args,**kwargs):
        qs=PatientProfile.objects.all()
        return render(request,"view_patient.html",{"patientprofile":qs})

class PatientProfileUpdateView(UpdateView):
    model=PatientProfile
    form_class=PatientProfileForm
    template_name="patient_profileupdate.html"
    success_url=reverse_lazy("home")
    pk_url_kwarg="id"
    def form_valid(self,form):
        form.instance.user=self.request.user     
        return super().form_valid(form)

class PatientProfilDetailView(TemplateView):
    template_name="PatientProfilDetailView.html"
class PatientSignUp(CreateView):
    model=User
    form_class=PatientRegistrationForm
    template_name="patient_register.html"
    success_url=reverse_lazy("home")



@method_decorator(decs,name="dispatch")
# class BookAppointmentView(CreateView,TemplateView):
#     authentication_classes=[authentication.BasicAuthentication]
#     permission_classes=[permissions.IsAuthenticated]
#     model=Appointment
#     form_class=AppointmentForm
#     template_name="appointment.html"
#     success_url=reverse_lazy("patient_home")
class BookAppointmentView(View):
   
    def get(self,request,*args,**kwargs):
        form=AppointmentForm()
        qs=DocLeave.objects.all().order_by("-start_date")
        return render(request,"appointment.html",{"form":form,"doctorleave":qs})
    def post(self,request,*args,**kwargs):
        form=AppointmentForm(request.POST)
        if form.is_valid():
            form.instance.patient=self.request.user.patientprofile     #to give the user ,instance is used 
            form.save()
            messages.success(request,"Apointmentsubmitted")
            return redirect("patient_home")
        else:
            messages.success(request,"failed to create appointment")
            return render(request,"appointment.html",{"form":form})
    
    
    
    # def get(self,request,*args,**kwargs):
    #     qs=DocLeave.objects.all().order_by("-start_date")
    #     return render(request,"view_doctorleave.html",{"doctorleave":qs})
    #     return render(request,"view_doctorleave.html",{"doctorleave":qs,"form":value})
    
    
    

class View_AppointmentView(View):
    def get(self,request,*args,**kwargs):
        qs=Appointment.objects.filter(doctor=request.user.doctorprofile).order_by("-appointment_date")
        return render(request,"view_appointment.html",{"appointment":qs})
    

class DoctorLeaveView(CreateView):
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    model=DocLeave
    form_class=DotorLeaveForm
    template_name="doctor_leave.html"
    success_url=reverse_lazy("doctor_home")
    def form_valid(self,form):
        form.instance.doctor=self.request.user.doctorprofile
        return super().form_valid(form)
    

class View_DoctorLeaveView(View):
    def get(self,request,*args,**kwargs):
        qs=DocLeave.objects.all().order_by("-start_date")
        return render(request,"view_doctorleave.html",{"doctorleave":qs})
    