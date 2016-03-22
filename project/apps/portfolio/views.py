from __future__ import unicode_literals

from django.http import Http404

from django.shortcuts import render
from portfolio.models import PortfolioItem

def index(request):
	items = PortfolioItem.objects.all()
#	raise ValueError('TEST')
	return render(request, 'portfolio/index.html', {'object_list': items})


def single(request, pk):
	try:
		obj = PortfolioItem.objects.get(pk=pk)
	except PortfolioItem.DoesNotExist:
		raise Http404

	return render(request, 'portfolio/single.html', {'object': obj})