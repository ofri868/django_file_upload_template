from django.db import models

# Create your models here.
class Test(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    image = models.ImageField(null=True,blank=True,default='/placeholder.png')

    def __str__(self) -> str:
        return self.name

