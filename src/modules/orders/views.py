from email.policy import HTTP
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from modules.inventory.serializers import ProductSerializer
from .serializers import OrderSerializer
from .models import Order

class OrderViews(APIView):
    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None):
        if id:
            try:
                item = Order.objects.get(id=id)
                serializer = OrderSerializer(item)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Order.DoesNotExist:
                raise Response("error", status=status.HTTP_400_BAD_REQUEST)
            
        items = Order.objects.all()
        serializer = OrderSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def patch(self, request, id=None):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    def delete(self, request, id=None):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)