from django.db import models
from django.urls import reverse

# Create your models here.


class Jobs(models.Model):
    image = models.ImageField(upload_to="images/")
    upload_date = models.DateTimeField(auto_now_add=True)
    

    def get_absolute_url(self):     
        return reverse('home', args=[str(self.id)])

   

