from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.text import slugify




class Category(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self) -> str:
            return self.name 


from django.db import models
from django.template.defaultfilters import slugify
from django.conf import settings

class Post(models.Model):
    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status="published")

    options = (
        ("draft", "Draft"),
        ("published", "Published")
    )

    category = models.ForeignKey('Category', on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=200, unique=True)
    excerpt = models.TextField(null=True)
    content = models.TextField()
    slug = models.SlugField(max_length=250, blank=True)
    published = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blog_posts')
    status = models.CharField(max_length=10, choices=options, default='published')
    
    objects = models.Manager()  # default manager
    postobjects = PostObjects()  # custom manager to fetch only published posts

    class Meta:
        ordering = ("-published",)

    def save(self, *args, **kwargs):
        # Update slug if title changes
        if not self.slug or self.pk is None:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

