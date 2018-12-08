from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.conf import settings
from django.urls import reverse
from django.views import View
from django.views.generic import DetailView

from . import models, forms, utils

class Index(View):
    model = User
    template_name = 'memories/index.html'

    def get(self, request):
        users = self.model.objects.all()
        return render(request, self.template_name, {'users': users})


class MemoryListView(View):
    model = models.Memory
    template_name = 'memories/memory_list.html'

    def get(self, request, username=None):
        user = get_object_or_404(User, username=username)
        memories = self.model.objects.filter(author__username=username)
        return render(request, self.template_name, {'memories': memories, 'page_username': username})


class MemoryCreateView(View):
    form_class = forms.MemoryForm
    template_name = "memories/memory_create.html"

    def get(self, request, username, *args, **kwargs):
        if request.user.username != username:
            raise Http404
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, username):
        if request.user.username != username:
            raise Http404
        file = request.FILES
        form = self.form_class(request.POST, file)
        if form.is_valid():
            memory = form.save(commit=False)
            memory.author = request.user
            mime = utils.check_in_memory_mime(file['media'])
            memory.mime_type = mime
            memory.save()
            return redirect(reverse('memories:detail', kwargs={'username': request.user.username, 'pk': memory.pk}))
        return render(request, self.template_name, {'form': form})

class MemoryEmbedView(View):
    form_class = forms.EmbedForm
    template_name = "memories/embed_form.html"

    def get(self, request, username):
	    if request.user.username != username:
	        raise Http404
	    form = self.form_class()
	    return render(request, self.template_name, {'form': form})
    
    def post(self, request, username):
        if request.user.username != username:
            raise Http404
        form = self.form_class(request.POST)
        if form.is_valid():
            embed_id = form.cleaned_data.get('embed_id')
            memory = form.save(embed_id, request.user)
            return redirect(reverse('memories:detail', kwargs={"username": username, 'pk': memory.id }))
        return render(request, self.template_name, {'form': form})


class MemoryDetailView(DetailView):
    model = models.Memory
    context_object_name = 'memory'