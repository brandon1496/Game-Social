from django.views.generic import TemplateView

class HomePage(TemplateView):
    template_name = 'index.html'

class TestPage(TemplateView):
    template_name = 'test.html'

class Peacepage(TemplateView):
    template_name = 'peace.html'