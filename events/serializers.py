from rest_framework import serializers
from .models import Event, Race


class RaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Race
        fields = [
            "id", 
            "event", 
            "name", 
            "distance_km", 
            "race_date", 
            "start_time"
        ]

    def validate(self, attrs):
        event = attrs.get("event") or getattr(self.instance, "event", None)
        race_date = attrs.get("race_date") or getattr(self.instance, "race_date", None)

        if event and race_date:
            if not (event.start_date <= race_date <= event.end_date):
                raise serializers.ValidationError(
                    {
                        "race_date": (
                            f"Race date must fall within the event dates "
                            f"({event.start_date} to {event.end_date})."
                        )
                    }
                )
        return attrs


class EventSerializer(serializers.ModelSerializer):
    # Nested read-only list so GET /api/events/ returns the event with its races
    races = RaceSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = [
            "id",
            "name",
            "location",
            "start_date",
            "end_date",
            "description",
            "website",
            "races",
        ]

    def validate(self, attrs):
        start_date = attrs.get("start_date") or getattr(self.instance, "start_date", None)
        end_date = attrs.get("end_date") or getattr(self.instance, "end_date", None)

        if start_date and end_date and end_date < start_date:
            raise serializers.ValidationError(
                {"end_date": "Event end date cannot precede its start date."}
            )
        return attrs