from .models import ShortUrl, SHORT_URL_DOMAIN
from .serializers import ShortUrlSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

import random, string 

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

        # Create the full URL with the domain 'tier.app'
        fullShortUrl = SHORT_URL_DOMAIN + newShortUrl.shortUrl

        return Response({'shortUrl': fullShortUrl}, 200)
    
    def get(self, request, format=None):

        # Get the shortUrl query argument, returning an error message if it's empty or not present
        shortUrlArg = request.GET.get('shortUrl', '')
        if shortUrlArg == '':
            return Response({'errorMessage': 'Please provide a shortUrl query parameter'}, 400)

        # Get the corresponding ShortUrl object from the database
        shortUrlNoDomain = shortUrlArg.replace(SHORT_URL_DOMAIN, '')
        correspondingShortUrlObject = ShortUrl.objects.filter(shortUrl=shortUrlNoDomain)

        # If a corresponding ShortUrl object exists, return its real url
        # Otherwise, return an error message
        if correspondingShortUrlObject.count() == 1:
            return Response({'realUrl': correspondingShortUrlObject.first().realUrl}, 200)
        else:
            return Response({'errorMessage': f"The shortUrl parameter '{shortUrlArg}' is invalid. Please provide a valid shortUrl"}, 400)

# Generates a random string consisting of lower case letters
# of length <length>
# Credits: https://pynative.com/python-generate-random-string/
def generateShortUrlPath(length):

    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))

    return result_str