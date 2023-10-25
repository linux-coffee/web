from django.contrib import admin
from .models import Home,Comment,Aboutme

@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created')
    search_fields = ('title', 'decriptions')
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']
    def approve_comments(self, request, queryset):
        queryset.update(active=True)

@admin.register(Aboutme)
class AboutmeAdmin(admin.ModelAdmin):
    list_display = ('name','created')