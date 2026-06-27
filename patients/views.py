from django.shortcuts import render, redirect, get_object_or_404
from .models import Patient
from .forms import PatientForm
from .predictor import predict_health

# READ
def patient_list(request):
    patients = Patient.objects.all().order_by("-created_at")

    return render(
        request,
        "patients/index.html",
        {"patients": patients},
    )


# CREATE
def add_patient(request):

    if request.method == "POST":

        form = PatientForm(request.POST)

        if form.is_valid():

            patient = form.save(commit=False)

            patient.remarks = predict_health(
                patient.glucose,
                patient.haemoglobin,
                patient.cholesterol,
            )

            patient.save()

            return redirect("patient_list")

    else:
        form = PatientForm()

    return render(
        request,
        "patients/add_patient.html",
        {"form": form},
    )


# UPDATE
def edit_patient(request, pk):

    patient = get_object_or_404(Patient, pk=pk)

    if request.method == "POST":

        form = PatientForm(request.POST, instance=patient)

        if form.is_valid():

            patient = form.save(commit=False)

            patient.remarks = predict_health(
                patient.glucose,
                patient.haemoglobin,
                patient.cholesterol,
            )

            patient.save()

            return redirect("patient_list")

    else:
        form = PatientForm(instance=patient)

    return render(
        request,
        "patients/edit_patient.html",
        {
            "form": form,
            "patient": patient,
        },
    )


# DELETE
def delete_patient(request, pk):

    patient = get_object_or_404(Patient, pk=pk)

    if request.method == "POST":
        patient.delete()
        return redirect("patient_list")

    return render(
        request,
        "patients/delete_patient.html",
        {
            "patient": patient
        },
    )