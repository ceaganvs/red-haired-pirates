from django.contrib import admin
from .models import CrewMember


@admin.register(CrewMember)
class CrewMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'hometown', 'age', 'joined_date')
    list_filter = ('role', 'joined_date')
    search_fields = ('name', 'email', 'hometown')
    readonly_fields = ('joined_date',)
