from django.test import TestCase
from .models import Image, Category

# Create your tests here.
class ImageTest(TestCase):
    '''
    a class to test the Image and it's instances
    '''
    def setUp(self):
        self.picture = Image( image ='image/', img_name='myPicture', img_description='description')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.picture, Image))
        
    def test_save_image(self):
        '''
        function to check save method
        '''
        self.picture.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images)>0)
        
    def test_delete_image(self):
        '''
        method to delete a saved image
        '''
        self.picture.save_image()
        image = Image.objects.filter(img_name='myPicture').first()
        delete = Image.objects.filter(img_name= image.img_name).delete()
        images = Image.objects.all()
        self.assertFalse(len(images) == 1)    
        
    def test_update_image(self):
        '''
        a method to check the update method
        '''
        self.picture.save_image()
        image = Image.objects.filter(img_name='myPicture').first()
        update = Image.objects.filter(img_name= image.img_name).update(img_name = 'Picta')
        updated = Image.objects.filter(img_name = 'Picta').first()
        self.assertNotEqual(image.img_name, updated.img_name)
        
    def test_get_image_by_id(self):
        self.picture.save_image()
        image = Image.get_image_by_id(1)
        self.assertFalse(len(image) >0)       
        
class CategoryTest(TestCase):
    '''
    class to check the instances and function of category model
    '''
    def setUp(self):
        self.cat = Category( namecat ='leisure')    
        
    def test_instance(self):
        self.assertTrue(isinstance(self.cat, Category))
        
    def test_save_cat(self):
        self.cat.save_cat()
        categories = Category.objects.all()
        self.assertTrue(len(categories)>0)  
        
    def test_delete_cat(self):
        '''
        method to delete a saved category
        '''
        self.cat.save_cat()
        cat = Category.objects.filter(namecat='leisure').first()
        delete = Category.objects.filter(namecat= cat.namecat).delete()
        catz = Category.objects.all()
        self.assertFalse(len(catz) == 1)    
        
    def test_update_image(self):
        '''
        a method to check the update method
        '''
        self.cat.save_cat()
        cate = Category.objects.filter(namecat='leisure').first()
        update = Category.objects.filter(namecat= cate.namecat).update(namecat='food')
        updated = Category.objects.filter(namecat = 'food').first()
        self.assertNotEqual(cate.namecat, updated.namecat)    