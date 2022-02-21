from django.db import models

# Create your models here.


class Inventory(models.Model):
    image = models.CharField(max_length=250)
    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.item_name

    # class Meta:
        # ordering = [self.item_name]
