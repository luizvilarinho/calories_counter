from django.db import models

class Calories(models.Model):
    alimento = models.CharField(max_length=255)
    cal = models.DecimalField(max_digits=10, decimal_places=2)
    p = models.DecimalField(max_digits=10, decimal_places=2)
    c = models.DecimalField(max_digits=10, decimal_places=2)
    g = models.DecimalField(max_digits=10, decimal_places=2)
    f = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'tb_taco'

    def __str__(self):
        return self.alimento
