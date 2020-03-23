from django import forms
from multiselectfield import MultiSelectFormField
class EnquiryForm(forms.Form):
    name=forms.CharField(
        label="Enter Your Name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'your name'

            }
        )
    )
    mobile= forms.IntegerField(
        label="Enter Your Number",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your mobile number'

            }
        )
    )
    email = forms.EmailField(
        label="Enter Your Email",
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your email id'

            }
        )
    )
    COURSES_CHOICES=(
        ('python','PYTHON'),
        ('django','DJANGO'),
        ('UI','UI'),
        ('Rest Api','REST API')
    )
    courses=MultiSelectFormField(choices=COURSES_CHOICES,label="Select Required Courses:")
    TRAINERS_CHOICES=(
        ('narayana','NARAYANA'),
        ('srinivas','SRINIVAS'),
        ('mohan reddy','MOHAN REDDY'),
        ('Wilson','WILSON')
        )
    trainers=MultiSelectFormField(choices=TRAINERS_CHOICES,label="Select Required Trainers:")
    SHIFTS_CHOICES=(
        ('Morning','MORNING'),
        ('evening','EVENING'),
        ('night','NIGHT')
    )
    shifts=MultiSelectFormField(choices=SHIFTS_CHOICES,label="Select Required Shift:")
    LOCATIONS_CHOICES=(
        ('ameerpet','AMEERPET'),
        ('madhapur','MADHAPUR'),
        ('KPHB','KPHB')
    )
    loction=MultiSelectFormField(choices=LOCATIONS_CHOICES,label="Select Required Loction:")
    GENDER_CHOICES=(
        ('male','MALE'),
        ('female','FEMALE')
    )
    gender=forms.ChoiceField(
        widget=forms.RadioSelect ,choices=GENDER_CHOICES,
        label="Select Your Gender:"
    )
    start_date=forms.DateField(
        widget=forms.SelectDateWidget(),
        label="Enter Your Comfortable Timings:"
    )

