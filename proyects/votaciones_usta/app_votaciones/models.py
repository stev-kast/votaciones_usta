from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=45, null=False)
    last_name = models.CharField(max_length=45, null=False)
    email = models.CharField(max_length=45, null=False)
    password = models.CharField(max_length=45, null=False)
    is_superuser = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        app_label = 'app_votaciones'