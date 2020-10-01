from django.db import models

# Create your models here.
class Product(models.Model):
  product_id = models.AutoField  #autofield is auto assigning integer and increment for new obj
  name = models.CharField(max_length=30)
  category = models.CharField(max_length=50 ,default='')
  subcategory = models.CharField(max_length=50,default='')
  price = models.IntegerField(default=0)
  description = models.CharField(max_length=100)
  publish_date = models.DateField()
  image= models.ImageField(upload_to='shop/images',default='')

  #this fucn is for displaying product in admin panel by what(ex: in this case by name)
  def __str__(self):
    return self.name

