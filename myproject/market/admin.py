from django.contrib import admin
from .models import *
# Register your models here.


class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'page_count', 'category', 'published')
    list_display_links = ('name',)
    search_fields = ('name',)
    list_filter = ('author',) 


admin.site.register(Book, BookAdmin)
admin.site.register(Category)
admin.site.register(Author)
