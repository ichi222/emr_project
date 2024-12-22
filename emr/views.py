from django.shortcuts import render, get_object_or_404, redirect
from .models import Patient, Treatment, MedicalImage
from .forms import TreatmentForm, MedicalImageForm

def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'emr/patient_list.html', {'patients': patients})

def treatment_list(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    treatments = patient.treatments.all().order_by('-performed_at')
    return render(request, 'emr/treatment_list.html', {'patient': patient, 'treatments': treatments})

def treatment_create(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    if request.method == 'POST':
        form = TreatmentForm(request.POST)
        if form.is_valid():
            treatment = form.save(commit=False)
            treatment.patient = patient
            treatment.save()
            return redirect('treatment_list', patient_id=patient.id)
    else:
        form = TreatmentForm()
    return render(request, 'emr/treatment_form.html', {'form': form, 'patient': patient})

def medical_image_list(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    images = patient.medical_images.all()
    return render(request, 'emr/medical_image_list.html', {'patient': patient, 'images': images})

def medical_image_upload(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    if request.method == 'POST':
        form = MedicalImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.patient = patient
            image.save()
            return redirect('medical_image_list', patient_id=patient.id)
    else:
        form = MedicalImageForm()
    return render(request, 'emr/medical_image_upload.html', {'form': form, 'patient': patient})
