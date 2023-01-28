# Generated by Django 4.1.4 on 2023-01-07 07:27

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('user_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('phone_number', models.IntegerField()),
                ('pin_code', models.IntegerField(default=None)),
                ('city', models.CharField(default=None, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('med_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('med_name1', models.CharField(default=None, max_length=100, null=True)),
                ('med_time1', models.CharField(max_length=100)),
                ('duration1', models.CharField(max_length=100)),
                ('days1', models.CharField(max_length=100)),
                ('med_name2', models.CharField(default=None, max_length=100, null=True)),
                ('med_time2', models.CharField(default=None, max_length=100, null=True)),
                ('duration2', models.CharField(default=None, max_length=100, null=True)),
                ('days2', models.CharField(default=None, max_length=100, null=True)),
                ('med_name3', models.CharField(default=None, max_length=100, null=True)),
                ('med_time3', models.CharField(default=None, max_length=100, null=True)),
                ('duration3', models.CharField(default=None, max_length=100, null=True)),
                ('days3', models.CharField(default=None, max_length=100, null=True)),
                ('med_name4', models.CharField(default=None, max_length=100, null=True)),
                ('med_time4', models.CharField(default=None, max_length=100, null=True)),
                ('duration4', models.CharField(default=None, max_length=100, null=True)),
                ('days4', models.CharField(default=None, max_length=100, null=True)),
                ('med_name5', models.CharField(default=None, max_length=100, null=True)),
                ('med_time5', models.CharField(default=None, max_length=100, null=True)),
                ('duration5', models.CharField(default=None, max_length=100, null=True)),
                ('days5', models.CharField(default=None, max_length=100, null=True)),
                ('med_name6', models.CharField(default=None, max_length=100, null=True)),
                ('med_time6', models.CharField(default=None, max_length=100, null=True)),
                ('duration6', models.CharField(default=None, max_length=100, null=True)),
                ('days6', models.CharField(default=None, max_length=100, null=True)),
                ('med_name7', models.CharField(default=None, max_length=100, null=True)),
                ('med_time7', models.CharField(default=None, max_length=100, null=True)),
                ('duration7', models.CharField(default=None, max_length=100, null=True)),
                ('days7', models.CharField(default=None, max_length=100, null=True)),
                ('med_name8', models.CharField(default=None, max_length=100, null=True)),
                ('med_time8', models.CharField(default=None, max_length=100, null=True)),
                ('duration8', models.CharField(default=None, max_length=100, null=True)),
                ('days8', models.CharField(default=None, max_length=100, null=True)),
                ('med_name9', models.CharField(default=None, max_length=100, null=True)),
                ('med_time9', models.CharField(default=None, max_length=100, null=True)),
                ('duration9', models.CharField(default=None, max_length=100, null=True)),
                ('days9', models.CharField(default=None, max_length=100, null=True)),
                ('med_name10', models.CharField(default=None, max_length=100, null=True)),
                ('med_time10', models.CharField(default=None, max_length=100, null=True)),
                ('duration10', models.CharField(default=None, max_length=100, null=True)),
                ('days10', models.CharField(default=None, max_length=100, null=True)),
                ('med_name11', models.CharField(default=None, max_length=100, null=True)),
                ('med_time11', models.CharField(default=None, max_length=100, null=True)),
                ('duration11', models.CharField(default=None, max_length=100, null=True)),
                ('days11', models.CharField(default=None, max_length=100, null=True)),
                ('med_name12', models.CharField(default=None, max_length=100, null=True)),
                ('med_time12', models.CharField(default=None, max_length=100, null=True)),
                ('duration12', models.CharField(default=None, max_length=100, null=True)),
                ('days12', models.CharField(default=None, max_length=100, null=True)),
                ('med_name13', models.CharField(default=None, max_length=100, null=True)),
                ('med_time13', models.CharField(default=None, max_length=100, null=True)),
                ('duration13', models.CharField(default=None, max_length=100, null=True)),
                ('days13', models.CharField(default=None, max_length=100, null=True)),
                ('med_name14', models.CharField(default=None, max_length=100, null=True)),
                ('med_time14', models.CharField(default=None, max_length=100, null=True)),
                ('duration14', models.CharField(default=None, max_length=100, null=True)),
                ('days14', models.CharField(default=None, max_length=100, null=True)),
                ('med_name15', models.CharField(default=None, max_length=100, null=True)),
                ('med_time15', models.CharField(default=None, max_length=100, null=True)),
                ('duration15', models.CharField(default=None, max_length=100, null=True)),
                ('days15', models.CharField(default=None, max_length=100, null=True)),
                ('patiend_med', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Lab',
            fields=[
                ('lab_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('lab_name1', models.CharField(max_length=200)),
                ('lab_number1', models.IntegerField()),
                ('lab_name2', models.CharField(default=None, max_length=200)),
                ('lab_number2', models.IntegerField(default=None)),
                ('patient_lab', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('hos_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('hos_name1', models.CharField(max_length=100)),
                ('hos_number1', models.IntegerField()),
                ('hos_name2', models.CharField(default=None, max_length=100, null=True)),
                ('hos_number2', models.IntegerField(default=102)),
                ('hos_name3', models.CharField(default=None, max_length=100)),
                ('hos_number3', models.IntegerField(default=102)),
                ('patient_hos', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.patient')),
            ],
        ),
        migrations.CreateModel(
            name='FamilyMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('family_id', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('fam_name1', models.CharField(max_length=100)),
                ('fam_number1', models.IntegerField()),
                ('fam_name2', models.CharField(default=None, max_length=100, null=True)),
                ('fam_number2', models.IntegerField(default=None, null=True)),
                ('fam_name3', models.CharField(default=None, max_length=100, null=True)),
                ('fam_number3', models.IntegerField(default=None, null=True)),
                ('patient_fam', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('doctor_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('doc_name1', models.CharField(max_length=100)),
                ('doc_number1', models.IntegerField()),
                ('doc_name2', models.CharField(default=None, max_length=100, null=True)),
                ('doc_number2', models.IntegerField(default=None, null=True)),
                ('doc_name3', models.CharField(default=None, max_length=100, null=True)),
                ('doc_number3', models.IntegerField(default=None, null=True)),
                ('patient_doc', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Chemist',
            fields=[
                ('chemist_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('chemist_name1', models.CharField(max_length=100)),
                ('chemist_number1', models.IntegerField()),
                ('chemist_name2', models.CharField(default=None, max_length=100)),
                ('chemist_number2', models.IntegerField(default=None)),
                ('chemist_name3', models.CharField(default=None, max_length=100)),
                ('chemist_number3', models.IntegerField(default=None)),
                ('patient_chemist', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Ambulance',
            fields=[
                ('ambulance_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('amb_name1', models.CharField(max_length=150)),
                ('amb_number1', models.IntegerField()),
                ('amb_name2', models.CharField(default=None, max_length=150)),
                ('amb_number2', models.IntegerField(default=None)),
                ('amb_name3', models.CharField(default=None, max_length=150)),
                ('amb_number3', models.IntegerField(default=None)),
                ('patient_ambulance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Ailment',
            fields=[
                ('ailment_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('ailment_name', models.CharField(max_length=100)),
                ('ailment_sub_type', models.CharField(default=None, max_length=100, null=True)),
                ('patient_ailment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.patient')),
            ],
        ),
    ]