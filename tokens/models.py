from django.db import models

# Create your models here.

class Farmer(models.Model):
    name = models.CharField(max_length=100)
    village = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    registration_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Token(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled')
    ]

    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    crop_type = models.CharField(max_length=100)
    estimated_arrival_time = models.DateTimeField()
    actual_arrival_time = models.DateTimeField(null=True, blank=True)
    token_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    redeemed = models.BooleanField(default=False)

    def __str__(self):
        return f"Token #{self.id} - {self.farmer.name} - {self.estimated_arrival_time}"
    
    # tokens/models.py

class MandiPrice(models.Model):
    crop_name = models.CharField(max_length=100)
    variety = models.CharField(max_length=100)
    min_price = models.IntegerField()
    max_price = models.IntegerField()
    avg_price = models.IntegerField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.crop_name} - {self.variety} on {self.date}"

    