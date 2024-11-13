from django.db.models import Sum

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from core.models import Pedido
from core.serializers import PedidoSerializer, TotalSerializer, PedidoCreateSerializer


class PedidoViewSet(ModelViewSet):
    queryset = Pedido.objects.all().order_by("id")

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return PedidoSerializer
        else:
            return PedidoCreateSerializer


    @action(detail=False, methods=["get"], url_path="total")
    def total(self, request, *args, **kwargs):
        total = Pedido.objects.aggregate(total=Sum("produto__valor"))["total"] or 0
        serializer = TotalSerializer({"total": total})
        return Response(serializer.data)
