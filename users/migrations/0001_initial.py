# Generated by Django 5.1.7 on 2025-04-05 14:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(blank=True, max_length=30, null=True)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='profile_images')),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='cover_images')),
                ('occupation', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('availability', models.CharField(blank=True, choices=[('full-time', 'Full-time'), ('part-time', 'Part-time'), ('freelance', 'Freelance'), ('other', 'Other')], max_length=100, null=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('years_of_experience', models.PositiveIntegerField(blank=True, null=True)),
                ('adress', models.CharField(blank=True, max_length=150, null=True)),
                ('company_name', models.CharField(blank=True, max_length=100, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
