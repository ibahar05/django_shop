from django.db import models
from accounts.validators import validation_iranian_cellphone


class Contact(models.Model):
    
    name = models.CharField(max_length=255)
    phone_number = models.CharField(
            max_length=13, validators=[validation_iranian_cellphone]
    )
    email = models.EmailField()
    subject = models.CharField(max_length=255, null= True, blank= True)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ["created_date"]

    def __str__(self):
        return self.name 
    
class NewsLetter(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email 
