from django.shortcuts import render
import requests
from front.settings import BACK_HOST
# Create your views here.
def counter(request):
    count = requests.get(f'{BACK_HOST}/count').json()

    return render(request, 'index.html', {'count' : count})