from django.http import HttpResponse

from .models import ShortUrl
from .serializers import ShortUrlSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

def index(request):
    return HttpResponse("Hello, world. You're at the api index.")

class ShortUrlCreateView(CreateAPIView):

    def post(self, request, format=None):

        # Run serializer validation on the request arguments, and return an error message 
        # if the user didn't provide all the expected arguments correctly
        serializer = ShortUrlSerializer(data = request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)

        return Response(200)
