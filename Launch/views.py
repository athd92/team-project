from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class IndexView(TemplateView):
    template_name = 'Launch/index.html'


class LegalView(TemplateView):
    """
    This view displays legal content for this
     website.
    """
    template_name = 'Launch/legals.html'
