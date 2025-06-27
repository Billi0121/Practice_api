from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your views here.
class Memories(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    