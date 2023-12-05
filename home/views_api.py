from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .utils import *

class LoginView(APIView):

    def post(self, request):
        response = {}
        response['status'] = 500
        response['message'] = 'Something went wrong'
        try:
            data = request.data

            if data.get('username') is None:
                response['message'] = 'key username not found'
                raise Exception('key username not found')

            if data.get('password') is None:
                response['message'] = 'key password not found'
                raise Exception('key password not found')

            check_user = User.objects.filter(
                username=data.get('username')).first()

            print("*"*20)
            print(check_user)
            print("*"*20)
            if check_user is None:
                response['message'] = 'invalid username, user not found'
                raise Exception('invalid username not found')

            print(data.get('username'), data.get('password'))
            user_obj = authenticate(username=data.get('username'),
                                    password=data.get('password'))
            if user_obj:
                print(request, user_obj)
                login(request, user_obj)
                response['status'] = 200
                response['message'] = 'Welcome'
            else:
                response['message'] = 'invalid password'
                raise Exception('invalid password')


        except Exception as e:
            print(e)

        return Response(response)


LoginView = LoginView.as_view()


class RegisterView(APIView):

    def post(self, request):
        response = {'status': 500, 'message': 'Something went wrong'}
        try:
            data = request.data
            print(response)
            print(data)
            print(response)
            if data.get('reg-username') is None:
                response['message'] = 'key username not found'
                raise Exception('key username not found')

            if data.get('reg-password') is None:
                response['message'] = 'key password not found'
                raise Exception('key password not found')
            check_user = User.objects.filter(
                username=data.get('reg-username')).first()
            if check_user:
                response['message'] = 'username already taken'
                raise Exception('username already taken')

            user_obj = User.objects.create(email=data.get('reg-email'),
                                           username=data.get('reg-username'))
            user_obj.set_password(data.get('reg-password'))
            user_obj.save()
            
            token = generate_random_string(20)

            response['message'] = 'User created '
            response['status'] = 200
        except Exception as e:
            print(e)

        return Response(response)


RegisterView = RegisterView.as_view()
