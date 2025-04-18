from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    
    CHOICE = (
        ('full-time', 'Full-time'),
        ('part-time', 'Part-time'),
        ('freelance', 'Freelance'),
        ('other', 'Other')
    )
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone_number = models.CharField(max_length=30, blank=True, null=True)
    profile_image = models.ImageField(upload_to='profile_images', blank=True, null=True)
    cover_image = models.ImageField(upload_to='cover_images', blank=True, null=True)
    occupation = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    availability = models.CharField(max_length=100, choices=CHOICE, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    years_of_experience = models.PositiveIntegerField(blank=True, null=True) # i need to see the cero
    adress = models.CharField(max_length=150, blank=True, null=True)
    company_name = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.user.username
    
    
    #langage
    #country
    