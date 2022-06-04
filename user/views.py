# from django.contrib.auth.models import User
# from django.shortcuts import render
# from django.contrib.auth import authenticate, login,logout
# from django.views import generic, View
#
#
# # Create your views here.
#
#
# class UserLogin(User):
#     template_name = 'user/login.html'
#
#     def get(self, request):
#         return render(request, 'user/login.html')
#
#     def post(self, request):
#         username = request.POST['username']
#         password = request.GET['password']
#         user = authenticate(request, username=username, password=password)
#
#         if user is not None:
#             login(request, user)
#         else:
#             return render(request, 'user/login.html')
#
#
# class UserLogout(generic.TemplateView):
#     template_name = 'user/login.html'
#
#     @staticmethod
#     def logout_view(request):
#         logout(request)
#
