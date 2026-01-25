from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # This controls the columns you see in the admin list
    list_display = ('user', 'text_preview', 'created_at', 'photo_exists')
    
    # Adds a sidebar to filter by date or user
    list_filter = ('created_at', 'user')
    
    # Adds a search bar for the text content
    search_fields = ('text', 'user__username')

    # Custom methods to make the list look better
    def text_preview(self, obj):
        return obj.text[:50] + "..." if len(obj.text) > 50 else obj.text
    
    def photo_exists(self, obj):
        return bool(obj.photo)
    photo_exists.boolean = True # Shows a nice green checkmark icon