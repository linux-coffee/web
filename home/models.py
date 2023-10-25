from django.db import models


class Home(models.Model):
    title = models.CharField(max_length = 100)
    body = models.TextField()
    decriptions = models.TextField(blank=True)
    author = models.CharField(max_length = 200,blank=True)
    img = models.ImageField(upload_to='posts',blank=True)
    created = models.DateTimeField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Home,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)

class Aboutme(models.Model):
    name = models.CharField(max_length = 200,blank=True)
    text = models.TextField()
    img = models.ImageField(blank=True,upload_to='posts')
    created = models.DateTimeField(auto_now_add=True)