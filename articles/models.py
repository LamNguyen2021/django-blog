from django.db import models

# Create your models here.
class Article(models.Model):
  title = models.CharField(max_length=100)
  content = models.TextField()
  created_date = models.DateTimeField(auto_now_add=True)
  
  def __str__(self) -> str:
    return self.title