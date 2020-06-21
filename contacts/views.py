from django.shortcuts import render

# Create your views here.
from .models import Contact
from .serializers import ContactSerializer
from rest_framework import generics

class ContactListCreate(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer