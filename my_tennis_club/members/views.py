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
    mydata = Member.objects.filter(Q(firstname='Emil') | Q(firstname='Tobias')).values()
    comeca_com_l = Member.objects.filter(firstname__startswith="L").values()
    termina_com_l = Member.objects.filter(firstname__endswith="L").values()
    ordenando_consultas = Member.objects.all().order_by("firstname").values()
    ordenando_consultas_reverso = Member.objects.all().order_by("-firstname").values()
    template = loader.get_template('template2.html')
    context = {
        'mymembers': mydata,
        "comeca_com_l":comeca_com_l,
        "termina_com_l":termina_com_l,
        "ordenando_consultas":ordenando_consultas,
        "ordenando_consultas_reverso":ordenando_consultas_reverso,
    }
    return HttpResponse(template.render(context, request))
