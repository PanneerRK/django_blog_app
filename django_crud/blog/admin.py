from django.contrib import admin
from .models import Post, Category, AboutUs, Subcategory
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from unfold.admin import ModelAdmin
from django import forms

admin.site.unregister(User)
admin.site.unregister(Group)

@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if not obj:  # This ensures we're dealing with the "Add User" form
            form.base_fields['password1'].widget.attrs.update({'class': 'border bg-white font-medium min-w-20 rounded-md shadow-sm text-font-default-light text-sm focus:ring focus:ring-primary-300 focus:border-primary-600 focus:outline-none group-[.errors]:border-red-600 group-[.errors]:focus:ring-red-200 dark:bg-gray-900 dark:border-gray-700 dark:text-font-default-dark dark:focus:border-primary-600 dark:focus:ring-primary-700 dark:focus:ring-opacity-50 dark:group-[.errors]:border-red-500 dark:group-[.errors]:focus:ring-red-600/40 px-3 py-2 w-full max-w-2xl'})
            form.base_fields['password2'].widget.attrs.update({'class': 'border bg-white font-medium min-w-20 rounded-md shadow-sm text-font-default-light text-sm focus:ring focus:ring-primary-300 focus:border-primary-600 focus:outline-none group-[.errors]:border-red-600 group-[.errors]:focus:ring-red-200 dark:bg-gray-900 dark:border-gray-700 dark:text-font-default-dark dark:focus:border-primary-600 dark:focus:ring-primary-700 dark:focus:ring-opacity-50 dark:group-[.errors]:border-red-500 dark:group-[.errors]:focus:ring-red-600/40 px-3 py-2 w-full max-w-2xl'})
        return form

@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'category', 'subcategory', 'img_url']
    
    class Media:
        js = ('admin/js/vendor/jquery/jquery.js', 'js/admin/dependent_dropdown.js')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add 'form-control' class to category and subcategory fields
        self.fields['category'].widget.attrs.update({'class': 'form-control'})
        self.fields['subcategory'].widget.attrs.update({'class': 'form-control'})

class PostAdmin(ModelAdmin):    
    list_display = ('title', 'content', 'category', 'subcategory')
    search_fields = ('title', 'content')
    list_filter = ('category', 'created_at')
    form = PostForm

# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Category, ModelAdmin)
admin.site.register(Subcategory, ModelAdmin)
admin.site.register(AboutUs, ModelAdmin)