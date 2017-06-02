from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User') #작성자
    title = models.CharField(max_length=200) # 제목
    text = models.TextField() #내용
    created_date = models.DateTimeField(default=timezone.now)
    # 생성일
    published_date = models.DateTimeField(blank=True, null=True)
    #작성일

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


# Create your models here.
