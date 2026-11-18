from django.contrib import admin
from .models import Campaign, CampaignSlot


class CampaignSlotInline(admin.TabularInline):
    model = CampaignSlot
    extra = 1
    fields = [
        "race",
        "tickets_available",
        "selection_method",
        "target_gender",
        "required_platform",
        "require_public_post",
        "brand_provides_product",
        "sponsor_deliverables",
    ]


@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "brand",
        "event",
        "status",
        "application_deadline",
        "total_tickets",
        "created_at",
    ]
    list_filter = ["status", "event", "created_at"]
    search_fields = ["title", "description", "brand__username", "brand__email", "event__name"]
    readonly_fields = ["created_at", "updated_at"]
    inlines = [CampaignSlotInline]

    @admin.display(description="Total Tickets")
    def total_tickets(self, obj):
        return sum(slot.tickets_available for slot in obj.slots.all())


@admin.register(CampaignSlot)
class CampaignSlotAdmin(admin.ModelAdmin):
    list_display = [
        "campaign",
        "race",
        "tickets_available",
        "selection_method",
        "target_gender",
        "required_platform",
        "brand_provides_product",
    ]
    list_filter = [
        "selection_method",
        "target_gender",
        "required_platform",
        "brand_provides_product",
        "campaign__event",
    ]
    search_fields = ["campaign__title", "race__name", "sponsor_deliverables"]