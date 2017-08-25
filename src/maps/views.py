from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')
    # return HttpResponse("Hello, world. You're at the polls index.")

# def trips_list(request):
# 	# trips = Trip.objects.all()
# 	# query = request.GET.get("destination")
# 	# if query:
# 	# 	trips = trips.filter(
# 	# 		Q(origin__icontains=query) |
# 	# 		Q(destination__icontains=query)
# 	# 	).distinct()
# 	return render(request, 'index.html', {"trips": trips})
