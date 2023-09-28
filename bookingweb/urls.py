from django.urls import path
from bookingweb import views
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path("",views.IndexView.as_view(),name="home"),
    path('admin/', admin.site.urls),
    path("doctorsignup",views.DocterSignUpView.as_view(),name="docter_register"),
    path("doctorlogin",views.DoctorSignInView.as_view(),name="signindoc"),
    path("doctorprofile",views.DoctorProfileView.as_view(),name="doctor-profile"),
    path("signout",views.DoctorSignoutView.as_view(),name="signout"),
    path("patientsignout",views.PatientSignoutView.as_view(),name="p_signout"),
    path("doctor_home",views.DoctorHomeView.as_view(),name="doctor_home"),
    path("patientlogin",views.SignInView.as_view(),name="signin"),
    path("patientprofile",views.PatientProfileView.as_view(),name="patient_profile"),
    #path("patientprofile-detail",views.PatientProfilDetailView.as_view(),name="patientprofile-detail"),
    path("view_patient",views.Patient_ProfilDetailView.as_view(),name="view_patient"),
    path("patientprofile-edit/<int:id>",views.PatientProfileUpdateView.as_view(),name="patientprofile-edit"),
    path('signup/',views.PatientSignUp.as_view(),name="patient_register"),
    path("patient_home",views.PatientHomeView.as_view(),name="patient_home"),
    path("about_us",views.AboutUsView.as_view(),name="about_us"),
    path("contact_us",views.ContactUsView.as_view(),name="contact_us"),
    path("gallery",views.GalleryView.as_view(),name="gallery"),
    path("appointment",views.BookAppointmentView.as_view(),name="appointment"),
    path("view_doctor",views.Doctor_ProfilDetailView.as_view(),name="view_doctor"),
    path("view_appointment",views.View_AppointmentView.as_view(),name="view_appointment"),
    path("doctor_Leave",views.DoctorLeaveView.as_view(),name="doctor_leave"),
    path("view_doctorleave",views.View_DoctorLeaveView.as_view(),name="view_doctorleave"),
    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
