from django.contrib import admin
from .models import Flan, ContactForm, Category, Post, Comment

@admin.register(Flan)
class FlanAdmin(admin.ModelAdmin):
    list_display = ('name','description','is_private','price')
    prepopulated_fields = {'slug': ('name',),}
    list_filter = ('is_private',)
    search_fields = ('name',)

admin.site.register(ContactForm)
admin.site.register(Category)

@admin.register(Post)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title','id','status','slug','author')
    prepopulated_fields = {'slug': ('title',),}

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post','name','email','publish','status')
    list_filter = ('status','publish')
    search_fields = ('name','email','content')

# Register your models here.
