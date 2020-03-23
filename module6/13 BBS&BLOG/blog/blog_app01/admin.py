from django.contrib import admin

# Register your models here.


from blog_app01 import models

admin.site.register(models.UserInfo)
admin.site.register(models.UserBlog)
admin.site.register(models.Category)
admin.site.register(models.Tag)
admin.site.register(models.Article)
admin.site.register(models.ArticleUpDown)
admin.site.register(models.Article2Tag)
admin.site.register(models.Comment)
