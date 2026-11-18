from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Role(models.TextChoices):
        ATHLETE = "athlete", "Athlete"
        BRAND = "brand", "Brand"

    email = models.EmailField(unique=True)
    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.ATHLETE,
    )

    REQUIRED_FIELDS = ["email"]

    def __str__(self) -> str:
        return f"{self.username} ({self.role})"


class AthleteProfile(models.Model):
    class Gender(models.TextChoices):
        MALE = "male", "Male"
        FEMALE = "female", "Female"

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="athlete_profile",
    )
    gender = models.CharField(
        max_length=10,
        choices=Gender.choices,
        blank=True,
        help_text="Required to apply for gender-specific campaign slots.",
    )
    # Sportista personīgie kanāli (kur publicēs atskaites)
    instagram_handle = models.CharField(
        max_length=100,
        blank=True,
        help_text="@handle",
    )
    strava_profile_url = models.URLField(
        blank=True,
        help_text="Link to Strava profile",
    )
    facebook_handle = models.CharField(
        max_length=100,
        blank=True,
    )

    # Reputācijas kontrole, ja neizpilda kampaņas nosacījumus
    is_banned = models.BooleanField(
        default=False,
        help_text="Banned athletes cannot apply for new campaigns.",
    )
    ban_reason = models.TextField(blank=True)

    def __str__(self) -> str:
        return f"Athlete: {self.user.username}"


class BrandProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="brand_profile",
    )
    company_name = models.CharField(max_length=255)
    website = models.URLField(blank=True)

    # Brenda publiskie kanāli (ieskaitot LinkedIn IT uzņēmumiem)
    instagram_handle = models.CharField(
        max_length=100,
        blank=True,
        help_text="Brand IG @handle",
    )
    linkedin_url = models.URLField(
        blank=True,
        help_text="Brand LinkedIn company page URL",
    )
    facebook_url = models.URLField(
        blank=True,
        help_text="Brand Facebook page URL",
    )

    # Verifikācija un kontrole
    is_verified = models.BooleanField(
        default=False,
        help_text="Designates whether this brand is verified by admin to publish campaigns.",
    )
    admin_notes = models.TextField(
        blank=True,
        help_text="Internal notes on verification, suspension, or company registration details.",
    )

    def __str__(self) -> str:
        return f"Brand: {self.company_name}"