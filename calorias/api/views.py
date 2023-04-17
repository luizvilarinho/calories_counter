from django.http import HttpResponse, JsonResponse
from rest_framework import generics, viewsets
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from api.calorias_service import calcular_calorias
from api.models import Calories
from api.serializers import CaloriasSerializer, AlimentosSerializer


class CalcularCalorias(viewsets.ModelViewSet):

    queryset = Calories.objects.all()
    serializer_class = CaloriasSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        alimento = Calories.objects.get(id=data['id_alimento'])

        calcularDict = {
            "alimento": alimento,
            "quantidade": data['quantidade']
        }

        macros = calcular_calorias(calcularDict)
        serializer = CaloriasSerializer(macros).data

        return Response({"success": True, "response": serializer})

class AlimentoList(viewsets.ModelViewSet):
    queryset = Calories.objects.all()
    serializer_class = AlimentosSerializer

class AlimentoDetail(RetrieveAPIView):
    queryset = Calories.objects.all()
    serializer_class = CaloriasSerializer
    lookup_url_kwarg = 'id'

