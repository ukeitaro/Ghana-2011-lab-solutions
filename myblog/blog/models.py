from django.db import models
from django.contrib import admin

class Blog(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    def __unicode__(self):
        return str(self.title)

class Comment(models.Model):
    body = models.TextField()
    author = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    post = models.ForeignKey(Blog)

    def body_first_60(self):
        return self.body[:30]

    def __unicode__(self):
        return str(self.body[:100])

# Admin stuff
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post','author','body_first_60','created','updated')
    list_filter = ('author','created')

class CommentInline(admin.StackedInline):
    model = Comment

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','created','updated')
    inlines = [CommentInline]
    search_fields = ('title','body')
    list_filter=('created',)

admin.site.register(Blog,BlogAdmin)
admin.site.register(Comment,CommentAdmin)
