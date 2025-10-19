from rest_framework import pagination, viewsets

from .models import MotoImage
from .serializers.moto_image import MotoImageSerializer


class StandardResultsSetPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100


class MotoImageViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet that currently only exposes list (paginated) for MotoImage.

    Authentication is required to access the endpoint.
    """

    queryset = MotoImage.objects.all().order_by("-id")
    serializer_class = MotoImageSerializer
    pagination_class = StandardResultsSetPagination
