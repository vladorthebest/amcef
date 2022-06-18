from rest_framework.response import Response
from rest_framework.views import APIView
from main.models import UserPost
from .serializers import PostSerializer
from django.db.models import Q
import requests
from django.core.exceptions import ObjectDoesNotExist


def check_userid(user_id):
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    for item in response.json():
        if item['id'] == user_id:
            return True
    return False

class PostAPIView(APIView):

    def get(self, request):
    
        userid = request.GET.get('userid')
        id = request.GET.get('id')

        try:
            item = UserPost.objects.get(id=id)
        except ObjectDoesNotExist:
            return Response({"status": "Post does"})

        if id or userid:
            items = UserPost.objects.filter(Q(userId=userid) | Q(id=id))
        else:   
            items = UserPost.objects.all()
        
        serialiser = PostSerializer(items, many=True)
        return Response(serialiser.data)


    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True) and check_userid(request.data['userId']):
            serializer.save()
            return Response(serializer.data)
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
        return Response(serializer.data)

def deletePost(request):
    id = request.GET.get('id')
    UserPost.objects.filter(id=id).delete()
    return Response({"status": "ok"})