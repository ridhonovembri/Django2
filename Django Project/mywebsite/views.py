from django.http import HttpResponse
from django.shortcuts import render

def index(request):
	context = {
		'judul':'kelas terbuka',
		'kontributor':'ridho novembri',
	}

	return render(request, 'index.html', context)

