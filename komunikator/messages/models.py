from django.db import models
from komunikator.accounts.models import User

# Create your models here.

class Messages(models.Model):

    from_id = models.ForeignKey(User, default=None, on_delete=models.SET_DEFAULT, null=False, blank=False)
    to_id = models.ForeignKey(User, default=None, on_delete=models.SET_DEFAULT, null=False, blank=False)
    message = models.CharField(max_length=1000)
    date_time = models.DateTimeField()
