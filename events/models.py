from django.db import models
from django.core.exceptions import ValidationError


class Event(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField(blank=True)
    website = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["start_date", "name"]
        constraints = [
            models.CheckConstraint(
                condition=models.Q(end_date__gte=models.F("start_date")),
                name="event_end_date_gte_start_date",
            )
        ]

    def clean(self):
        super().clean()
        if self.start_date and self.end_date and self.start_date > self.end_date:
            raise ValidationError({"end_date": "End date cannot precede start date."})

    def __str__(self) -> str:
        return f"{self.name} ({self.start_date})"


class Race(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="races")
    name = models.CharField(max_length=255)
    distance_km = models.DecimalField(max_digits=9, decimal_places=4)
    race_date = models.DateField()
    start_time = models.TimeField(null=True, blank=True)

    class Meta:
        ordering = ["race_date", "start_time", "distance_km"]

    def clean(self):
        super().clean()
        if self.event_id and self.race_date:
            if not (self.event.start_date <= self.race_date <= self.event.end_date):
                raise ValidationError(
                    {
                        "race_date": (
                            f"Race date must fall between {self.event.start_date} "
                            f"and {self.event.end_date}."
                        )
                    }
                )

    def __str__(self) -> str:
        return f"{self.event.name} - {self.name} ({self.distance_km} km)"
