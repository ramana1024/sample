from django.shortcuts import render
from. models import EnquiryData
from. forms import EnquiryForm
def enquiry_view(request):
    if request.method=="POST":
        eform=EnquiryForm(request.POST)
        if eform.is_valid():
            name=eform.cleaned_data.get('name')
            mobile=eform.cleaned_data.get('mobile')
            email = eform.cleaned_data.get('email')
            courses = eform.cleaned_data.get('courses')
            trainers = eform.cleaned_data.get('trainers')
            shifts = eform.cleaned_data.get('shifts')
            location = eform.cleaned_data.get('location')
            start_date= eform.cleaned_data.get('start_date')
            gender= eform.cleaned_data.get('gender')
            data=EnquiryData(
                    name=name,
                    mobile=mobile,
                    email=email,
                    courses=courses,
                    trainers=trainers,
                    shifts=shifts,
                    location=location,
                    start_date=start_date,
                    gender=gender
            )
            data.save()
            eform=EnquiryForm()
            context={'form':eform}
            return render(request,'enquiryform.html',context)
    else:
        eform=EnquiryForm()
        context={'form':eform}
        return render(request,'enquiryform.html',context)


