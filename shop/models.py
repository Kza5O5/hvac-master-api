from django.db import models

# Create your models here.

class TopHeader(models.Model):
    shift = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    def __str__(self):
        return f'Top Header - {self.shift} | {self.email} | {self.phone}'
class Menu(models.Model): 
    menuName = models.CharField(max_length=200,null=True) 
    url = models.CharField(max_length=200,null=True) 
    
    def __str__(self):
        return f'{self.menuName}' 

class SubMenu(models.Model): 
    menuName = models.CharField(max_length=200,null=True) 
    url = models.CharField(max_length=200,null=True) 
    menuId= models.ForeignKey(Menu,on_delete=models.CASCADE,null=True,related_name='submenus') 
    def __str__(self): 
        return f'{self.menuId.menuName} -> {self.menuName}' 

class Sub2Menu(models.Model): 
    menuName = models.CharField(max_length=200,null=True) 
    url = models.CharField(max_length=200,null=True) 
    menuId= models.ForeignKey(SubMenu,on_delete=models.CASCADE,null=True) 
    def __str__(self):
        return f'{self.menuId.menuName} -> {self.menuName}' 
    
class HomeBanner(models.Model):
    image = models.ImageField(upload_to='home_banners/', null=True, blank=True)
    title = models.CharField(max_length=200, null=True)
    model = models.CharField(max_length=200, null=True)
    price = models.CharField(max_length=200, null=True)
    time = models.CharField(max_length=200, null=True)
    def __str__(self):
        return f'Home Banner - {self.title} | {self.price}'

class Service(models.Model):
    maintitle = models.CharField(max_length=200, null=True)
    maintext = models.TextField(null=True, blank=True)
    image1 = models.ImageField(upload_to='services/', null=True, blank=True)
    title1 = models.CharField(max_length=200, null=True)
    text1 = models.TextField(null=True, blank=True)
    image2 = models.ImageField(upload_to='services/', null=True, blank=True)
    title2 = models.CharField(max_length=200, null=True)
    text2 = models.TextField(null=True, blank=True)
    image3 = models.ImageField(upload_to='services/', null=True, blank=True)
    title3 = models.CharField(max_length=200, null=True)
    text3 = models.TextField(null=True, blank=True)
    image4 = models.ImageField(upload_to='services/', null=True, blank=True)
    title4 = models.CharField(max_length=200, null=True)
    text4 = models.TextField(null=True, blank=True)
    def __str__(self):
        return f'Service - {self.maintitle}'

class Feature(models.Model):
    title = models.CharField(max_length=200, null=True)
    text = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='features/', null=True, blank=True)
    def __str__(self):
        return f'Feature - {self.title}'

class Car(models.Model):
    stock = models.CharField(max_length=200,null=True)
    laste_on_sale = models.CharField(max_length=200,null=True,blank=True)
    image = models.ImageField(upload_to='cars/', null=True, blank=True)
    vin = models.CharField(max_length=200,null=True)
    price = models.CharField(max_length=200,null=True)
    name = models.CharField(max_length=200,null=True)
    year = models.CharField(max_length=200,null=True)
    mile = models.CharField(max_length=200,null=True)
    tranmission = models.CharField(max_length=200,null=True)
    housepw = models.CharField(max_length=200,null=True)
    def __str__(self):
        return f'{self.name} - {self.year}'
    
# -----------------------------------
class CarDetails(models.Model):
    carId = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='cardetails')
    title = models.CharField(max_length=200,null=True)
    name = models.CharField(max_length=200,null=True)
    image = models.ImageField(upload_to='cars/', null=True, blank=True)
    stock = models.CharField(max_length=200,null=True)
    vin = models.CharField(max_length=200,null=True)
    price = models.CharField(max_length=200,null=True)
    text = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.name
    
class CarDetailImage(models.Model):
    carId = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='cardetailimages')
    image = models.ImageField(upload_to='cars/', null=True, blank=True)
    def __str__(self):
        return f'Image for - {self.id} - {self.carId.name}'
    
    # =============================


class CarImage(models.Model):
    carId = models.ForeignKey(Car, on_delete= models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='car_images/', null=True, blank=True)

    def __str__(self):
        return f'Image for {self.carId.name} - {self.carId.year}'

class ChooseUs(models.Model):
    title = models.CharField(max_length=200, null=True)
    maintext = models.TextField(null=True, blank=True)
    text1 = models.TextField(null=True, blank=True)
    text2 = models.TextField(null=True, blank=True)
    text3 = models.TextField(null=True, blank=True)
    text4 = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='choose_us/', null=True, blank=True)
    def __str__(self):
        return f'Choose Us - {self.title}'
    
class Blog(models.Model):
    image = models.ImageField(upload_to='blogs/', null=True, blank=True)
    user = models.CharField(max_length=200, null=True)
    date = models.DateField(null=True, blank=True)
    commenttitle = models.CharField(max_length=200, null=True)
    commenttext = models.TextField(null=True, blank=True)
    def __str__(self):
        return f'Latest Blog - {self.user} | {self.date}'

class BlogDetails(models.Model):
    blogId = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='details')
    image = models.ImageField(upload_to='blogs_details/', null=True, blank=True)
    user = models.CharField(max_length=200, null=True)
    date = models.DateField(null=True, blank=True)
    commenttitle = models.CharField(max_length=200, null=True)
    commenttext = models.TextField(null=True, blank=True)
    def __str__(self):
        return f'{self.user} | {self.date}'

class BlogImage(models.Model):
    blogId = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    def __str__(self):
        return f'Image for Blog by {self.blogId.user} on {self.blogId.date}'
    
class FooterSection(models.Model):
    title = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    logo = models.ImageField(upload_to='footer/', null=True, blank=True)
    image = models.ImageField(upload_to='footer/', null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    def __str__(self):
        return f'Footer - {self.title} | {self.phone} | {self.email}'

class TitleBanner(models.Model):
    MenuID = models.ForeignKey(Menu, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200, null=True)
    text = models.CharField(max_length=200, null=True)
    def __str__(self):
        return f'{self.title} | {self.text} '

class TitleBanner2(models.Model):
    MenuID = models.ForeignKey(Menu, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200, null=True)
    text = models.CharField(max_length=200, null=True)
    def __str__(self):
        return f'{self.title} | {self.text} '
  

class AccessToken(models.Model):
    token = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.token
