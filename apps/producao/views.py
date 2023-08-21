from rest_framework.response import Response
from rest_framework.views import APIView
from apps.producao.models.produtos import Produtos
from apps.producao.models.producao import Producao
from apps.producao.serializers.produtos import ProdutosSerializer
from apps.producao.serializers.producao import ProducaoSerializer, ProducaoSerializerRead
from rest_framework import status
from django.shortcuts import get_object_or_404


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
        return Response({'':''})
    
    def delete(self, request, id=None):
        return Response({'':''})




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
        return Response({'':''})

    def put(self, request, id=None):
        return Response({'':''})
    
    def delete(self, request, id=None):
        return Response({'':''})
