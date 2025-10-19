from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class MotoImage(models.Model):
    """Model that represents motorcycle images.

    Only stores the image file (besides the default id field).
    """

    image = models.ImageField(upload_to="moto_images/")

    class Meta:
        verbose_name = "Moto Image"
        verbose_name_plural = "Moto Images"

    def __str__(self) -> str:  # pragma: no cover - trivial
        return f"MotoImage {self.pk}"
