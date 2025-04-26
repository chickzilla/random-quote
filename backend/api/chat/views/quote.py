from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from chat.models import Quote
import random

class SubmitQuote(APIView):
    def post(self, request):
        text = request.data.get('text')
        if text:
            
            if len(text) > 255:
                return Response({'error': 'Text must not be more than 255 characters.'}, status=status.HTTP_400_BAD_REQUEST)
            quote = Quote.objects.create(text=text, user_id=1)
            return Response({'id': quote.id, 'message': 'Quote submitted successfully!'})
        else:
            return Response({'error': 'Text are required.'}, status=400)

class RandomQuote(APIView):
    def get(self, request):
        quotes = list(Quote.objects.all())
        if quotes:
            random_quotes = random.sample(quotes, min(5, len(quotes)))
            result = [
                {
                    'username': quote.user.username, 
                    'text': quote.text
                }
                for quote in random_quotes
            ]
            return Response(result)
        else:
            return Response({'error': 'No quotes found.'}, status=404)
