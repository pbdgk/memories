from django.shortcuts import render
from django.contrib.auth.models import User
from django.conf import settings
from django.views import View

class Index(View):
    model = User
    template_name = 'memories/index.html'

    def get(self, request):
        users = self.model.objects.all()
        return render(request, self.template_name, {'users': users})
