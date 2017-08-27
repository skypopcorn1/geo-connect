from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import LayerForm
from .models import CSVUpload, Map

def index(request):
    if request.user.is_authenticated():
        form = LayerForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return HttpResponseRedirect(instance.get_absolute_url())
        context = {
        "form": form,
        }
        return render(request, 'index2.html', context)
    else:
        return redirect('/login/')


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
