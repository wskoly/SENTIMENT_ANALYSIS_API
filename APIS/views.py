from rest_framework.views import APIView
from rest_framework.response import Response
from .analyzer import analyze

class AnalyzeAPIView(APIView):
    def post(self, request):
        if not request.data:
            # Return error response if JSON body is empty
            return Response({'error': 'Json body cannot be empty'}, status=400)
        
        if "text" not in request.data:
            # Return error response if the required field("text") is missing
            return Response({'error': 'Missing required fields'}, status=400)
        
        if request.data.get("text") == "":
            # Return error response if the value for the field("text") is missing
            return Response({'error': 'Value for text field is missing'}, status=400)
        
        try:
            # Perform sentiment analysis on the text
            sentiment = analyze(request.data.get("text"))
            return Response({'sentiment': sentiment})
        except:
            # Return error response if an unknown error occurs
            return Response({'error': 'Some unknown error occurred'}, status=400)
