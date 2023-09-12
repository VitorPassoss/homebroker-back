from rest_framework.response import Response
from rest_framework.views import APIView
from apps.materia_prima.models.fornecedores import Fornecedores
from apps.materia_prima.models.insumos import Insumos
from apps.materia_prima.models.entrada import Entrada
from apps.materia_prima.models.estoque_insumo import EstoqueInsumo
from apps.materia_prima.serializers.fornecedores import FornecedoresSerializer
from apps.materia_prima.serializers.insumos import InsumosSerializer
from apps.materia_prima.serializers.entrada import EntradaSerializer, EntradaCreateSerializer
from apps.materia_prima.serializers.estoque_insumo import EstoqueSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404
from decimal import Decimal


class FornecedoresView(APIView):
    serializer_class = FornecedoresSerializer
    def get(self, request, id=None):
        if id:
            try:
                search_query = Fornecedores.objects.get(pk=id)
                search_item = FornecedoresSerializer(search_query).data
                return Response(search_item, status=status.HTTP_200_OK)
            except Fornecedores.DoesNotExist:
                return Response({"error": "Item not found"}, status=status.HTTP_404_NOT_FOUND)

        fornecedores_query = Fornecedores.objects.all()
        fornecedores = FornecedoresSerializer(fornecedores_query, many=True ).data
        return Response(fornecedores, status=status.HTTP_200_OK)

    def post(self, request):
        fornecedor_serializer = self.serializer_class(data=request.data)
        if fornecedor_serializer.is_valid():
            fornecedor_serializer.save()
            return Response(fornecedor_serializer.data, status=status.HTTP_201_CREATED)
        return Response(fornecedor_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id=None):
        saved_supplie= get_object_or_404(Fornecedores.objects.all(), pk=id)
        fornecedor_serializer = self.serializer_class(instance=saved_supplie, data=request.data, partial=True)
        if fornecedor_serializer.is_valid():
            fornecedor_serializer.save()
            return Response(fornecedor_serializer.data, status=status.HTTP_200_OK)
        return Response(fornecedor_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id=None):
        fornecedor = get_object_or_404(Fornecedores.objects.filter(pk=id))
        fornecedor.delete()
        return Response({"message": f"Product with id {id} has been deleted."}, status=status.HTTP_204_NO_CONTENT)


class InsumosView(APIView):
    serializer_class = InsumosSerializer
    def get(self, request, id=None):
        if id:
            try:
                search_query = Insumos.objects.get(pk=id)
                search_item = InsumosSerializer(search_query).data
                return Response(search_item, status=status.HTTP_200_OK)
            except Insumos.DoesNotExist:
                return Response({"error": "Item not found"}, status=status.HTTP_404_NOT_FOUND)
        
        insumos_query = Insumos.objects.all()
        insumos = InsumosSerializer(insumos_query, many=True).data
        return Response(insumos, status=status.HTTP_200_OK)

    def post(self, request):
        insumos_serializer = self.serializer_class(data=request.data)
        if insumos_serializer.is_valid():
            insumos_serializer.save()
            return Response(insumos_serializer.data, status=status.HTTP_201_CREATED)
        return Response(insumos_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id=None):
        saved_insumo = get_object_or_404(Insumos.objects.all(), pk=id)
        insumo_serializer = self.serializer_class(instance=saved_insumo, data=request.data, partial=True)
        if insumo_serializer.is_valid():
            insumo_serializer.save()
            return Response(insumo_serializer.data, status=status.HTTP_200_OK)
        return Response(insumo_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id=None):
        insumo = get_object_or_404(Insumos.objects.filter(pk=id))
        insumo.delete()
        return Response({"message": f"Product with id {id} has been deleted."}, status=status.HTTP_204_NO_CONTENT)


class EntradasView(APIView):
    serializer_class = EntradaSerializer
    def get(self, request, id=None):
        if id:
            entrada = get_object_or_404(Entrada, pk=id)
            data = self.serializer_class(entrada).data
            return Response(data, status=status.HTTP_200_OK)
        
        entradas = Entrada.objects.all()
        data = self.serializer_class(entradas, many=True).data
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = EntradaCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            self.addStock(request.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id=None):
        entrada = get_object_or_404(Entrada, pk=id)
        serializer = self.serializer_class(instance=entrada, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id=None):
        entrada = get_object_or_404(Entrada, pk=id)
        entrada.delete()
        return Response({"message": f"Entrada with id {id} has been deleted."}, status=status.HTTP_204_NO_CONTENT)

    def addStock(self, data):
        quantidade = data['quantidade']
        valor = data['valor']
        tipo_insumo = data['tipo_insumo']

        stock_item, created = EstoqueInsumo.objects.get_or_create(tipo_insumo_id=tipo_insumo)

        if not created:
            stock_item.quantidade += Decimal(quantidade)
            stock_item.valor += valor
        else:
            stock_item.quantidade = Decimal(quantidade)
            stock_item.valor = valor

        stock_item.save()



class EstoqueView(APIView):
    serializer_class = EstoqueSerializer
    def get(self, request, id=None):
        if id:
            estoque = get_object_or_404(EstoqueInsumo, pk=id)
            data = self.serializer_class(estoque).data
            return Response(data, status=status.HTTP_200_OK)
        
        estoque = EstoqueInsumo.objects.all()
        data = self.serializer_class(estoque, many=True).data
        return Response(data, status=status.HTTP_200_OK)

    def put(self, request, id=None):
        stock = get_object_or_404(EstoqueInsumo, pk=id)
        serializer = self.serializer_class(instance=stock, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id=None):
        stock = get_object_or_404(EstoqueInsumo, pk=id)
        stock.delete()
        return Response({"message": f"Item with id {id} has been deleted."}, status=status.HTTP_204_NO_CONTENT)