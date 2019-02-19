from django.contrib import admin
from .models import Post, Comment
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status')
    list_filter = ('status', 'created', 'updated')
    
    prepopulated_fields = {'slug':('title',)}
    list_editable = ('status',)
    date_hierarchy = ('created')
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)