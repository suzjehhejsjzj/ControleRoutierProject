# Generated by Django 5.0.4 on 2024-05-08 00:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_criteria'),
    ]

    operations = [
        migrations.CreateModel(
            name='CriteriaByControl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criteria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.criteria')),
            ],
            options={
                'verbose_name': 'Critère par contrôle',
                'verbose_name_plural': 'Critères par contrôle',
            },
        ),
        migrations.CreateModel(
            name='RoadControl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Date')),
                ('type_piece', models.CharField(max_length=255, verbose_name='Type de pièce')),
                ('license_number', models.CharField(max_length=255, verbose_name='Numéro du permis ou CNI / PASSEPORT')),
                ('type_vehicule', models.CharField(max_length=255, verbose_name='Type de véhicule')),
                ('imatriculation', models.CharField(max_length=255, verbose_name='Imatriculation du véhicule')),
                ('telephone_conducteur', models.CharField(max_length=255, unique=True, verbose_name='Numéro téléphone conducteur')),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.agent')),
                ('control_point', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.controlpoint')),
                ('criteria', models.ManyToManyField(through='users.CriteriaByControl', to='users.criteria', verbose_name='Critères')),
            ],
            options={
                'verbose_name': 'Contrôle routier',
                'verbose_name_plural': 'Contrôles routiers',
            },
        ),
        migrations.AddField(
            model_name='criteriabycontrol',
            name='road_control',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.roadcontrol'),
        ),
        migrations.AlterUniqueTogether(
            name='criteriabycontrol',
            unique_together={('criteria', 'road_control')},
        ),
    ]