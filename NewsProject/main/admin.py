from django.contrib import admin
from django.utils.safestring import mark_safe
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import Human, Profession


class HumanAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Human
        fields = '__all__'


class HumanAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'last_name', 'get_photo', 'profession', 'sex', 'age', 'born_at')
    list_display_links = ('id', 'get_photo')
    search_fields = ('id', 'name', 'last_name', 'age')
    list_filter = ('id', 'age')
    list_editable = ['profession']
    fields = ('name', 'last_name', 'photo', 'profession', 'sex', 'age', 'born_at')
    readonly_fields = ('age', 'born_at')
    form = HumanAdminForm

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75">')
        else:
            return 'Фото отстутствует'

    get_photo_description = 'Фотокарточка'


class ProfessionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')


admin.site.register(Human, HumanAdmin)
admin.site.register(Profession, ProfessionAdmin)

admin.site.site_title = 'Страница администратора'
admin.site.site_header = 'Страница администратора'
admin.site.index_title = 'Администрирование сайта'
