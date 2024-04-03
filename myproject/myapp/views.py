from django.shortcuts import render

# Create your views here.
def star(request):
    return render(request, 'star.html')
def main(request):
    return render(request, 'snow.html')
def home(request):
    return render(request, 'home.html')
def firefly(request):

    return render(request=request,
        template_name='firefly.html'
    )