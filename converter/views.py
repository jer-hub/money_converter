from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'converter/home.html')

def result(request):

    peso = float(request.GET.get('peso',1))

    sr = peso * 0.077
    jy = peso * 2.19
    usd = peso * 0.041
    cd = peso * 0.026
    uae = peso * 0.075

    return render (request, 'converter/result.html', {
        'sr' : sr,
        'jy' : jy,
        'usd' : usd,
        'cd' : cd,
        'uae' : uae
    })

