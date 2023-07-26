from django.db import models
from django.db import models
from django.utils import timezone
# Create your models here. 注意縮排
class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    abstract = models.TextField()
    pic_url= models.URLField(max_length=250)
    body = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-pub_date',)
        
    def __str__(self):
        return self.title
