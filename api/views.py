from django.http import HttpResponse

from .models import ShortUrl
from .serializers import ShortUrlSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

import random, string 

def index(request):
    return HttpResponse("Hello, world. You're at the api index.")

class ShortUrlCreateView(CreateAPIView):

    def post(self, request, format=None):

        # Run serializer validation on the request arguments, and return an error message 
        # if the user didn't provide all the expected arguments correctly
        serializer = ShortUrlSerializer(data = request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)

        # Generate the shortUrl
        randomShortUrl = generateShortUrlPath(10)

        # Create the ShortUrl object
        newShortUrl = ShortUrl.objects.create(realUrl=request.data['realUrl'])
        newShortUrl.shortUrl = randomShortUrl
        newShortUrl.save()

        return Response(newShortUrl.shortUrl, 200)

# Generates a random string consisting of lower case letters
# of length <length>
# Credits: https://pynative.com/python-generate-random-string/
def generateShortUrlPath(length):

    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))

    return result_str