from django.contrib import admin

from .models import MotoImage


@admin.register(MotoImage)
class MotoImageAdmin(admin.ModelAdmin):
    list_display = ("id", "image")
    readonly_fields = ("id",)
