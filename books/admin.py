from django.contrib import admin

from .models import books, comments
@admin.register(comments)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'text', 'book', 'datetime_created','is_active','recommend',)


admin.site.register(books)
# admin.site.register(comments)