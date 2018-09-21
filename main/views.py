from . import models
from rest_framework import permissions
from rest_framework.decorators import permission_classes
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import response, status


@permission_classes((permissions.AllowAny,))
class IndexListView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "zaebest/pages/index.html"

    def get(self, request):
        return response.Response(status=status.HTTP_200_OK)


@permission_classes((permissions.AllowAny,))
class SearchListView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "zaebest/pages/search.html"

    def get(self, request):
        return response.Response(status=status.HTTP_200_OK)


@permission_classes((permissions.AllowAny,))
class AddedPlacesListView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "zaebest/pages/added_places.html"

    def get(self, request):
        return response.Response(status=status.HTTP_200_OK)


@permission_classes((permissions.AllowAny,))
class LikedPlacesListView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "zaebest/pages/search.html"

    def get(self, request):
        return response.Response(status=status.HTTP_200_OK)
