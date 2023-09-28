from rest_framework.urls import path
from rest_framework.routers import DefaultRouter
from api import views
from rest_framework.authtoken.views import ObtainAuthToken


routers=DefaultRouter()
routers.register("account/docuser",views.UserDoctorView,basename="doc_user")
routers.register("account/patientuser",views.UserDoctorView,basename="patient_user")
routers.register("patientuser/profile",views.PatientProfileView,basename="patient-profile")

urlpatterns = [
    path("token/",ObtainAuthToken.as_view(),name="user_token"),
]+routers.urls