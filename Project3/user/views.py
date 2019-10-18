from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.core import serializers
from rest_framework.views import APIView
from user.forms import FormRegister
from user.serializers import UserSerializer
from django.urls import reverse_lazy
import json

def userListed(request):
    list = serializers.serialize('json', User.objects.all(), fields=['username', 'first_name'])
    return HttpResponse(list, content_type='application/json')

class UserRegister(CreateView):
    model = User
    template_name = 'user/register.html'
    form_class = FormRegister
    success_url = reverse_lazy('pet:pet_list')
    #print(form_class.errors)
    
class UserAPI(APIView):
    serializer = UserSerializer

    def get(self, request, format=None):
        list = User.objects.all()
        response = self.serializer(list, many=True)
        return HttpResponse(json.dumps(response.data), content_type='application/json')