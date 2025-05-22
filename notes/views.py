from rest_framework.decorators import api_view
from rest_framework.response import Response
from clerk import Clerk  # pip install clerk-sdk

@api_view(["GET"])
def hello(request):
    return Response({"message": "Hello from Django on Railway!"})
