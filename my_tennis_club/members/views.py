from django.http import HttpResponse,JsonResponse
from django.template import loader
from .models import Member
from django.db.models import Q

def members(request):
    mymembers = Member.objects.all().values()

    template = loader.get_template('all_members.html')
    context = {
        "mymembers":mymembers
    }
    return HttpResponse(template.render(context,request))

def details(request,id):
    mymember  = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        "mymember":mymember
    }
    return HttpResponse (template.render(context,request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def testing(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('template.html')
    context = {
        'mymembers':mymembers,
        'firstname':"Gabrielzin"
    
    }

    return HttpResponse(template.render(context,request))

def testando(request):
    mydata = Member.objects.filter(firstname = "Gabriel").values() | Member.objects.filter(firstname = "Tobias").values()

    template = loader.get_template("template2.html")
    context = {
        "mymembers":mydata
    }

    return HttpResponse(template.render(context,request))
