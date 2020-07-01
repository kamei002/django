from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
import logging
logger = logging.getLogger("app")
# Create your views here.


class Index(APIView):
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request):
        data = {
        }
        return Response(data, template_name='app/index.html')
