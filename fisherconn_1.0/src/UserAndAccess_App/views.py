from django.shortcuts import render, HttpResponse
from django.contrib.auth import (authenticate, get_user_model, login, logout)
# Create your views here.

from .forms import UserLoginFrom
from .models import User,Product

def login_view(request):
    if request.method == "POST":
        title = "form"
    # form = "(request.POST or None)
    # if form.is_valid():
    #     username = form.cleaned_data.get("username")
    #     password = form.cleaned_data.get("password")
    #     print ("username :" +username + " password :" + password)
    print "**** "
    print request
    print " ******"
    return render(request, "form.html", {  "title":title})


from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import UserSerializer, ProductSerializer




class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer



class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer