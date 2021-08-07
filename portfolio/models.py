from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('blog')

class Post(models.Model):
    title = models.CharField(max_length=255)
    # header_image = models.ImageField(null=True, blank=True, upload_to='images/')
    header_image = models.CharField(max_length=255, default='EmptyText')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    # body = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=255, default='Uncategorized')
    snippet = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        return reverse('blog')
        # return reverse('article-details', args=(str(self.id)))
    

