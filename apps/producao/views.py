from rest_framework.response import Response
from rest_framework.views import APIView
from apps.producao.models.produtos import Produtos
from apps.producao.models.producao import Producao
from apps.producao.serializers.produtos import ProdutosSerializer
from apps.producao.serializers.producao import ProducaoSerializer, ProducaoSerializerRead, ProducaoEstoqueSerializer
from rest_framework import status
from apps.producao.models.producao import ProducaoItem, ProdutoEstoque
from django.shortcuts import get_object_or_404
from decimal import Decimal


class ProducaoView(APIView):
    serializer_class = ProducaoSerializer
    def get(self, request, id=None):
        if id:
            try:
                search_query = Producao.objects.get(pk=id)
                search_item = ProducaoSerializerRead(search_query).data
                return Response(search_item, status=status.HTTP_200_OK)
            except Produtos.DoesNotExist:
                return Response({"error": "Item not found"}, status=status.HTTP_404_NOT_FOUND)
        items = Producao.objects.all()
        result = ProducaoSerializerRead(items, many=True ).data
        return Response(result, status=status.HTTP_200_OK)

    def post(self, request, id=None):
        serializer_producao = self.serializer_class(data=request.data)
        if serializer_producao.is_valid():
            serializer_producao.save()
            return Response(serializer_producao.data, status=status.HTTP_201_CREATED)
        return Response(serializer_producao.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id=None):
        producao = Producao.objects.get(id=id)
        producao.status = 'F'
        producao_items = request.data.get('producao_items', [])

        quantidade_total = Decimal(0)
        
        for item in producao_items:
            item_query = ProducaoItem.objects.get(id=item['id'])
            item_query.quantidade = item['quantidade']
            item_query.save()

            quantidade_total += Decimal(item['quantidade'])
            product_type = Produtos.objects.get(pk=item['produto']['id'])

            stock_item, created = ProdutoEstoque.objects.get_or_create(produto=product_type)

            if not created:
                stock_item.quantidade += Decimal(item['quantidade'])
            else:
                stock_item.quantidade = Decimal(item['quantidade'])
            
            stock_item.save()

        producao.quantidade = quantidade_total
        producao.save()
        return Response(status=status.HTTP_201_CREATED)

class ProdutosView(APIView):
    serializer_class = ProdutosSerializer
    def get(self, request, id=None):
        if id:
            try:
                search_query = Produtos.objects.get(pk=id)
                search_item = ProdutosSerializer(search_query).data
                return Response(search_item, status=status.HTTP_200_OK)
            except Produtos.DoesNotExist:
                return Response({"error": "Item not found"}, status=status.HTTP_404_NOT_FOUND)

        item_query = Produtos.objects.all()
        items = self.serializer_class(item_query, many=True ).data
        return Response(items, status=status.HTTP_200_OK)

    def post(self, request, id=None):
        serializer_produto = self.serializer_class(data=request.data)
        if serializer_produto.is_valid():
            serializer_produto.save()
            return Response(serializer_produto.data, status=status.HTTP_201_CREATED)
        return Response(serializer_produto.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id=None):
        item = get_object_or_404(Produtos.objects.all(), pk=id)
        serializer_produto = self.serializer_class(instance=item, data=request.data, partial=True)
        if serializer_produto.is_valid():
            serializer_produto.save()
            return Response(serializer_produto.data, status=status.HTTP_200_OK)
        return Response(serializer_produto.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id=None):
        item = get_object_or_404(Produtos.objects.filter(pk=id))
        item.delete()
        return Response({"message": f"Product with id {id} has been deleted."}, status=status.HTTP_204_NO_CONTENT)

class ProdutoEstoqueView(APIView):
    serializer_class = ProducaoEstoqueSerializer
    def get(self, request):
        items = ProdutoEstoque.objects.all()
        result = self.serializer_class(items, many=True).data
        return Response(result, status=status.HTTP_200_OK)

