from django.db import models

from django.db.models import Model
from django.contrib.auth.models import User
import datetime
# Create your models here. for databases
class ChaiVariety(models.Model):
    CHAI_TYPE_CHOICE = [
        ('ML', "MASALA"),
        ('GR', 'GINGER'),
        ('kl','KIWI'),
        ('PL','PLAIN'),
        ('EL','ELAICHI'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(default='chais/')
    date_added = models.DateTimeField(default=datetime.datetime.now)
    type=models.CharField(max_length=2, choices=CHAI_TYPE_CHOICE)
    description = models.TextField(default='')
    use = models.CharField(max_length=255, default='default_value')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self): 
        return self.name
  
#one to many
class ChaiReview(models.Model):
     chai=models.ForeignKey(ChaiVariety, on_delete=models.CASCADE, related_name='review')
   
    # other fields...

     rating=models.IntegerField()
     comment=models.TextField()
     date_added=models.DateTimeField(default=datetime.datetime.now)

     def __str__(self): 
         return f'{self.name.username} review for {self.chai.name}'
    
#many to many  
class Store(models.Model):
     name = models.CharField(max_length=255)
     location = models.CharField(max_length=100)
     chai_varieties = models.ManyToManyField(ChaiVariety, related_name='stores')

     def __str__(self): 
        return self.name
 
#one to one 
class ChaiCertificate(models.Model):
     chai=models.OneToOneField(ChaiVariety, on_delete=models.CASCADE, related_name='certificate')
     certificate_number = models.CharField(max_length=255) 
     issued_date=models.DateTimeField(default=datetime.datetime.now) 
     valid_until=models.DateTimeField()    

     def __str__(self):
      return f'Certificate for {self.name.chai}'

       


     