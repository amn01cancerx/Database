from django.db import models
import uuid
# Create your models here.

class Patient(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    pin_code = models.IntegerField(default=None)
    city = models.CharField(max_length=50, default=None)

class FamilyMember(models.Model):
    family_id = models.UUIDField(default=uuid.uuid4, editable=False)
    patient_fam = models.ForeignKey(Patient, on_delete=models.CASCADE , null=True)

    fam_name1 = models.CharField(max_length=100)
    fam_number1 = models.IntegerField()

    fam_name2 = models.CharField(max_length=100, default=None, null=True)
    fam_number2 = models.IntegerField(default=None, null=True)

    fam_name3 = models.CharField(max_length=100, default=None, null=True)
    fam_number3 = models.IntegerField(default=None, null=True)


class Doctor(models.Model):
    doctor_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient_doc = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)

    doc_name1 = models.CharField(max_length=100)
    doc_number1 = models.IntegerField()

    doc_name2 = models.CharField(max_length=100, default=None, null=True)
    doc_number2 = models.IntegerField(default=None, null=True)

    doc_name3 = models.CharField(max_length=100, default=None, null=True)
    doc_number3 = models.IntegerField(default=None, null=True)

class Medicine(models.Model):
    med_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patiend_med = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)

    med_name1 = models.CharField(max_length=100, default=None, null=True)
    med_time1 = models.CharField(max_length=100)
    duration1 = models.CharField(max_length=100)
    days1 = models.CharField(max_length=100)

    med_name2 = models.CharField(max_length=100, default=None, null=True)
    med_time2 = models.CharField(max_length=100, default=None, null=True)
    duration2 = models.CharField(max_length=100, default=None, null=True)
    days2 = models.CharField(max_length=100, default=None, null=True)

    med_name3 = models.CharField(max_length=100, default=None, null=True)
    med_time3 = models.CharField(max_length=100, default=None, null=True)
    duration3 = models.CharField(max_length=100, default=None, null=True)
    days3 = models.CharField(max_length=100, default=None, null=True)

    med_name4 = models.CharField(max_length=100, default=None, null=True)
    med_time4 = models.CharField(max_length=100, default=None, null=True)
    duration4 = models.CharField(max_length=100, default=None, null=True)
    days4 = models.CharField(max_length=100, default=None, null=True)

    med_name5 = models.CharField(max_length=100, default=None, null=True)
    med_time5 = models.CharField(max_length=100, default=None, null=True)
    duration5 = models.CharField(max_length=100, default=None, null=True)
    days5 = models.CharField(max_length=100, default=None, null=True)

    med_name6 = models.CharField(max_length=100, default=None, null=True)
    med_time6 = models.CharField(max_length=100, default=None, null=True)
    duration6 = models.CharField(max_length=100, default=None, null=True)
    days6 = models.CharField(max_length=100, default=None, null=True)

    med_name7 = models.CharField(max_length=100, default=None, null=True)
    med_time7 = models.CharField(max_length=100, default=None, null=True)
    duration7 = models.CharField(max_length=100, default=None, null=True)
    days7 = models.CharField(max_length=100, default=None, null=True)

    med_name8 = models.CharField(max_length=100, default=None, null=True)
    med_time8 = models.CharField(max_length=100, default=None, null=True)
    duration8 = models.CharField(max_length=100, default=None, null=True)
    days8 = models.CharField(max_length=100, default=None, null=True)

    med_name9 = models.CharField(max_length=100, default=None, null=True)
    med_time9 = models.CharField(max_length=100, default=None, null=True)
    duration9 = models.CharField(max_length=100, default=None, null=True)
    days9 = models.CharField(max_length=100, default=None, null=True)

    med_name10 = models.CharField(max_length=100, default=None, null=True)
    med_time10 = models.CharField(max_length=100, default=None, null=True)
    duration10 = models.CharField(max_length=100, default=None, null=True)
    days10 = models.CharField(max_length=100, default=None, null=True)

    med_name11 = models.CharField(max_length=100, default=None, null=True)
    med_time11 = models.CharField(max_length=100, default=None, null=True)
    duration11 = models.CharField(max_length=100, default=None, null=True)
    days11 = models.CharField(max_length=100, default=None, null=True)

    med_name12 = models.CharField(max_length=100, default=None, null=True)
    med_time12 = models.CharField(max_length=100, default=None, null=True)
    duration12 = models.CharField(max_length=100, default=None, null=True)
    days12 = models.CharField(max_length=100, default=None, null=True)

    med_name13 = models.CharField(max_length=100, default=None, null=True)
    med_time13 = models.CharField(max_length=100, default=None, null=True)
    duration13 = models.CharField(max_length=100, default=None, null=True)
    days13 = models.CharField(max_length=100, default=None, null=True)

    med_name14 = models.CharField(max_length=100, default=None, null=True)
    med_time14 = models.CharField(max_length=100, default=None, null=True)
    duration14 = models.CharField(max_length=100, default=None, null=True)
    days14 = models.CharField(max_length=100, default=None, null=True)

    med_name15 = models.CharField(max_length=100, default=None, null=True)
    med_time15 = models.CharField(max_length=100, default=None, null=True)
    duration15 = models.CharField(max_length=100, default=None, null=True)
    days15 = models.CharField(max_length=100, default=None, null=True)


class Ailment(models.Model):
    ailment_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient_ailment = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)
    ailment_name = models.CharField(max_length=100)
    ailment_sub_type = models.CharField(max_length=100, default=None, null=True)


class Hospital(models.Model):
    hos_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient_hos = models.ForeignKey(Patient, on_delete = models.CASCADE, null=True)

    hos_name1 = models.CharField(max_length=100)
    hos_number1 = models.IntegerField()

    hos_name2 = models.CharField(max_length=100, default=None, null=True)
    hos_number2 = models.IntegerField(default=102)

    hos_name3 = models.CharField(max_length=100, default=None, null=True)
    hos_number3 = models.IntegerField(default=102)


class Chemist(models.Model):
    chemist_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient_chemist = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)

    chemist_name1 = models.CharField(max_length=100)
    chemist_number1 = models.IntegerField()

    chemist_name2 = models.CharField(max_length=100, default=None, null=True)
    chemist_number2 = models.IntegerField(default=None, null=True)

    chemist_name3 = models.CharField(max_length=100, default=None, null=True)
    chemist_number3 = models.IntegerField(default=None, null=True)


class Lab(models.Model):
    lab_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient_lab = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)

    lab_name1 = models.CharField(max_length=200)
    lab_number1 = models.IntegerField(null=True)

    lab_name2 = models.CharField(max_length=200, default=None, null=True)
    lab_number2 = models.IntegerField(default=None, null=True)


class Ambulance(models.Model):
    ambulance_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient_ambulance = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)

    amb_name1 = models.CharField(max_length=150)
    amb_number1 = models.IntegerField()

    amb_name2 = models.CharField(max_length=150, default=None, null=True)
    amb_number2 = models.IntegerField(default=None, null=True)

    amb_name3 = models.CharField(max_length=150, default=None, null=True)
    amb_number3 = models.IntegerField(default=None, null=True)


# # class UserPreferreds(models.Model):

#     # p_family = models.ForeignKey(FamilyMember, on_delete=models.CASCADE)
#     # p_hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
#     # p_lab = models.ForeignKey(Lab, on_delete=models.CASCADE)
#     # p_chemist = models.ForeignKey(Chemist, on_delete=models.CASCADE)
#     # p_doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
#     # p_amb = models.ForeignKey(Ambulance, on_delete=models.CASCADE)
