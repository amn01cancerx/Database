# Generated by Django 4.1.4 on 2023-01-07 07:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_hospital_hos_name3'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ambulance',
            name='patient_ambulance',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.patient'),
        ),
        migrations.AlterField(
            model_name='chemist',
            name='chemist_name2',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='chemist',
            name='chemist_name3',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='lab',
            name='lab_name2',
            field=models.CharField(default=None, max_length=200, null=True),
        ),
    ]
