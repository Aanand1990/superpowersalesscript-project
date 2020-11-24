from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required
from .models import Salesscript
from django.utils import timezone


def home(request):
    return render(request,'salesscripts/home.html')

@login_required
def dashboard(request):
    scriptlist = list(Salesscript.objects.filter(member=request.user))
    if not scriptlist:
        return render(request,'salesscripts/dashboard.html')
    else:
        return render(request,'salesscripts/dashboard.html', {'scriptlist':scriptlist})


@login_required
def create(request):
    if request.method == 'POST':
        salesscript = Salesscript()
        salesscript.scripttitle = request.POST.get("scripttitleone")
        salesscript.salutationone = request.POST.get('salutationone')
        salesscript.greetingsone = request.POST.get('greetingsone')
        salesscript.usernameone = request.POST.get('usernameone')
        salesscript.companynameone = request.POST.get('companynameone')
        salesscript.problemstatementone = request.POST.get('problemstatementone')
        salesscript.backstorytwo = request.POST.get('backstorytwo')
        salesscript.productnamethree = request.POST.get('productnamethree')
        salesscript.qualifierquestionsthree = request.POST.get('qualifierquestionsthree')
        salesscript.productpresentationfour = request.POST.get('productpresentationfour')
        salesscript.rapportquestionfive = request.POST.get('rapportquestionfive')
        salesscript.customerdoubtssix = request.POST.get('customerdoubtssix')
        salesscript.answertocustomersix = request.POST.get('answertocustomersix')
        salesscript.productnameseven = request.POST.get('productnameseven')
        salesscript.painpointseven = request.POST.get('painpointseven')
        salesscript.productidealstateeight = request.POST.get('productidealstateeight')
        salesscript.problemstatementnine = request.POST.get('problemstatementnine')
        salesscript.productdescriptionelevan = request.POST.get('productdescriptionelevan')
        salesscript.productnametwelve = request.POST.get('productnametwelve')
        salesscript.whatdoesitdotwelve = request.POST.get('whatdoesitdotwelve')
        salesscript.pricetwelve = request.POST.get('pricetwelve')
        salesscript.member = request.user
        salesscript.pub_date = timezone.datetime.now()
        salesscript.save()
        return redirect('/salesscripts/'+ str(salesscript.id))
    else:
        return render(request,'salesscripts/create.html')

@login_required
def script(request, salescript_id):
    script = get_object_or_404(Salesscript, pk=salescript_id)
    return render(request,'salesscripts/script.html', {'script':script})
