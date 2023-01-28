from django.db import models
from rest_framework import serializers
import uuid
# Create your models here.

class Patient(serializers.Serializer):
    user_id = serializers.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = serializers.CharField(max_length=100)
    phone_number = serializers.IntegerField()
    pin_code = serializers.IntegerField(default=None)
    city = serializers.CharField(max_length=50, default=None)


class FamilyMember(serializers.Serializer):
    family_id = serializers.UUIDField(default=uuid.uuid4, editable=False)
    patient_fam = serializers.ForeignKey(Patient, on_delete=models.CASCADE)

    fam_name1 = serializers.CharField(max_length=100)
    fam_number1 = serializers.IntegerField()

    fam_name2 = serializers.CharField(max_length=100, default=None, null=True)
    fam_number2 = serializers.IntegerField(default=None, null=True)

    fam_name3 = serializers.CharField(max_length=100, default=None, null=True)
    fam_number3 = serializers.IntegerField(default=None, null=True)


class Doctor(serializers.Serializer):
    doctor_id = serializers.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient_doc = serializers.ForeignKey(Patient, on_delete=models.CASCADE)

    doc_name1 = serializers.CharField(max_length=100)
    doc_number1 = serializers.IntegerField()

    doc_name2 = serializers.CharField(max_length=100, default=None, null=True)
    doc_number2 = serializers.IntegerField(default=None, null=True)

    doc_name3 = serializers.CharField(max_length=100, default=None, null=True)
    doc_number3 = serializers.IntegerField(default=None, null=True)


class Medicine(serializers.Serializer):
    med_id = serializers.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patiend_med = serializers.ForeignKey(Patient, on_delete=models.CASCADE)

    med_name1 = serializers.CharField(max_length=255, default=None, null=True)
    med_time1 = serializers.CharField(max_length=255)
    duration1 = serializers.CharField(max_length=255)
    days1 = serializers.CharField(max_length=255)

    med_name2 = serializers.CharField(max_length=255, default=None, null=True)
    med_time2 = serializers.CharField(max_length=255, default=None, null=True)
    duration2 = serializers.CharField(max_length=255, default=None, null=True)
    days2 = serializers.CharField(max_length=255, default=None, null=True)

    med_name3 = serializers.CharField(max_length=255, default=None, null=True)
    med_time3 = serializers.CharField(max_length=255, default=None, null=True)
    duration3 = serializers.CharField(max_length=255, default=None, null=True)
    days3 = serializers.CharField(max_length=255, default=None, null=True)

    med_name4 = serializers.CharField(max_length=255, default=None, null=True)
    med_time4 = serializers.CharField(max_length=255, default=None, null=True)
    duration4 = serializers.CharField(max_length=255, default=None, null=True)
    days4 = serializers.CharField(max_length=255, default=None, null=True)

    med_name5 = serializers.CharField(max_length=255, default=None, null=True)
    med_time5 = serializers.CharField(max_length=255, default=None, null=True)
    duration5 = serializers.CharField(max_length=255, default=None, null=True)
    days5 = serializers.CharField(max_length=255, default=None, null=True)

    med_name6 = serializers.CharField(max_length=255, default=None, null=True)
    med_time6 = serializers.CharField(max_length=255, default=None, null=True)
    duration6 = serializers.CharField(max_length=255, default=None, null=True)
    days6 = serializers.CharField(max_length=255, default=None, null=True)

    med_name7 = serializers.CharField(max_length=255, default=None, null=True)
    med_time7 = serializers.CharField(max_length=255, default=None, null=True)
    duration7 = serializers.CharField(max_length=255, default=None, null=True)
    days7 = serializers.CharField(max_length=255, default=None, null=True)

    med_name8 = serializers.CharField(max_length=255, default=None, null=True)
    med_time8 = serializers.CharField(max_length=255, default=None, null=True)
    duration8 = serializers.CharField(max_length=255, default=None, null=True)
    days8 = serializers.CharField(max_length=255, default=None, null=True)

    med_name9 = serializers.CharField(max_length=255, default=None, null=True)
    med_time9 = serializers.CharField(max_length=255, default=None, null=True)
    duration9 = serializers.CharField(max_length=255, default=None, null=True)
    days9 = serializers.CharField(max_length=255, default=None, null=True)

    med_name10 = serializers.CharField(max_length=255, default=None, null=True)
    med_time10 = serializers.CharField(max_length=255, default=None, null=True)
    duration10 = serializers.CharField(max_length=255, default=None, null=True)
    days10 = serializers.CharField(max_length=255, default=None, null=True)

    med_name11 = serializers.CharField(max_length=255, default=None, null=True)
    med_time11 = serializers.CharField(max_length=255, default=None, null=True)
    duration11 = serializers.CharField(max_length=255, default=None, null=True)
    days11 = serializers.CharField(max_length=255, default=None, null=True)

    med_name12 = serializers.CharField(max_length=255, default=None, null=True)
    med_time12 = serializers.CharField(max_length=255, default=None, null=True)
    duration12 = serializers.CharField(max_length=255, default=None, null=True)
    days12 = serializers.CharField(max_length=255, default=None, null=True)

    med_name13 = serializers.CharField(max_length=255, default=None, null=True)
    med_time13 = serializers.CharField(max_length=255, default=None, null=True)
    duration13 = serializers.CharField(max_length=255, default=None, null=True)
    days13 = serializers.CharField(max_length=255, default=None, null=True)

    med_name14 = serializers.CharField(max_length=255, default=None, null=True)
    med_time14 = serializers.CharField(max_length=255, default=None, null=True)
    duration14 = serializers.CharField(max_length=255, default=None, null=True)
    days14 = serializers.CharField(max_length=255, default=None, null=True)

    med_name15 = serializers.CharField(max_length=255, default=None, null=True)
    med_time15 = serializers.CharField(max_length=255, default=None, null=True)
    duration15 = serializers.CharField(max_length=255, default=None, null=True)
    days15 = serializers.CharField(max_length=255, default=None, null=True)


