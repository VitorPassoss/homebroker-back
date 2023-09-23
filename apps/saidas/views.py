from rest_framework.response import Response
from rest_framework.views import APIView
from apps.saidas.models.saida import Saida
from apps.saidas.models.destinacao import Destinacao
from apps.saidas.serializers.saida import SaidaSerializer, DestinacaoSerializer, SaidaSerializerRead
from apps.producao.models.producao import ProdutoEstoque
from apps.producao.models.produtos import Produtos
from apps.producao.serializers.produtos import ProdutosSerializer
from rest_framework import status
from decimal import Decimal
from django.shortcuts import get_object_or_404

class DestinacaoView(APIView):
    serializer_class = DestinacaoSerializer
    def get(self, request, id=None):
        if id:
            try:
                search_query = Destinacao.objects.get(pk=id)
                search_item = self.serializer_class(search_query).data
                return Response(search_item, status=status.HTTP_200_OK)
            except Destinacao.DoesNotExist:
                return Response({"error": "Item not found"}, status=status.HTTP_404_NOT_FOUND)

        item_query = Destinacao.objects.all()
        items = self.serializer_class(item_query, many=True ).data

   
        return Response(items, status=status.HTTP_200_OK)

    def post(self, request):
        item_serializer = self.serializer_class(data=request.data)
        if item_serializer.is_valid():
            item_serializer.save()
            return Response(item_serializer.data, status=status.HTTP_201_CREATED)
        return Response(item_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id=None):
        saved_supplie= get_object_or_404(Destinacao.objects.all(), pk=id)
        fornecedor_serializer = self.serializer_class(instance=saved_supplie, data=request.data, partial=True)
        if fornecedor_serializer.is_valid():
            fornecedor_serializer.save()
            return Response(fornecedor_serializer.data, status=status.HTTP_200_OK)
        return Response(fornecedor_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id=None):
        fornecedor = get_object_or_404(Destinacao.objects.filter(pk=id))
        fornecedor.delete()
        return Response({"message": f"Product with id {id} has been deleted."}, status=status.HTTP_204_NO_CONTENT)

class SaidasView(APIView):
    serializer_class = SaidaSerializer
    def get(self, request, id=None):
        if id:
            try:
                search_query = Saida.objects.get(pk=id)
                search_item = SaidaSerializerRead(search_query).data
                return Response(search_item, status=status.HTTP_200_OK)
            except Saida.DoesNotExist:   # I've corrected this from Destinacao.DoesNotExist to Saida.DoesNotExist
                return Response({"error": "Item not found"}, status=status.HTTP_404_NOT_FOUND)

        item_query = Saida.objects.all()
        items = SaidaSerializerRead(item_query, many=True).data
        for item in items:
            try:
                produto_obj = Produtos.objects.get(pk=item['id_ref'])
                item['produto'] = ProdutosSerializer(produto_obj).data  
            except Produtos.DoesNotExist:
                pass
        return Response(items, status=status.HTTP_200_OK)

    def post(self, request):
        item_serializer = self.serializer_class(data=request.data)
        if item_serializer.is_valid():
            item_serializer.save()
            quantidade = request.data.get('quantidade')
            id_ref = request.data.get('id_ref')
            stock_query = ProdutoEstoque.objects.get(produto_id=id_ref)
            stock_query.quantidade -= Decimal(quantidade)
            stock_query.save()
            return Response(item_serializer.data, status=status.HTTP_201_CREATED)
        return Response(item_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

