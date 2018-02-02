from django.db import models
from django.utils import timezone
from django.urls import reverse

def upload_location(instance, filename):
    #filebase, extension = filename.split(".")
    #return "%s/%s.%s" %(instance.id, filename, extension)
    return "%s/%s" %(instance.id, filename)

class Category(models.Model):
    title = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['title']

    def __str__(self):
        return self.title    

class Post(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.PROTECT)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to=upload_location,
        blank=True,
        null=True,
        width_field="width_field",
        height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    video_key = models.CharField(max_length=12)
    is_public = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['id']

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Comment(models.Model):
    # Post : Comment = 1 : N
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    author = models.CharField(max_length=10)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(auto_now=True)

    def get_edit_url(self):
        return reverse('comment_edit', args=[self.post.pk, self.pk])

    def get_delete_url(self):
        return reverse('comment_delete', args=[self.post.pk, self.pk])

    