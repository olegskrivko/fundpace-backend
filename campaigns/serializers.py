from django.db import transaction
from rest_framework import serializers
from .models import Campaign, CampaignSlot


class CampaignSlotSerializer(serializers.ModelSerializer):
    race_name = serializers.CharField(source="race.name", read_only=True)
    distance_km = serializers.DecimalField(
        source="race.distance_km", max_digits=9, decimal_places=4, read_only=True
    )

    class Meta:
        model = CampaignSlot
        fields = [
            "id",
            "race",
            "race_name",
            "distance_km",
            "tickets_available",
            "selection_method",
            "target_gender",
            "required_platform",
            "require_public_post",
            "brand_provides_product",
            "sponsor_deliverables",
        ]


class CampaignSerializer(serializers.ModelSerializer):
    slots = CampaignSlotSerializer(many=True)
    event_name = serializers.CharField(source="event.name", read_only=True)
    brand_username = serializers.CharField(source="brand.username", read_only=True)

    class Meta:
        model = Campaign
        fields = [
            "id",
            "brand",
            "brand_username",
            "event",
            "event_name",
            "title",
            "description",
            "status",
            "application_deadline",
            "slots",
            "created_at",
        ]
        read_only_fields = ["brand", "created_at"]

    def validate(self, attrs):
        event = attrs.get("event")
        slots = attrs.get("slots", [])

        if not slots:
            raise serializers.ValidationError(
                {"slots": "A campaign must include at least one race ticket slot."}
            )

        for slot in slots:
            race = slot["race"]
            if race.event_id != event.id:
                raise serializers.ValidationError(
                    {"slots": f"Race '{race.name}' does not belong to event '{event.name}'."}
                )
            if (
                slot.get("required_platform") == CampaignSlot.SocialPlatform.NONE
                and slot.get("require_public_post", True)
            ):
                raise serializers.ValidationError(
                    {"slots": "Cannot require a public post when required_platform is 'none'."}
                )

        return attrs

    @transaction.atomic
    def create(self, validated_data):
        slots_data = validated_data.pop("slots")
        campaign = Campaign.objects.create(**validated_data)
        for slot_data in slots_data:
            CampaignSlot.objects.create(campaign=campaign, **slot_data)
        return campaign