from django.db import models

# Create your models here.
from django.db import models

class Registration(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    TRAINING_MODE_CHOICES = [
        ('online', 'Live online'),
        ('classroom', 'Classroom'),
    ]
    
    LOCATION_CHOICES = [
        ('technopark', 'Technopark TVM'),
        ('thampanoor', 'Thampanoor TVM'),
        ('kochi', 'Kochi'),
        ('nagercoil', 'Nagercoil'),
        ('online', 'Online'),
    ]
    
    TIME_SLOT_CHOICES = [
        ('8am_10am', 'Between 8am - 10am'),
        ('9am_1pm', 'Between 9am - 1pm'),
        ('1pm_6pm', 'Between 1pm - 6pm'),
        ('6pm_10pm', 'Between 6pm - 10pm'),
    ]
    
    # Fields in the form
    full_name = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    educational_qualification = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)
    email = models.EmailField()
    guardian_mobile = models.CharField(max_length=15, blank=True, null=True)
    training_mode = models.CharField(max_length=10, choices=TRAINING_MODE_CHOICES)
    location = models.CharField(max_length=50, choices=LOCATION_CHOICES)
    guardian_name = models.CharField(max_length=100, blank=True, null=True)
    guardian_occupation = models.CharField(max_length=100, blank=True, null=True)
    preferred_training_time = models.CharField(max_length=20, choices=TIME_SLOT_CHOICES)
    address = models.TextField(blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    pin_code = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.full_name
