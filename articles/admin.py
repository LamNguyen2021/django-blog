from django.contrib import admin
from .models import Article

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
  list_display = ["title", "created_date"] # hien thi cac field cua model trong trang admin
  list_filter = ["created_date"] # hien thi bo loc theo ngay
  search_fields = ["title"] # hien thi thanh tim kiem theo title


admin.site.register(Article, ArticleAdmin)