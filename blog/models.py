from django.db import models
from django.db.models import permalink

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    text = models.TextField()
    pub_date = models.DateField(db_index=True, auto_now_add=True)
    category = models.ForeignKey('blog.Category')
    user_id = models.IntegerField(db_index=True, default=0)

    def __unicode__(self):
        return self.title

    @permalink
    def get_absolute_url(self):
        return ('view_blog_post', None, { 'slug': self.slug })


class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def __unicode__(self):
        return self.title

    @permalink
    def get_absolute_url(self):
        return ('view_blog_category', None, { 'slug': self.slug })