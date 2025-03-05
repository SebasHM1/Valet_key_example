from django.db import models
import uuid
from django.utils.timezone import now
from datetime import timedelta

def default_expiration():
    return now() + timedelta(seconds=30)

class ValetKey(models.Model):
    id = models.BigAutoField(primary_key=True)  
    file_path = models.CharField(max_length=255)  
    key = models.UUIDField(default=uuid.uuid4, unique=True)
    expires_at = models.DateTimeField(default=default_expiration)  # Usa la función

    def is_valid(self):
        return now() < self.expires_at
