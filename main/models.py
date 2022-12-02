from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(verbose_name="категории", max_length=100)
    slug = models.SlugField(null=False, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('main:category', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title


class NewsBlog(models.Model):
    title = models.CharField(verbose_name='статьи', max_length=200)
    category = models.ForeignKey(Category, verbose_name='категории', on_delete=models.CASCADE)
    content = models.TextField(verbose_name='контент')
    user = models.ForeignKey(User, verbose_name='автор', on_delete=models.CASCADE)
    img = models.ImageField(upload_to='main')
    slug = models.SlugField(null=False, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('main:detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title
