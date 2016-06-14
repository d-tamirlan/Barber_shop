from django.db import models
from ckeditor import fields


class Navigation(models.Model):
    nav_item = models.CharField("Элемент навигации", max_length=100, default="")
    url = models.CharField("Ссылка", max_length=100, default="/писать между слешами/")
    number = models.IntegerField("Номер в очереди", default=0)

    def __str__(self):
        return self.nav_item

    class Meta:
        ordering = ["number"]


class ContactInfo(models.Model):
    info = fields.RichTextField("Информация", max_length=5000, default="")
    working_time = fields.RichTextField("Время работы", max_length=1000, default="")

    def __str__(self):
        return "Контактная информация"


class Description(models.Model):
    title = models.CharField("Заголовок", max_length=100, default="")
    description = fields.RichTextField("Описание", max_length=5000, default="")
    number = models.IntegerField("Номер в очереди", default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["number"]


class PriceTable(models.Model):
    service = models.CharField("Услуга", max_length=100, default="")
    price = models.IntegerField("Цена", default=0)

    def __str__(self):
        return self.service


class ManufacturerList(models.Model):
    name = models.CharField("Название", max_length=100, default="")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["id"]

class ProductGroup(models.Model):
    name = models.CharField("Название", max_length=100, default="")

    def __str__(self):
        return self.name


class AboutUs(models.Model):
    description1 = fields.RichTextField("Превое описание", max_length=5000, default="")
    description2 = fields.RichTextField("Второе описание", max_length=5000, default="")

    def __str__(self):
        return "О нас"
