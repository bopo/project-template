from django.db import models
from django_lifecycle import LifecycleModel, hook

# Create your models here.



class UserAccount(LifecycleModel):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=200)
    password_updated_at = models.DateTimeField(null=True)
    
    @hook('before_update', when='password', has_changed=True)
    def timestamp_password_change(self):
        self.password_updated_at = timezone.now()


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__original_password = self.password


    def save(self, *args, **kwargs):
        if self.pk is not None and self.password != self.__orginal_password:
            self.password_updated_at = timezone.now()
        super().save(*args, **kwargs)       
