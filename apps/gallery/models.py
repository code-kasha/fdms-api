from django.db import models


class Image(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)
    image = models.ImageField(upload_to="images/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Images"

    def __str__(self):
        return self.title


class Gallery(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    images = models.ManyToManyField(Image, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Galleries"

    def __str__(self):
        return self.title
