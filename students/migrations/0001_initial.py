# Generated by Django 5.0.1 on 2024-02-06 12:22

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('classes', '0001_initial'),
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('birth_date', models.DateField()),
                ('town', models.CharField(blank=True, max_length=50, null=True)),
                ('neighborhood', models.CharField(blank=True, max_length=50, null=True)),
                ('sex', models.CharField(choices=[('girl', 'Fille'), ('boy', 'Garçon')], max_length=50)),
                ('photo', models.ImageField(default='default.jpg', upload_to='students_pics')),
                ('matricule', models.CharField(max_length=50)),
                ('entry_date', models.DateField(default=django.utils.timezone.now)),
                ('active', models.BooleanField(default=True)),
                ('parent_name', models.CharField(max_length=50)),
                ('parent_phone', models.CharField(max_length=50)),
                ('parent_email', models.CharField(blank=True, max_length=50, null=True)),
                ('observations', models.TextField()),
                ('classe', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='classes.classe')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.school')),
            ],
        ),
    ]
