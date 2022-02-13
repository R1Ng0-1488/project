from rest_framework.views import APIView 
from rest_framework.response import Response
# Create your views here.

from .models import Worker, AStore, Visit
from .serializers import AStoreSerializer, VisitSerializer
# from .main import serializers


class AStoreListView(APIView):
    """Класс списка торговых точек полученный по номеру телефона"""
    serializer_class = AStoreSerializer

    def post(self, request, *args, **kwargs):
        phone = request.data.get('phone')
        if phone:
            queryset = AStore.objects.filter(worker__phone=phone)
            serializer = self.serializer_class(queryset, many=True)
            return Response(serializer.data)
        return Response({'error': 'there is no phone'})


class CreateVisitView(APIView):
    """Класс создания посещения на данной торговой точке"""
    serializer_class = VisitSerializer

    def post(self, request, *args, **kwargs):
        serailizer = self.serializer_class(data=request.data)
        if serailizer.is_valid():
            obj = serailizer.save()
            return Response({
                'pk': obj.pk,
                'datetime': obj.datetime
            })
        return Response({'error': serailizer.errors})