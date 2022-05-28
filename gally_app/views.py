from django.http import Http404, HttpResponse
from django.shortcuts import render,redirect
from .models import Category, Image,Location
# Create your views here.

def index(request):
  photos = Image.objects.all()
  locations = Location.objects.all()
  heading = "All Locations"
  return render(request,"gally_app/index.html",{'photos':photos, 'locations':locations,'heading':heading})

def location(request,place):
  try:
    placeId = Location.objects.get(name=place)
  except Location.DoesNotExist:
    raise Http404
  photos = Image.filter_by_location(placeId)
  heading = placeId
  locations = Location.objects.all()
  return render(request,"gally_app/index.html",{'photos':photos, 'heading':heading, 'locations':locations})

def category(request):
  locations = Location.objects.all()
  
  if 'category' in request.GET and request.GET['category']:
    cat_to_search = request.GET.get('category')
    cat_to_search = cat_to_search.lower()
    try:
      cat_Id = Category.objects.get(name=cat_to_search)
    except Category.DoesNotExist:
      heading = f"Seems category {cat_to_search} does not exist"
      return render(request,"gally_app/results.html",{ 'heading':heading, 'locations':locations})
    photos = Image.objects.filter(category = cat_Id)
    heading = f"Search results for {cat_to_search}"
    return render(request,"gally_app/results.html",{'photos':photos, 'heading':heading, 'locations':locations})
  return render(request,"gally_app/results.html",{'photos':photos, 'heading':heading, 'locations':locations})



def notFound(request,exception):

  return render(request,"gally_app/404.html")