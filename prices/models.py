from django.db import models

class CryptoPrice(models.Model):
    name = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    change_24h = models.DecimalField(max_digits=10, decimal_places=2)
    change_7d = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.price}"
