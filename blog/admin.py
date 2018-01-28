from django.contrib import admin
from .models import Post, Comment

class PostAdmin(admin.ModelAdmin):
	list_display = ('id', 'title','is_public','created_date','published_date')
	list_display_links = ['title']
	list_editable = ['is_public']

#class CommentAdmin(admin.ModelAdmin):
#	list_display = ('Comment')

admin.site.register(Post,PostAdmin)

#admin.site.register(Comment,CommentAdmin)
admin.site.register(Comment)