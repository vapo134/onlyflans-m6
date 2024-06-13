from django.db import models
import uuid

# Flan, generar y aplicar modelo
class Flan(models.Model):
    flans_uuid = models.UUIDField(primary_key = True, default=uuid.uuid4, editable=False) 
    name = models.CharField(max_length = 64)
    description = models.TextField()
    image_url = models.URLField(blank=True)
    slug = models.SlugField()
    is_private = models.BooleanField()
    
    
    def __str__(self):
        return self.name
    
# ContactForm, generar y aplicar sus migraciones y agregar el modelo
class ContactForm(models.Model):
    contact_form_uuid = models.UUIDField(primary_key = True, default=uuid.uuid4, editable=False)
    customer_email = models.EmailField()
    customer_name = models.CharField(max_length  = 64)
    message = models.TextField()
    
    def __str__(self):
        return self.customer_name