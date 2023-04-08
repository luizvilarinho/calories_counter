from django.urls import path
from api.views import AlimentoList, AlimentoDetail, CalcularCalorias

urlpatterns = [
    path("", AlimentoList.as_view({'get': 'list'}), name="alimento_list"),
    path('<int:id>', AlimentoDetail.as_view()),
    path('calcular', CalcularCalorias.as_view({'get': 'list'}))
]
