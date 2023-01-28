from django.contrib import admin
from .models import *

# Register your models here.
# admin.site.register(Patient)
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('user_id','name','phone_number')

@admin.register(FamilyMember)
class FamilyMemberAdmin(admin.ModelAdmin):
    list_display = ('family_id','patient_fam','fam_name1','fam_number1')

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('doctor_id','patient_doc','doc_name1','doc_number1')

@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = ('med_id','patiend_med','med_name1','med_time1','duration1','days1')

@admin.register(Ailment)
class AilmentAdmin(admin.ModelAdmin):
    list_display = ('ailment_id','patient_ailment','ailment_name','ailment_sub_type')

@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
    list_display = ('hos_id','hos_name1','hos_number1','patient_hos')

@admin.register(Chemist)
class ChemistAdmin(admin.ModelAdmin):
    list_display = ('chemist_id','chemist_name1','chemist_number1','patient_chemist')

@admin.register(Lab)
class LabAdmin(admin.ModelAdmin):
    list_display = ('lab_id','lab_name1','lab_number1','patient_lab')

@admin.register(Ambulance)
class AmbulanceAdmin(admin.ModelAdmin):
    list_display = ('ambulance_id','amb_name1','amb_number1')