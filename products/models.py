from django.db import models


class Product(models.Model):
    class SizeChoices(models.TextChoices):
        SINGLE = "Single"
        DOUBLE = "Double"
        KING = "King"
        SUPER_KING = "Super King"
    
    class MaterialChoices(models.TextChoices):
        CALICO_GOLD = "Calico Gold"
        CALICO = "Calico"
        SATEEN = "Sateen"
        ENHANCED_COTTON = "Enhanced Cotton"
        POPLIN = "Poplin"
        FLANNEL = "Flannel"
    
    class ColorChoices(models.TextChoices):
        WHITE = "White"
        BLUE = "Blue"
        RED = "Red"
        BEIGE = "Beige"
        YELLOW = "Yellow"
        PINK = "Pink"
        GREEN = "Green"
        PURPLE = "Purple"

    name = models.CharField(max_length=255)
    size = models.CharField(choices=SizeChoices, max_length=50)
    material = models.CharField(choices=MaterialChoices, max_length=50)
    color = models.CharField(choices=ColorChoices, max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
