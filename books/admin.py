from django.contrib import admin

# Register your models here.
from books.models import BookInfo, PersonInfo, AreaInfo, NewsInfo


class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['btitle', 'bpub_date', 'bread', 'bcomment', 'isDelete']

admin.site.register(BookInfo,BookInfoAdmin)

class PersonInfoAdmin(admin.ModelAdmin):
    list_display = ['pname', 'pgender', 'isDelete', 'pcomment']

admin.site.register(PersonInfo,PersonInfoAdmin)

class AreaInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'atitle', 'aParent']

admin.site.register(AreaInfo,AreaInfoAdmin)

class NewsInfoAdmin(admin.ModelAdmin):
    list_display = ['ntitle','ncontent','npub_date']

admin.site.register(NewsInfo,NewsInfoAdmin)