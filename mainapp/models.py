from django.db import models
from django.utils.text import slugify
# Create your models here.


class Catego(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Book(models.Model):
    status_book = [
        ('available','available'),
        ('rental','rental'),
        ('sold','sold'),
    ]
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50,null=True,blank=True)
    img_book = models.ImageField( upload_to='imgs/book/', null=True,blank=True)
    img_author = models.ImageField( upload_to='imgs/book/',null=True,blank=True)
    pages = models.IntegerField(null=True,blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2,null=True,blank=True)
    retal_day = models.DecimalField(max_digits=5, decimal_places=2,null=True,blank=True)
    retal_period = models.DecimalField(max_digits=5, decimal_places=2,null=True,blank=True)
    active = models.BooleanField(default=True)
    staus = models.CharField(choices=status_book,null=True,blank=True, max_length=50)
    category = models.ForeignKey(Catego,on_delete=models.PROTECT,null=True,blank=True)
    total_rental = models.DecimalField(max_digits=5, decimal_places=2,null=True,blank=True)
    slug = models.SlugField(null=True,blank=True)

    def save(self,*args, **kwargs):
        self.slug = slugify(self.title)
        super(Book,self).save(*args, **kwargs)
    def __str__(self):
        return self.title
    