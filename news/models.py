from django.db import models


class News(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True) # рег.даты создания
    updated_at = models.DateTimeField(auto_now=True) # рег.даты изменения
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/') # параметр показывает куда сохранять
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title