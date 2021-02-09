from django import forms
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
# from modeltranslation.admin import TranslationAdmin
from .models import Course, Category


# class TagAdmin(TranslationAdmin):
#     pass


# class PostAdminForm(forms.ModelForm):
#     """Форма с виджетом ckeditor"""
#     text_ru = forms.CharField(label="Описание [ru]", widget=CKEditorUploadingWidget())
#     class Meta:
#         model = Post
#         fields = '__all__'



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	"""docstring for PostAdmin"""
	list_display = ('id', 'name', 'url')
	list_display_links = ('name',)
	search_fields = ('name',)
	save_as = True

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'draft', 'created_at')
	list_display_links = ('title',)
	list_filter = ('created_at', 'draft')
	list_editable = ('draft',)
	search_fields = ('title',)
	save_as = True
	readonly_fields = ('created_at',)
	# form = PostAdminForm


# admin.site.register(Tag, TagAdmin)

admin.site.site_title='mirsaid.uz'
admin.site.site_header='mirsaid.uz'
# admin.site.index_title='mirsaid.uz'