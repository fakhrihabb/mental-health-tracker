from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306223206',
        'name': 'Fakhri Habibi',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)

# Create your views here.
