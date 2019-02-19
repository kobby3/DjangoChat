from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    
    STATUS_CHOICES = (
        ('draft','Draft'),
        ('published','Published'),
    )

    title               =       models.CharField(max_length=100)
    slug                =       models.SlugField(max_length=120)
   
    body                =       models.TextField()
    
    created             =       models.DateTimeField(auto_now_add=True)
    updated             =       models.DateTimeField(auto_now=True)
    status              =       models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    


    def __str__(self):
       return self.title

    def get_absalute_url(self):
        return 'chat/%d/%s' %(self.id, self.slug)

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.PROTECT)
    user = models.ForeignKey(User,on_delete=models.PROTECT)
    content = models.TextField(max_length=160)
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return '{}-{}'.format(self.post.title, str(self.user.username))