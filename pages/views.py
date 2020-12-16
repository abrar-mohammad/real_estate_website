from django.shortcuts import render, HttpResponse
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import state_choices, bedroom_choices, price_choices

# Create your views here.


def index(request):
    listings = Listing.objects.order_by(
        '-list_date').filter(is_published=True)[:3]
    context = {
        'listings': listings,
        'state_choices': state_choices,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
    }
    return render(request, "pages/index.html", context)


def about(request):
    realtor = Realtor.objects.order_by('-hire_time')

    # get mvp
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)
    context = {
        'realtors': realtor,
        'mvp_realtors': mvp_realtors
    }
    return render(request, "pages/about.html", context)
