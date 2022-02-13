from django.contrib import admin

from .models import Worker, AStore, Visit


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    search_fields = ('name',)


@admin.register(AStore)
class AStoreAdmin(admin.ModelAdmin):
    search_fields = ('title',)


@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = ('id',)
    search_fields = ('astore__title',)