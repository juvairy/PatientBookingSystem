from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.

class Department(models.Model):
    department_name=models.CharField(max_length=200,unique=True)

    def __str__(self):
        return self.department_name

class DoctorProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="doctorprofile")
    specialization=models.ForeignKey(Department,on_delete=models.CASCADE)
    license_number=models.CharField(max_length=50)
    qualification=models.CharField(max_length=100)
    contact_number=models.CharField(max_length=20)
    bio=models.CharField(max_length=200)
    d_image=models.ImageField(upload_to="images",null=True,blank=True)
    is_active=models.BooleanField(default=False)
    age=models.PositiveIntegerField()
    options=(
    ("male","male"),
    ("female","female")
    )
    gender=models.CharField(max_length=10,choices=options,default="male")
    
    
    def __str__(self):
        return self.user.get_full_name()




class PatientProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="patientprofile")
    birth_date=models.DateField()
    age= models.PositiveIntegerField()
    bloodgroup=models.CharField(max_length=10)
    options=(
        ("male","male"),
        ("female","female")
    )
    gender=models.CharField(max_length=10,choices=options,default="male")
    addres=models.CharField(max_length=200)
    contact_number=models.CharField(max_length=20)
    p_image=models.ImageField(upload_to="images",null=True,blank=True)

    def __str__(self):
        return self.user.get_full_name()


class Appointment(models.Model):
    doctor=models.ForeignKey(DoctorProfile,on_delete=models.CASCADE)
    patient=models.ForeignKey(PatientProfile,on_delete=models.CASCADE)
    appointment_date=models.DateTimeField()
    appointment_reason=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together=('doctor','patient','appointment_date',)

    def __str__(self):
        return self.doctor.user.get_full_name()
    @property
    def doctor_patient(self):
         return PatientProfile.objects.filter(patient=self)

class DocLeave(models.Model):
    doctor=models.ForeignKey(DoctorProfile,on_delete=models.CASCADE,related_name='docleave')
    start_date=models.DateField()
    end_date=models.DateField()

class Review(models.Model):
    doctor=models.ForeignKey(DoctorProfile,on_delete=models.CASCADE)
    patient=models.ForeignKey(PatientProfile,on_delete=models.CASCADE)
    rating=models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
    comment=models.TextField(blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
  
    def __str__(self):
        return self.doctor.user.get_full_name()