import uuid
from django.db import models

class Flan(models.Model):
    flan_uuid = models.UUIDField()
    name = models.CharField(max_length=64)
    description = models.TextField()
    image_url = models.URLField()
    slug = models.SlugField()
    is_private = models.BooleanField()
    no_eggs = models.BooleanField()
    no_sugar = models.BooleanField()
    no_lactose = models.BooleanField()

class ContactForm(models.Model):
    contact_form_uuid = models.UUIDField(default=uuid.uuid4,editable=False)
    customer_email = models.EmailField()
    customer_name = models.CharField(max_length=64)
    message = models.TextField()


    
# Create your models here.
