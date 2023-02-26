from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.

class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='blogs')
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    content = models.TextField()
    image = models.ImageField(blank=True, upload_to='blogs')

    
    def __str__(self):
        return self.title