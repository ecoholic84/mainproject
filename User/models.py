from django.db import models
from Guest.models import *

# Create your models here.

class tbl_feedback(models.Model):
    feedback_content=models.CharField(max_length=1000)
    feedback_date=models.DateField(auto_now_add=True)
    user_id=models.ForeignKey(tbl_user, on_delete=models.CASCADE)