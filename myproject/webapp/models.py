from django.db import models


class CrewMember(models.Model):
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
        return f"{self.name} - {self.role}"
    
    class Meta:
        ordering = ['-joined_date']
