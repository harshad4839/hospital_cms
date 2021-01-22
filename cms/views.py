from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import PatientForm, DignosisForm, DocterForm
from .models import Docter, Patient, Dignocis
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import send_mail


def home(request):
    return render(request, 'cms/home.html')

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'cms/signupuser.html', {'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('docterdetails')
            except IntegrityError:
                return render(request, 'cms/signupuser.html', {'form':UserCreationForm(), 'error':'That username has already been taken. Please choose a new username'})
        else:
            return render(request, 'cms/signupuser.html', {'form':UserCreationForm(), 'error':'Passwords did not match'})

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'cms/loginuser.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'cms/loginuser.html', {'form':AuthenticationForm(), 'error':'Username and password did not match'})
        else:
            login(request, user)
            return redirect('viewpatients')

@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')



@login_required
def patient(request):
    if request.method == 'GET':
        return render(request, 'cms/createpatient.html', {'form':PatientForm()})
    else:
        try:
            form = PatientForm(request.POST)
            newitem = form.save(commit=False)
            newitem.docters = request.user
            if form.is_valid():
                form.save()
            return redirect('docter')
        except ValueError:
            return render(request, 'cms/createpatient.html', {'form':PatientForm(), 'error':'Bad data passed in. Try again.'})



@login_required
def docter(request):
    if request.method == 'GET':
        return render(request, 'cms/createdignosis.html', {'form':DignosisForm()})
    else:
        try:
            form = DignosisForm(request.POST)
            newitem = form.save(commit=False)
            newitem.docter = request.user
            if form.is_valid():
                form.save()
            return redirect('viewpatients')
        # except ValueError:
        except Exception as e:
            print(str(e))
            return render(request, 'cms/createdignosis.html', {'form':DignosisForm(), 'error':str(e)})


@login_required
def docterdetails(request):
    if request.method == 'GET':
        return render(request, 'cms/docterdetails.html', {'form':DocterForm()})
    else:
        try:
            form = DocterForm(request.POST)
            newitem = form.save(commit=False)
            newitem.user = request.user
            if form.is_valid():
                form.save()
            user = request.user
            docter_details = Docter.objects.filter(user=user).first()

            print("user",user)
            subject = 'Welcome to our system  Docter '+str(docter_details.name)
            message = 'Hi thank you for registering Docter'+str(docter_details.name)+'     your username :   '+ str(user.username) +'        your password is :     '+ str(user.password)
            email_form = settings.EMAIL_HOST_USER
            recipient_list = [docter_details.email, ]
            send_mail(subject, message, email_form, recipient_list)

            print("email = ", recipient_list)
            return redirect('patient')
        # except ValueError:
        except Exception as e:
            print(str(e))
            return render(request, 'cms/docterdetails.html', {'form':DocterForm(), 'error':str(e)})



@login_required
def viewpatients(request):
    patients = Patient.objects.filter(docters=request.user)
    print("pateints", patients)
    return render(request, 'cms/currentpatients.html', {'patients': patients})
    # return render(request, 'cms/currentpatients.html', {'patients':patients})



@login_required
def patientlist(request, item_pk):
    item = get_object_or_404(Patient, pk=item_pk) #docter=request.user
    if request.method == 'GET':
        form = PatientForm(instance=item)
        return render(request, 'cms/patient.html', {'item':item, 'form':form})
    else:
        try:
            form = PatientForm(request.POST, instance=item)
            form.save()
            return redirect('viewpatients')
        except ValueError:
            return render(request, 'cms/patient.html', {'item':item, 'form':form, 'error':'Bad info'})

@login_required
def deleteitem(request, item_pk):
    patient_obj = Patient.objects.filter(id=item_pk)
    print("delete patient", patient_obj)
    obj_patient = patient_obj.first()
    print("delete obj patient = ", obj_patient)

    # item = get_object_or_404(Patient, pk=item_pk, docters=request.user)
    if patient_obj.exists():
        obj_patient = patient_obj.first()

        # if request.method == 'POST':

        obj_patient.delete()

        return redirect('viewpatients')
    # return HttpResponse("no patient in this id")
        # return redirect('currentitem')


@login_required
def patientdignosis(request, item_pk):
    # Dignocis_id = get_object_or_404(Dignocis, pk=item_pk) #docter=request.user
    obj_patient = Patient.objects.get(id=item_pk)
    dignocis_id = Dignocis.objects.filter(patient = obj_patient)
    if request.method == 'GET':
        # form = DignosisForm(instance=Dignocis_id)
        return render(request, 'cms/patientsymptoms.html', {'dignocis_id':dignocis_id})
