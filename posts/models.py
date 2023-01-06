from cloudinary.models import CloudinaryField

from django.db import models


class Post(models.Model):
    class Meta(object):
        db_table = 'post'

    name=models.CharField(
            'Name', blank=False, null=False, max_length=14, db_index=True, default='Anonymous'
        )
    body = models.CharField(
            'body', blank=True, null=True, max_length=140, db_index=True 
        )
    image = CloudinaryField(
        'image',blank=True,null=True,db_index=True
    )
    count=models.IntegerField(
        'Like',default=0,null=True,blank=True
    )
    created_at = models.DateTimeField(
            'Created DateTime', blank=True, auto_now_add=True
        )




