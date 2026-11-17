from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class CampaignsHomeView(APIView):
    """
    Temporary view for testing campaigns endpoint.
    """
    def get(self, request):
        return Response({"message": "Hello from Campaigns API!"}, status=status.HTTP_200_OK)