# Generated by Django 5.0.4 on 2024-05-07 23:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_group_permission_agent'),
    ]

    operations = [
        migrations.CreateModel(
            name='ControlPoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('ville', models.CharField(max_length=255)),
                ('quartier', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Point de contrôle',
                'verbose_name_plural': 'Points de contrôle',
            },
        ),
        migrations.CreateModel(
            name='ControlPointByAgent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.BooleanField(default=True)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.agent')),
                ('control_point', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.controlpoint')),
            ],
            options={
                'verbose_name': 'Point de contrôle par agent',
                'verbose_name_plural': 'Points de contrôle par agents',
                'unique_together': {('agent', 'control_point')},
            },
        ),
        migrations.AddField(
            model_name='controlpoint',
            name='agents',
            field=models.ManyToManyField(through='users.ControlPointByAgent', to='users.agent'),
        ),
    ]
