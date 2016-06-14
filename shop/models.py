from django.db import models
from django.utils import timezone
from ckeditor import fields
from my_cms import cms_models
from django.contrib.auth import models as dj_models
import datetime


class News(models.Model):
    title = models.CharField("Заголовок", max_length=50, default="")
    description = fields.RichTextField("Описание", default="")
    pub_date = models.DateField("Дата публикации", default=datetime.datetime.now())

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-pub_date"]


class NewsImages(models.Model):
    key = models.ForeignKey(News, verbose_name="Новость", related_name="images")
    image = models.ImageField("Фото", upload_to="news_images/")

    def __str__(self):
        return 'Фото к новости "{0}"'.format(self.key)

    class Meta:
        ordering = ["-key"]


class Record(models.Model):
    user_key = models.ForeignKey(dj_models.User, related_name="records", null=True)
    name = models.CharField("Имя", max_length=50, default="")
    tel_number = models.IntegerField("Номер телефона", default=0)
    time = models.CharField("Время", max_length=50, default="")
    date = models.CharField("Дата", max_length=50, default="")
    save_date = models.DateField("Дата сохранения", default=datetime.datetime.now())

    def __str__(self):
        return "Запись на прием клиента {0}".format(self.name)

    class Meta:
        ordering = ["-save_date"]


class Order(models.Model):
    user_key = models.ForeignKey(dj_models.User, related_name="orders", null=True)
    full_name = models.CharField("ФИО", max_length=100, default="")
    address = models.CharField("Адрес", max_length=200, default="")
    tel_number = models.IntegerField("Номер телефона", default=0)
    product_name = models.CharField("Название товара", max_length=200, default="")
    price = models.IntegerField("Цена товара", default=0)
    order_date = models.DateTimeField("Дата заказа", default=datetime.datetime.now())

    def __str__(self):
        return 'Заказ товара "{0}"'.format(self.product_name)

    class Meta:
        ordering = ["-order_date"]


class Product(models.Model):
    product_name = models.CharField("Название товара", max_length=200, default="")
    price = models.IntegerField("Цена товара", default=0)
    description = fields.RichTextField("Описание товара", max_length=5000, default="")
    in_stock = models.BooleanField("В наличии", default=False)
    in_kit = models.TextField("В наборе", max_length=5000, default="", blank=True, null=True)
    group = models.ForeignKey(cms_models.ProductGroup, verbose_name="Группа товара", related_name="products")
    manufacturer = models.ForeignKey(cms_models.ManufacturerList, verbose_name="Производитель", related_name="products")
    save_date = models.DateTimeField("Дата добавления", default=datetime.datetime.now())

    def __str__(self):
        return self.product_name

    class Meta:
        ordering = ["-save_date"]


class ProductImages(models.Model):
    key = models.ForeignKey(Product, verbose_name="Товар", related_name="images")
    image = models.ImageField("Фотография товара", upload_to="images/")

    def __str__(self):
        return 'Фтография товара "{0}"'.format(self.key)


class PhotoGallery(models.Model):
    img = models.ImageField(upload_to="photo_gallery/")

    def __str__(self):
        return "Фото"
