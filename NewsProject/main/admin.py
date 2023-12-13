from django.contrib import admin
from .models import Human, Profession


class HumanAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'last_name', 'photo', 'profession', 'sex', 'age', 'born_at')
    list_display_links = ('id', 'photo')
    search_fields = ('id', 'name', 'last_name', 'age')
    list_filter = ('id', 'age')
    list_editable = ['profession']


class ProfessionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')


admin.site.register(Human, HumanAdmin)
admin.site.register(Profession, ProfessionAdmin)
