from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
# from .models import CustomUser, Post, Category

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'username', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    search_fields = ('email', 'username')
    ordering = ('email',)

# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     list_display = ('title', 'author', 'created_at', 'is_featured')
#     prepopulated_fields = {'slug': ('title',)}

# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('name', 'color')
