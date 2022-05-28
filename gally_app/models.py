from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.


class Location(models.Model):
  name = models.CharField(max_length=200)


  def __str__(self):
    return self.name

  



class Category(models.Model):
  name = models.CharField(max_length=200)

  def __str__(self):
    return self.name
  



class Image(models.Model):
  img = CloudinaryField('image')
  img_name = models.CharField(max_length=200)
  description = models.CharField(max_length=200)
  location = models.ForeignKey(Location,on_delete=models.CASCADE)
  category = models.ForeignKey(Category,on_delete=models.CASCADE)


  def __str__(self):
    return f"img_name: {self.img_name},description: {self.description},location: {self.location.name}, category: {self.category.name}"

  def save_image(self):
    self.save()
  
  def delete_image(self):
    self.delete()

  def update_image(self):
    self.update()
  
  def get_image_by_id(id):
    return Image.objects.get(id=id)

  def search_image(category):
    return Image.objects.filter(category = category)

  def filter_by_location(location):
    return Image.objects.filter(location = location)
  
  def locationName(self):
    return self.location.name
  
  def categoryName(self):
    return self.category.name
      
      


