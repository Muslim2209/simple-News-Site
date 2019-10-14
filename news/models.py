from django.conf import settings
from django.contrib.auth.models import User, AbstractUser
from django.db import models


class NewsCategory(models.Model):
    name = models.CharField(max_length=125)

    class Meta:
        verbose_name_plural = 'News Categories'

    def __str__(self):
        return self.name


class NewsTag(models.Model):
    name = models.CharField(max_length=125)

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=225)
    body = models.TextField()
    image = models.ImageField(upload_to='uploads/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ManyToManyField('NewsCategory')
    tag = models.ManyToManyField('NewsTag', blank=True)

    class Meta:
        verbose_name_plural = 'News'
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class CustomUser(AbstractUser):
    is_subscribed = models.BooleanField(default=True)
    date_of_birth = models.DateField(null=True)

    def __str__(self):
        if self.first_name or self.last_name:
            return '{} {}'.format(self.first_name, self.last_name)
        else:
            return self.username

    REQUIRED_FIELDS = ['email', 'is_subscribed', 'date_of_birth']
