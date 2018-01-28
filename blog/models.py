from django.db import models
from django.utils import timezone
from django.urls import reverse

class Post(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.PROTECT)
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(blank=True, null=True)
#   video = 
    is_public = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(auto_now=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail',args=[self.pk])

class Comment(models.Model):
    # Post : Comment = 1 : N
    post = models.ForeignKey(Post,on_delete=models.PROTECT)
    author = models.CharField(max_length=10)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']

    def get_edit_url(self):
        return reverse('comment_edit', args=[self.post.pk, self.pk])

    def get_delete_url(self):
        return reverse('comment_delete', args=[self.post.pk, self.pk])

    