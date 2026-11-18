from django.contrib import admin
from .models import Event, Race


class RaceInline(admin.TabularInline):
    model = Race
    extra = 1


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("name", "location", "start_date", "end_date")
    inlines = [RaceInline]


@admin.register(Race)
class RaceAdmin(admin.ModelAdmin):
    list_display = ("name", "event", "distance_km", "race_date", "start_time")
    list_filter = ("event", "race_date")