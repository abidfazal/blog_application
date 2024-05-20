from django.db import models
from django.utils import timezone

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    
    def __str__(self) -> str:
        return self.name


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)
    publication_date = models.DateField(default=timezone.now)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.title
    

class Comment(models.Model):
    comment_id = models.IntegerField()
    comment = models.CharField(max_length=200)


    
    
