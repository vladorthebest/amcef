from rest_framework.response import Response
from rest_framework.views import APIView
from main.models import UserPost
from .serializers import PostSerializer, APIPostSerializer
from django.db.models import Q
import requests
from django.core.exceptions import ObjectDoesNotExist

class APIplaceholder:

    @staticmethod
    def check_userid(user_id):
        response = requests.get(f"https://jsonplaceholder.typicode.com/users?id={user_id}")
        if not response.json():
            return False
        return True
    

    @staticmethod
    def check_postid(id):
        response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{id}")
        if not response.json():
            return False
        return True


    @staticmethod
    def get_post(id):
        response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{id}")
        return response.json()


    @staticmethod
    def save_post(id):
        if not APIplaceholder.check_postid(id):
            return False
        serializer = APIPostSerializer(data=APIplaceholder.get_post(id))
        print(serializer)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return True
        else:
            return False
    
    @staticmethod
    def check_userid(user_id):
        response = requests.get(f"https://jsonplaceholder.typicode.com/users?id={user_id}")
        if not response.json():
            return False
        return True




class PostAPIView(APIView):

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
        return Response({'status': False})
    

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
            return Response({"status": "Has not ID"})
        UserPost.objects.filter(id=pk).delete()
        return Response({"status": "ok"})