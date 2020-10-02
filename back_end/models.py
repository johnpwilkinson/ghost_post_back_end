from django.db import models
from django.utils import timezone
# Create your models here.


class Posts(models.Model):



    post_content = models.CharField(max_length=280)
    boast_or_roast = models.BooleanField()
    submission_time = models.DateTimeField( default=timezone.now)
    votes = models.IntegerField(default=0)
    


        
        

    def __str__(self):
        return self.post_content

