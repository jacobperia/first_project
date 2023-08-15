from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.shortcuts import get_object_or_404, render

from .models import UrlLink

# Create your views here.
class IndexView(generic.ListView):
    model = UrlLink
    template_name = 'urlShortener/index.html'
    context_object_name = 'short_url_list'

    def get_queryset(self):
        return UrlLink.objects.all()

def detail(request, url_link_id):
    url_link = get_object_or_404(UrlLink, pk=url_link_id)
    return render(request, 'urlShortener/detail.html', {'url_link': url_link})

def shorten(request):
    new_url = UrlLink(original_url = request.POST['original_url'])
    new_url.save()
    return HttpResponseRedirect(reverse('urlShortener:detail', args=(str(new_url.id),)))