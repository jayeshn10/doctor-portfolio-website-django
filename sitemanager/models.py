from PIL import Image
from django.db import models

# Create your models here.
from django.utils.datetime_safe import datetime
from django.utils.safestring import mark_safe


class Blogs(models.Model):
    blog_title = models.CharField(verbose_name='Title', max_length=255)
    blog_slug = models.SlugField(verbose_name='Slug', max_length=255)
    blog_desc = models.TextField(verbose_name='Description', max_length=20000)
    blog_pubdate = models.DateTimeField(verbose_name='Published Date & Time', default=datetime.now)
    blog_publish = models.BooleanField(verbose_name="Publish Status")
    blog_img = models.ImageField(verbose_name='Image', upload_to='blogimages/')

    class Meta:
        verbose_name_plural = 'Blog Posts'

    def __str__(self):
        return self.blog_title


class BlogImage(models.Model):
    blog = models.ForeignKey(Blogs, verbose_name='Blog Title', default=None, on_delete=models.CASCADE)
    blog_images = models.ImageField(verbose_name='Image', upload_to='blogimages/')

    class Meta:
        verbose_name_plural = 'Blog Images'

    def __str__(self):
        return self.blog.blog_title


class PortfolioImages(models.Model):
    portfolio_title = models.CharField(verbose_name='Caption', max_length=255)
    portfolio_img = models.ImageField(verbose_name='Image', upload_to='Portfolioimages/')
    publish_status = models.BooleanField(verbose_name="Publish Status")

    class Meta:
        verbose_name_plural = 'Portfolio'

    def __str__(self):
        return self.portfolio_title


class MapSection(models.Model):
    address_title = models.CharField(verbose_name='Title', max_length=255)
    address = models.TextField(verbose_name='Address')
    address_url = models.TextField(verbose_name='Address Url')
    avl_time = models.CharField(verbose_name='Time', max_length=255, blank=True)
    contact_no = models.CharField(verbose_name='Contact Number', max_length=255)

    class Meta:
        verbose_name_plural = 'Map Section'

    def __str__(self):
        return self.address_title


class ContactInfo(models.Model):
    personal_email = models.EmailField(verbose_name='Email Id')
    personal_contactno = models.CharField(verbose_name='Contact No', max_length=255)

    class Meta:
        verbose_name_plural = 'Contact Information'

    def __str__(self):
        return str(self.id)


class BlogExtraImage(models.Model):
    img_caption = models.CharField(verbose_name='Caption', max_length=255)
    blog_image = models.ImageField(verbose_name='Image', upload_to='blogdescimages/')

    class Meta:
        verbose_name_plural = 'Blog Description Images'

    def __str__(self):
        return self.img_caption


class ProfileImage(models.Model):
    img_caption = models.CharField(verbose_name='Caption', max_length=255)
    image_src = models.ImageField(verbose_name='Image size(600x500px)', upload_to='Profileimage/', )

    @property
    def thumbnail_preview(self):
        if self.image_src:
            return mark_safe('<img src="{}" width="500" height="600" />'.format(self.image_src.url))
        return ""

    class Meta:
        verbose_name_plural = 'Profile Image'

    def __str__(self):
        return self.img_caption


class CarouselImage(models.Model):
    Carouse_caption = models.CharField(verbose_name='Title', max_length=255)
    cimage_src = models.ImageField(verbose_name='Image', upload_to='Carouselimages/')

    @property
    def thumbnail_preview(self):
        if self.cimage_src:
            return mark_safe('<img src="{}" width="400" height="300" />'.format(self.cimage_src.url))
        return ""

    class Meta:
        verbose_name_plural = 'Certificates'

    def _str_(self):
        return self.Carouse_caption