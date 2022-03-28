import uuid
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Flan(models.Model):
    flan_uuid = models.UUIDField()
    name = models.CharField(max_length=64)
    description = models.TextField()
    image_url = models.URLField()
    slug = models.SlugField(unique=True)
    is_private = models.BooleanField()
    no_eggs = models.BooleanField(default=False)
    no_sugar = models.BooleanField(default=False)
    no_lactose = models.BooleanField(default=False)
    price = models.PositiveIntegerField(default=0)

class ContactForm(models.Model):
    contact_form_uuid = models.UUIDField(default=uuid.uuid4,editable=False)
    customer_email = models.EmailField()
    customer_name = models.CharField(max_length=64)
    message = models.TextField()

class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class Post(models.Model):

    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    options = (
        ('draft','Draft'),
        ('published','Published'),
    )            
    
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=255)
    image_url = models.URLField(default='http://pa1.narvii.com/6962/773484dfab00ca9fecc375a045ab58badc4582f2r1-360-360_00.gif')
    excerpt = models.TextField(null=True)
    content = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date='published', null=False, unique=True)
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    status = models.CharField(max_length=10, choices=options, default='draft')
    objects = models.Manager()
    postobjects = PostObjects()

    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.title

class Comment(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=50)
    email = models.EmailField()
    content = models.TextField()
    publish = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        ordering = ("publish",)

        def __str__(self) -> str:
            return f"Comment by {self.name}"