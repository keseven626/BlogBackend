from django.contrib import admin
from .models import *

# Register your models here
admin.site.site_header = "InsideDepth Admin" 
admin.site.register(Category)
admin.site.register(Comment)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):        
          list_display  = ('id', 'title', 'created', 'publish')

