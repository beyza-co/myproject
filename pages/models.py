from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=200, verbose_name='Plaj İsmi')
    image = models.ImageField(upload_to='pages/', verbose_name='Plaj Resimleri', default='')
    body=models.TextField()
    def __str__(self) :
        return self.title
    
class Restaurant(models.Model):
    title=models.CharField(max_length=100, verbose_name='Restoran İsmi')
    image=models.ImageField(upload_to='pages/', verbose_name='Restoran Resimleri',default='')
    body=models.TextField()
    def __str__(self) :
        return self.title
    
class Index(models.Model):
    title=  title=models.CharField(max_length=100)
    image=models.ImageField(upload_to='pages/',default='') 
    body=models.TextField()
    def __str__(self) :
        return self.title
    
class Hotel(models.Model):
    title=  title=models.CharField(max_length=100)
    image=models.ImageField(upload_to='pages/',default='') 
    body=models.TextField()
    def __str__(self) :
        return self.title
    
