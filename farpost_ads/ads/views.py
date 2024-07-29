from .models import Ad
from .serializers import AdSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from .serializers import RegisterSerializer


class AdDetailView(generics.RetrieveAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    lookup_field = 'ad_id'


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