class Ailment(serializers.Serializer):
    ailment_id = serializers.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient_ailment = serializers.ForeignKey(Patient, on_delete=models.CASCADE)
    ailment_name = serializers.CharField(max_length=150)
    ailment_sub_type = serializers.CharField(max_length=150, default=None, null=True)


class Hospital(serializers.Serializer):
    hos_id = serializers.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient_hos = serializers.ForeignKey(Patient, on_delete = models.CASCADE)

    hos_name1 = serializers.CharField(max_length=255)
    hos_number1 = serializers.IntegerField()

    hos_name2 = serializers.CharField(max_length=255, default=None, null=True)
    hos_number2 = serializers.IntegerField(default=102)

    hos_name2 = serializers.CharField(max_length=255, default=None, null=True)
    hos_number2 = serializers.IntegerField(default=102)


    hos_name3 = serializers.CharField(max_length=255, default=None)
    hos_number3 = serializers.IntegerField(default=102)


class Chemist(serializers.Serializer):
    chemist_id = serializers.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient_chemist = serializers.ForeignKey(Patient, on_delete=models.CASCADE)

    chemist_name1 = serializers.CharField(max_length=255)
    chemist_number1 = serializers.IntegerField()

    chemist_name2 = serializers.CharField(max_length=255, default=None)
    chemist_number2 = serializers.IntegerField(default=None)

    chemist_name3 = serializers.CharField(max_length=255, default=None)
    chemist_number3 = serializers.IntegerField(default=None)


class Lab(serializers.Serializer):
    lab_id = serializers.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient_lab = serializers.ForeignKey(Patient, on_delete=models.CASCADE)

    lab_name1 = serializers.CharField(max_length=255)
    lab_number1 = serializers.IntegerField()

    lab_name2 = serializers.CharField(max_length=255, default=None)
    lab_number2 = serializers.IntegerField(default=None)


class Ambulance(serializers.Serializer):
    ambulance_id = serializers.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient_ambulance = serializers.ForeignKey(Patient, on_delete=models.CASCADE)

    amb_name1 = serializers.CharField(max_length=255)
    amb_number1 = serializers.IntegerField()

    amb_name2 = serializers.CharField(max_length=255, default=None)
    amb_number2 = serializers.IntegerField(default=102)

    amb_name3 = serializers.CharField(max_length=255, default=None)
    amb_number3 = serializers.IntegerField(default=102)


# class UserPreferreds(models.Model):

    # p_family = models.ForeignKey(FamilyMember, on_delete=models.CASCADE)
    # p_hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    # p_lab = models.ForeignKey(Lab, on_delete=models.CASCADE)
    # p_chemist = models.ForeignKey(Chemist, on_delete=models.CASCADE)
    # p_doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    # p_amb = models.ForeignKey(Ambulance, on_delete=models.CASCADE)
