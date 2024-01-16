from django.db import models

# Create your models here.

class Bynary_tree(models.Model):
    parent = models.CharField(max_length = 50,default="")
    node = models.CharField(max_length = 50)
    name = models.CharField(max_length = 50,unique = True)

    def __str__(self):
        return self.name


