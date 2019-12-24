from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from product.models import Product
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q



# Create your views here.
def home(request):

   products = Product.objects.all()
   paginator = Paginator(products, 2)
   page = request.GET.get('page')
   try:
      contacts = paginator.page(page)

   except PageNotAnInteger:
      contacts = paginator.page(1)
   except EmptyPage:
      contacts = paginator.page(paginator.num_pages)

   print(contacts)

   # template = loader.get_template('index.html')
   # return HttpResponse(template.render({'products':products,"request":request,"contacts": contacts}))

   return render(request, 'index.html', {'products':products,'contacts': contacts})

def searchposts(request):
    if request.method == 'GET':
        query= request.GET.get('q')

        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups= Q(pname__icontains=query)

            results= Product.objects.filter(lookups).distinct()
            print(results)

            context={'products': results,
                     'submitbutton': submitbutton}

            return render(request, 'search_result.html', context)

        else:
            return render(request, 'search_result.html')

    else:
        return render(request, 'search_result.html')


