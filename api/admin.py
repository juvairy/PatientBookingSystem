from django.contrib import admin
from api.models import Department,DoctorProfile,Appointment,PatientProfile

admin.site.register(Department)
admin.site.register(DoctorProfile)
admin.site.register(Appointment)
admin.site.register(PatientProfile)

# Register your models here.
