from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail
from .models import Register
from django.conf import settings
from .utils import extract_features,load_model
from .models import Features
from django import forms
from .models import FileUpload
from .forms import PEFileForm
from django.forms import fields
import time
from django.urls import reverse 
import re
from .models import FileUpload
import joblib

class UploadFileForm(forms.ModelForm):
    doc_file=forms.FileField()


    class Meta:
        model=FileUpload
        fields=['doc_file']




# def upload_and_scan(request):
#     if request.method == 'POST':
#         form = UploadFileFo


def homepage(request):
    return render(request,'home.html',{})



from django.contrib import messages
import time
import os

def upload_file(request):
    if request.method == 'POST':
        form = PEFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            allowed_extensions = ['.exe', '.dll', '.sys', '.ocx', '.scr']
            file_extension = os.path.splitext(uploaded_file.name)[1].lower()
            if file_extension not in allowed_extensions:
                messages.error(request, 'Unsupported file format. Please upload a .exe, .dll, .sys, .ocx, or .scr file.')
            else:
                form.save()
                time.sleep(1)
                return redirect(reverse('rocket') + '?next=' + reverse('check'))
        else:
            # If form is not valid, it means there are errors in form fields.
            # Here, you can handle those errors as per your requirements.
            # For instance, you can display the errors to the user.
            print(form.errors)
            messages.error(request, 'Form is not valid. Please check your input.')
    else:
        form = PEFileForm()
    return render(request, 'scan.html', {'form': form})




def check(request):
    latest_uploaded_file = FileUpload.objects.latest('uploaded_at')
    uploaded_file_path = latest_uploaded_file.file.path

    # Perform feature extraction on the latest uploaded file
    features = extract_features(uploaded_file_path)

    loaded_model = joblib.load('model.joblib')
    features_2d = [features]  
    prediction = loaded_model.predict(features_2d)

    # Save features to the database
    my_feature = Features()
    my_feature.ImageDirectoryEntrySecurity = features[0]
    my_feature.CheckSum = features[1]
    my_feature.SizeOfInitializedData = features[2]
    my_feature.SizeOfImage = features[3]
    my_feature.MajorLinkerVersion = features[4]
    my_feature.AddressOfEntryPoint = features[5]
    my_feature.SectionMinEntropy = features[6]
    my_feature.DirectoryEntryImportSize = features[7]
    my_feature.SectionMaxPhysical = features[8]
    my_feature.SectionMinVirtualSize = features[9]
    my_feature.SectionMaxPointerData = features[10]
    my_feature.e_lfanew = features[11]
    my_feature.DllCharacteristics = features[12]
    my_feature.DirectoryEntryImport = features[13]
    my_feature.ImageDirectoryEntryResource = features[14]
    my_feature.ImageDirectoryEntryImport = features[15]
    my_feature.DirectoryEntryExport = features[16]
    my_feature.SizeOfCode = features[17]
    my_feature.ImageBase = features[18]
    my_feature.SizeOfStackReserve = features[19]
    my_feature.save()

   
    if prediction == 0:
        prediction = 'malicious'
    else:
        prediction = 'non-malicious'

    file_name = latest_uploaded_file.file.name 
    file_extension = file_name.split('.')[-1] 
    upload_date = latest_uploaded_file.uploaded_at  
    upload_date_time = upload_date.time()  
    upload_date_date = upload_date.date()  

    # Pass file details to the template context
    context = {
        'prediction': prediction,
        'file_name': file_name,
        'file_extension': file_extension,
        'upload_date': upload_date_date,
        'upload_time': upload_date_time,  
    }

    # Render the template with the context
    return render(request, 'check.html', context)








def contactus(request):
    if request.method == "POST":
        fname = request.POST.get("name")
        femail = request.POST.get("email")
        fmessage = request.POST.get("message")
        query = Contact.objects.create(name=fname, email=femail, message=fmessage)
        query.save()
        messages.success(request, "Thanks for Reaching Us! We will get back to you soon...")
        # messages.info(request,"Thanks for Reaching Us! We will get back to you soon...")
        return redirect('contact') 

    return render(request, 'contact.html', {})

def contains_only_alphabets(name):
    return bool(re.match(r'^[a-zA-Z]+$', name))

def signup(request):
    if request.method == 'POST':
        fname = request.POST['name']
        femail = request.POST['email']
        fpassword = request.POST['password']
        fconfirm_password = request.POST['confirm_password']
        
        if fpassword != fconfirm_password:
            messages.warning(request, "Password don't match")
            return render(request, 'signup.html')
        
        if not contains_only_alphabets(fname):
            messages.error(request, "Username must contain only alphabetic characters")
            return render(request, 'signup.html')
        
        if not femail.endswith('@gmail.com') and not femail.endswith('@banasthali.in'):
            messages.warning(request, "Email must end with either @gmail.com or @banasthali.in")
            return render(request, 'signup.html')
        if not re.match(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*()-_+=\[\]{}|:;"\'<>,.?/~`])[0-9a-zA-Z!@#$%^&*()-_+=\[\]{}|:;"\'<>,.?/~`]{8,}$', fpassword):
            messages.error(request, "Your password is weak")
            return render(request, 'signup.html')
    
        if Register.objects.filter(email=femail).exists():
            messages.warning(request, "Email is taken")
            return render(request, 'signup.html')
        user = Register.objects.create(name=fname, email=femail, password=fpassword, confirm_password=fconfirm_password)
        send_registration_email(user)
        messages.success(request, "Account created successfully!")
        return redirect('scan')  
    else:
        return render(request, 'signup.html')
    #    return render(request, 'signup.html', {'info_message': info_message})


    

def send_registration_email(user):
     subject = 'Registration Confirmation'
     message = f'Dear {user.name},\n\nThank you for registering on our website!'
     from_email = 'purti3296@gmail.com'
     to_email = user.email
     send_mail(subject, message, from_email, [to_email])


def loginpage(request):
    if request.method=='POST':
        username=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']

        if Register.objects.filter(name=username,email=email,password=password).exists():
            messages.success(request, "Login successful!")
            return redirect('scan')
       

        else:
            
            messages.error(request, "Register yourself first!")
            return redirect('sign')
    return render(request,'login.html',{})


def help(request):
    return render(request,'help.html',{})

def about(request):
    return render(request,'about.html',{})

# def check(request):
#     return render(request,'check.html',{})


def rocket_page(request):
    # Add your rocket page logic here
    return render(request, 'rocket.html')

