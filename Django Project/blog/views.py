from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	context ={
		'judul':'blog',
		'kontributor':'icha',
		'nav':[
			['/','Home' ],
			['/blog/post','Post' ],
			['/blog/recent', 'Recent']
		]
	}

	return render(request, 'blog/index.html', context)


def recent(request):
	context ={
		'judul':'recent',
		'kontributor':'ezel',
		'nav':[
			['/','Home' ],
			['/blog/post','Post' ],
			['/blog/recent', 'Recent']
		]
	}
	return render(request, 'blog/index.html', context)

def post(request):
	context ={
		'judul':'post',
		'kontributor':'widya',
		'nav':[
			['/','Home' ],
			['/blog/post','Post' ],
			['/blog/recent', 'Recent']
		]
	}

	return render(request, 'blog/index.html', context)
	


