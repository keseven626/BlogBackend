from django.db import models
from ckeditor.fields import RichTextField
# from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

user = get_user_model()
# Create your models here.


def post_image(instance, filename):
    return 'post/{filename}'.format(filename=filename)

class Category(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.name
                                                
class Post(models.Model):
    options = (
        ('draft', 'Draft'),
        ('publish', 'Publish')
    )
    title = models.CharField(max_length=250, blank=True, null=True)
    top_news = models.BooleanField(default=False)
    Author = models.ForeignKey(user, null=False, on_delete=models.CASCADE, default=1)
    content = RichTextField(blank=False, null=False)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    snippet = models.CharField(max_length=250, null=True, blank=True)
    image = models.ImageField(upload_to="post_image", null=True, blank=True)
    like = models.ManyToManyField(user, related_name='likes', blank=True)
    Allow_comment = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    publish = models.CharField(max_length=10, choices=options, default='draft')

    class Meta:
        ordering = ['-updated']

    def __str__(self):
        return self.title

class Comment(models.Model):
    content = models.CharField(max_length=300, null=True, blank=True)
    post_comment = models.ForeignKey(Post,null=False, related_name='comments', blank=False, on_delete=models.CASCADE)
    comment_author = models.ForeignKey(user,null=False, blank=False, on_delete=models.CASCADE )
    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


        