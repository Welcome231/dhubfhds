from django.shortcuts import render
from . import models

def homePage(request):
    if request.method == "POST":
        searchInput = request.POST.get("if")

        print(searchInput)
        
        
        sResults = list( models.nameee.objects.filter(title=searchInput).values().values_list('content'))
        updRes = str(sResults)


        sResults2 = list( models.nameee.objects.filter(title=searchInput).values().values_list('title'))
        updRes2 = str(sResults2)

        

        #       !GIGA PROBLEM!
        #   jakies nawisy zostają nawet po usunięciu
        #   indeksu z listy (po prostu usuwa część artykułu)
        #   kod: (niedziała)

        # #updRes2 = [*updRes]
        # updRes2 = list(updRes)
        # print(updRes2)

        # updRes2.pop(0)
        # updRes2.pop(1)
        # del updRes2[-1]
        # del updRes2[-2]
        
        # updRes4 = ''.join(updRes2)
        # #updRes5 = updRes4.join(' ')
        # #mydata = models.nameee.objects.values_list('content', )
        # #print(sResults) 


        context = {
            'myvar': updRes,
            'title': updRes2,
            
        }
        return render(request, 'index3.html', context)
    return render(request, 'index.html')


def createArt(request):
    if request.method == "POST":
        artTitle = request.POST.get("tbar")
        
        artContent = request.POST.get("conbar")

        models.nameee.objects.create(
            title = artTitle,
            
            content = artContent
        )

    return render(request, "index2.html")