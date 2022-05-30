from django.test import TestCase

from gally_app.views import category

from .models import *
# Create your tests here.



class LocationTestCase(TestCase):
  def setUp(self):
    self.location = Location(name="mars")

  def testInit(self):
    self.assertTrue(self.location, "mars")
  
  def testSave(self):
    Location.save_location(self.location)
  pass


class CategoryTestCase(TestCase):
  def setUp(self):
    self.category = Category(name="photography")

  def testInit(self):
    self.assertTrue(self.category, "photography")

  def testSave(self):
    Category.save_category(self.category)
    self.assertEqual(Category.objects.all(), Category(name="photography"))
  pass

class ImageTestCase(TestCase):
  
  def setUp(self) -> None:
      self.img1 = Image(img="/dbddkobs4/image/upload/v1653763532/fkx4bmfae7enhta2wfqz.jpg",img_name="abc",description="abcdef",location=Location(name="mars"),category=Category(name="photography"))
      
  
  def testInit(self):
    self.assertTrue(self.img1,Image)

  def testSave(self):
    Image.save_image(self.img1)



class CopyFunctionTestCase(TestCase):
  pass
  
