from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    thumbnail = models.ImageField(default='default.png', blank=True)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.title.upper()

    def capital(self):
        auth_cap = str(self.author)
        return auth_cap.capitalize()
    
    def snippets(self):
        
        return self.body[:30].capitalize() + '...'