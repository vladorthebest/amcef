from rest_framework.response import Response
from rest_framework.views import APIView
from main.models import UserPost
from .serializers import PostSerializer, APIPostSerializer
from django.db.models import Q
import requests
from django.core.exceptions import ObjectDoesNotExist
from .PlaceholderAPI import APIplaceholder


class CreateGetAPIView(APIView):

    def get(self, request):

        userid = request.GET.get('userid')
        id = request.GET.get('id')
        if id:
            try:
                item = UserPost.objects.get(id=id)
            except ObjectDoesNotExist:
                if not  APIplaceholder.save_post(id):
                    return Response({'status': 'Incorrect ID'})
                
        if id or userid:
            items = UserPost.objects.filter(Q(userId=userid) | Q(id=id))
        else:   
            items = UserPost.objects.all()
        
        serialiser = PostSerializer(items, many=True)
        return Response(serialiser.data)


    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True) and APIplaceholder.check_userid(request.data['userId']):
            serializer.save()
            return Response({'status': True, 'data':serializer.data})
        return Response({'status': 'Incorrect userId'})
    


class PutDeleteAPIView(APIView):

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"status": "Method PUT not allowed"})

        try:
            item = UserPost.objects.get(id=pk)
        except ObjectDoesNotExist:
            return Response({"status": "Post does"})

        serializer = PostSerializer(data=request.data, instance=item)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'status': True, 'data':serializer.data})


    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"status": "Incorrect ID"})
        UserPost.objects.filter(id=pk).delete()
        return Response({"status": f"Post ID={pk} deleted!"})