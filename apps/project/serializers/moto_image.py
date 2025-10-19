from django.conf import settings
from rest_framework import serializers

from ..models import MotoImage


class MotoImageSerializer(serializers.ModelSerializer):
    # return a full URL for the image depending on storage configuration
    image = serializers.SerializerMethodField()

    class Meta:
        model = MotoImage
        fields = ("id", "image")

    def get_image(self, obj):
        """Return full URL for the image.

        - If the ImageField already exposes an absolute URL, return it.
        - If USE_CLOUDINARY is True, build URL using CLOUDINARY_CLOUD_NAME.
        - Otherwise, use request.build_absolute_uri to create full URL for local media.
        """

        if not obj.image:
            return None

        # try to get the stored URL (may be relative)
        try:
            img_url = obj.image.url
        except Exception:
            return None

        # if already absolute, return as-is
        if isinstance(img_url, str) and img_url.startswith("http"):
            return img_url

        # if using Cloudinary, construct base URL
        if getattr(settings, "USE_CLOUDINARY", False):
            cloud_name = getattr(settings, "CLOUDINARY_CLOUD_NAME", "").strip()
            if cloud_name:
                # use the file name/path stored in the field
                name = getattr(obj.image, "name", "").lstrip("/")
                return f"https://res.cloudinary.com/{cloud_name}/{name}"

        # fallback: build absolute URI using request if available
        request = (
            self.context.get("request") if hasattr(self, "context") else None
        )
        if request is not None:
            return request.build_absolute_uri(img_url)

        # last resort, return whatever .url gives (could be relative)
        return img_url
