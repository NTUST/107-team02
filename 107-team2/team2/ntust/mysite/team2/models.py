from django.db import models

# Create your models here.

class Area(models.Model):
    area = models.CharField(max_length=20)

    def __str__(self):
        return self.area

class M_Type(models.Model):
    m_type = models.CharField(max_length=20)

    def __str__(self):
        return self.m_type

class Museum(models.Model):
    name = models.CharField(max_length=20)
    price_adult = models.CharField(max_length=20)
    price_discount = models.CharField(max_length=20)
    time =  models.CharField(max_length=100)
    rest = models.CharField(max_length=100)
    img = models.ImageField(upload_to='media/')
    hy = models.CharField(max_length=600)
    intro = models.CharField(max_length=1000)
    area = models.ForeignKey(Area)
    mtype = models.ForeignKey(M_Type)
    img1 = models.ImageField(upload_to='media/',blank=True)
    img2 = models.ImageField(upload_to='media/',blank=True)
    img3 = models.ImageField(upload_to='media/',blank=True)
    img4 = models.ImageField(upload_to='media/',blank=True)
    img5 = models.ImageField(upload_to='media/',blank=True)

    def __str__(self):
        return self.name


class About(models.Model):
    name = models.CharField(max_length=20)
    sy = models.CharField(max_length=20)
    img = models.ImageField(upload_to='media/')
    def __str__(self):
        return self.name

class home_page(models.Model):
    intro = models.CharField(max_length=300)
    img = models.ImageField(upload_to='media/')
    def __str__(self):
        return self.intro

class Comment(models.Model):
    content = models.CharField(max_length=200)
    user = models.CharField(max_length=20)
    museum = models.ForeignKey(Museum)

    def __str__(self):
        return self.content