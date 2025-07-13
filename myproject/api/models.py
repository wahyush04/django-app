from django.db import models

class Component(models.Model):
    CATEGORY_CHOICES = [
        ('CPU', 'Processor'),
        ('GPU', 'Graphics Card'),
        ('RAM', 'Memory'),
        ('SSD', 'Solid State Drive'),
        ('HDD', 'Hard Disk Drive'),
        ('PSU', 'Power Supply'),
        ('MOBO', 'Motherboard'),
        ('CASE', 'PC Case'),
        ('FAN', 'Cooling Fan'),
        ('OTHER', 'Other')
    ]

    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.category})"

