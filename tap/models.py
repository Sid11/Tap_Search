from django.db import models
from django.utils.text import slugify

class Post(models.Model):

    para = models.TextField(blank=True, null=True)
    #image = models.ImageField(upload_to="post_images")

    slug = models.SlugField(default='', blank=True)

    def save(self):
        self.slug = slugify(self.para)
        super(Post, self).save()

    def __str__(self):
        return '%s' % self.para


class Image(models.Model):
    name = models.CharField(max_length=500)
    img = models.ImageField(upload_to='images/')
