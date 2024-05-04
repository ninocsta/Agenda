from django.shortcuts import render
from django.http import JsonResponse 
from agenda.models import Events 
from django.contrib.auth.decorators import login_required
from agenda.models import Profissional, Client, Service
from agenda.forms import EventForm

from datetime import datetime, timedelta

# Create your views here.


 
# Create your views here.
@login_required(login_url='/login')
def index(request):  
    all_events = Events.objects.all()
    profissionais = Profissional.objects.all()
    servicos = []
    clientes = Client.objects.all()
    form = EventForm()
    context = {
        "events":all_events,
        "profissionais":profissionais,
        "servicos":servicos, 
        "clientes":clientes,   
        "form":form,    
    }
    return render(request,'index.html',context)


@login_required(login_url='/login')
def load_funcoes_servicos_profissional(request):
    profissional_id = request.GET.get('profissional_id')
    profissional = Profissional.objects.get(id=profissional_id)
    servicos = profissional.services.all().order_by('description')

    out = []
    for servico in servicos:
        out.append({
            'id': servico.id,
            'description': servico.description,
            'time_min': servico.time_min,
            # Add other fields as needed
        })

    return JsonResponse(out, safe=False)


@login_required(login_url='/login')
def load_funcoes_dados_servicos(request):
    servico_id = request.GET.get('servico_id')
    servico = Service.objects.get(id=servico_id)

    out = {
        'id': servico.id,
        'description': servico.description,
        'time_min': servico.time_min,
        # Add other fields as needed
    }
    return JsonResponse(out, safe=False)


@login_required(login_url='/login')
def all_events(request):                                                                                                 
    all_events = Events.objects.all()                                                                                    
    out = []                                                                                                             
    for event in all_events:                                                                                             
        out.append({                                                                                                   
                                                                                        
            'id': event.id,
            'title': event.client.name,
            'start': event.start,                                                         
            'end': event.end,
            'client': event.client.name,                                                   
        })                                                                                                               
                                                                                                                      
    return JsonResponse(out, safe=False) 
 

@login_required(login_url='/login')
def add_event(request):
    service_id = request.GET.get("servico", None)
    service = Service.objects.get(id=service_id)
    start_str = request.GET.get("start", None)
    start = datetime.strptime(start_str, "%Y-%m-%dT%H:%M")   
    time_min_str = request.GET.get("timeMin", None)
    # Convert the string to an integer
    time_min = int(time_min_str) 
    end = start + timedelta(minutes=time_min)
    client_id = request.GET.get("client", None)
    # Obtenha a instância do cliente correspondente ao ID fornecido
    client = Client.objects.get(id=client_id)
    professional_id = request.GET.get("profissional", None)
    # Obtenha a instância do profissional correspondente ao ID fornecido
    professional = Profissional.objects.get(id=professional_id)
    observation = request.GET.get("obs", None)
    event = Events(start=start, end=end, client=client, professional=professional, service=service, observation=observation)    
    event.save()
    data = {}
    return JsonResponse(data)


@login_required(login_url='/login')
def update(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    id = request.GET.get("id", None)
    event = Events.objects.get(id=id)
    event.start = start
    event.end = end
    event.name = title
    event.save()
    data = {}
    return JsonResponse(data)


@login_required(login_url='/login')
def remove(request):
    id = request.GET.get("id", None)
    event = Events.objects.get(id=id)
    event.delete()
    data = {}
    return JsonResponse(data)


