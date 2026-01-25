from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    # Category options matching your sketch
    CATEGORY_CHOICES = [
        ('Articles', 'Articles'),
        ('Poems', 'Poems'),
        ('Stories', 'Stories'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=1500) 
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    
    # ADD THIS LINE 👇
    category = models.CharField(
        max_length=20, 
        choices=CATEGORY_CHOICES, 
        default='Articles'
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self): 
        return f'{self.user.username} - {self.text[:20]}...'