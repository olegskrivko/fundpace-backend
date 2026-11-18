from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models

from events.models import Event, Race


class Campaign(models.Model):
    class Status(models.TextChoices):
        DRAFT = "draft", "Draft"
        ACTIVE = "active", "Active"
        CLOSED = "closed", "Closed"

    brand = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="campaigns",
    )
    event = models.ForeignKey(
        Event,
        on_delete=models.PROTECT,
        related_name="campaigns",
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.DRAFT,
    )
    application_deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"{self.title} ({self.event.name})"


class CampaignSlot(models.Model):
    class SelectionMethod(models.TextChoices):
        MANUAL = "manual", "Brand Selects Manually"
        RANDOM = "random", "Random Draw Among Eligible Runners"

    class TargetGender(models.TextChoices):
        ANY = "any", "Any Gender"
        FEMALE = "female", "Female Only"
        MALE = "male", "Male Only"

    class SocialPlatform(models.TextChoices):
        NONE = "none", "No Social Post Required"
        INSTAGRAM = "instagram", "Instagram (Public Post / Story)"
        STRAVA = "strava", "Strava Activity Photo"
        FACEBOOK = "facebook", "Facebook Public Post"
        ANY = "any", "Any of Instagram / Strava / Facebook"

    campaign = models.ForeignKey(
        Campaign,
        on_delete=models.CASCADE,
        related_name="slots",
    )
    race = models.ForeignKey(
        Race,
        on_delete=models.PROTECT,
        related_name="campaign_slots",
    )
    tickets_available = models.PositiveIntegerField(
        validators=[MinValueValidator(1)],
        help_text="Number of free race entries sponsored in this slot.",
    )
    selection_method = models.CharField(
        max_length=20,
        choices=SelectionMethod.choices,
        default=SelectionMethod.MANUAL,
    )
    target_gender = models.CharField(
        max_length=10,
        choices=TargetGender.choices,
        default=TargetGender.ANY,
    )

    # --- Social & Brand Deliverables ---
    required_platform = models.CharField(
        max_length=20,
        choices=SocialPlatform.choices,
        default=SocialPlatform.INSTAGRAM,
    )
    require_public_post = models.BooleanField(
        default=True,
        help_text="Athlete must have a public profile and tag the brand + @fundpace.",
    )
    brand_provides_product = models.BooleanField(
        default=False,
        help_text="True if the brand provides physical gear, apparel, food, or drinks for the athlete.",
    )
    sponsor_deliverables = models.TextField(
        blank=True,
        help_text=(
            "What the brand provides and what the athlete must do "
            "(e.g., wear our t-shirt, drink Monster at the finish line, tag @brand and @fundpace)."
        ),
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["campaign", "race", "target_gender"],
                name="unique_campaign_race_gender_slot",
            )
        ]

    def clean(self):
        super().clean()
        if self.campaign_id and self.race_id:
            if self.race.event_id != self.campaign.event_id:
                raise ValidationError(
                    {"race": "Selected race must belong to the campaign's event."}
                )
        if self.required_platform == self.SocialPlatform.NONE and self.require_public_post:
            raise ValidationError(
                {"require_public_post": "Cannot require a public post when social platform is 'none'."}
            )

    def __str__(self) -> str:
        return f"{self.campaign.title} - {self.race.name} ({self.tickets_available}x)"