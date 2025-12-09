"""
Database models for the Red-Haired Pirates crew management system.

This module contains the CrewMember model for storing information
about individuals who want to join Shanks' pirate crew.
"""

from django.db import models


class CrewMember(models.Model):
    """
    Model representing a crew member application for the Red Hair Pirates.
    
    Attributes:
        name (str): Full name of the applicant
        email (str): Unique email address for contact
        age (int): Age of the applicant
        hometown (str): Place of origin
        role (str): Preferred role on the ship (fighter, navigator, etc.)
        skills (str): Description of the applicant's abilities
        reason (str): Why they want to join the crew
        joined_date (datetime): Timestamp when the application was submitted
    """
    
    ROLE_CHOICES = [
        ('fighter', 'Fighter'),
        ('navigator', 'Navigator'),
        ('cook', 'Cook'),
        ('doctor', 'Doctor'),
        ('sniper', 'Sniper'),
        ('musician', 'Musician'),
        ('general', 'General Crew'),
    ]
    
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    hometown = models.CharField(max_length=150)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    skills = models.TextField()
    reason = models.TextField(help_text="Why do you want to join the Red Hair Pirates?")
    joined_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        """Return string representation of the crew member."""
        return f"{self.name} - {self.role}"
    
    class Meta:
        ordering = ['-joined_date']
