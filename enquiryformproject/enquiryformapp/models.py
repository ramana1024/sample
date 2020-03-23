from django.db import models
from multiselectfield import MultiSelectField
class EnquiryData(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    mobile=models.BigIntegerField()
    COURSES_CHOICES=(
        ('python','PYTHON'),
        ('django','DJANGO'),
        ('UI','UI'),
        ('Rest Api','REST API')
    )
    courses=MultiSelectField(max_length=100,choices=COURSES_CHOICES)
    TRSINERS_CHOICES=(
        ('narayana','NARAYANA'),
        ('Srinivas','SRINIVAS'),
        ('mohan reddy','MOHAN REDDY'),
        ('wilson','WILSON')
    )
    trainers=MultiSelectField(max_length=100,choices=TRSINERS_CHOICES)
    SHIFTS_CHOICES=(
        ('Morning','MORNING'),
        ('evening','EVENING'),
        ('night','NIGHT')
    )
    shifts=MultiSelectField(max_length=100,choices=SHIFTS_CHOICES)
    LOCATIONS_CHOICES=(
        ('ameerpet','AMEERPET'),
        ('madhapur','MADHAPUR'),
        ('KPHB','KPHB')
    )
    location=MultiSelectField(max_length=100,choices=LOCATIONS_CHOICES)
    start_date=models.DateField(max_length=100)
    gender=models.CharField(max_length=100)

