from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.text import slugify




class Category(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self) -> str:
            return self.name 


class Post(models.Model):
      

    class PostObjects(models.Manager):
            def get_queryset(self)  :
                  return super().get_queryset().filter(status="published")
       
    options=(
            
            ("draft","Draft"),
            ("published","Published")
      ) 


    category=models.ForeignKey(Category,
                                 on_delete=models.CASCADE,default=1)
    title=models.CharField(max_length=200 ,unique=True)
    excerpt=models.TextField(null=True)
    content=models.TextField()
    slug=models.SlugField(max_length=250,unique_for_date="published",blank=True)
    published=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='blog_posts')
    status=models.CharField(max_length=10,choices=options,default=published)
    objects=models.Manager()
    postobjects=PostObjects() #custom


    class Meta:
        
        ordering=("-published",)
        
    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.title)
            super().save(*args, **kwargs)    

    def __str__(self):
         
         return self.title
        
    
             
   


