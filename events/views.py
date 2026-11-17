from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class EventsHomeView(APIView):
    """
    Temporary view for testing events endpoint.
    """
    def get(self, request):
        return Response({"message": "Hello from Events API!"}, status=status.HTTP_200_OK)