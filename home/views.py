from django.shortcuts import render
from .models import HepepsTeam, BackgroundImages

from service.models import Service

# Create your views here.
def index(request):
    all_team = HepepsTeam.objects.all()
    bgimages = BackgroundImages.objects.all()
    service=Service.objects.all()
    content = {
        'all_team': all_team,
        'bgimages': bgimages,
        'service': service
    }

    return render(request, 'home/index.html', content)
