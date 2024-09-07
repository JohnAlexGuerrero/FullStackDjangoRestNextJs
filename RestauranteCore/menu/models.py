from django.db import models
from django.urls import reverse

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=250)
    price = models.FloatField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = ("Menu")
        verbose_name_plural = ("Menus")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("menu_detail", kwargs={"pk": self.pk})
