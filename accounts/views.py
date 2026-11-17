from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class AccountsHomeView(APIView):
    """
    Temporary view for testing accounts endpoint.
    """
    def get(self, request):
        return Response({"message": "Hello from Accounts API!"}, status=status.HTTP_200_OK)