from .serializers import APIPostSerializer
import requests

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

