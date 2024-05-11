from django.shortcuts import render
from django.http import JsonResponse 
from django.contrib.auth.decorators import login_required
from agenda.models import Profissional, Client, Service, Events
from agenda.forms import EventForm
from django.shortcuts import get_object_or_404
from datetime import datetime, timedelta
from django.views.generic import ListView, UpdateView, CreateView, DetailView, DeleteView

# Create your views here.


 
# Create your views here.
@login_required(login_url='/login')
def index(request):  
    all_events = Events.objects.all().exclude(status='R')
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
        "status_choices": Events.status_choices,    
    }
    return render(request,'index.html',context)


@login_required(login_url='/login')
def load_funcoes_servicos_profissional(request):
    profissional_id = request.GET.get('profissional_id')
    profissional = Profissional.objects.get(id=profissional_id)
    servicos = profissional.services.all().order_by('description')
    event_id = request.GET.get('event')
    servico_do_evento = None  # Initialize servico_do_evento
    if event_id:
        event_id = Events.objects.get(id=event_id)
        servico_do_evento = event_id.service.id

    out = []
    for servico in servicos:
        out.append({
            'id': servico.id,
            'description': servico.description,
            'selected': servico.id == servico_do_evento,  # Set selected to True if servico is the same as servico_do_evento      
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
    all_events = Events.objects.all().exclude(status='C')                                                                               
    out = []                                                                                                             
    for event in all_events:
        #if event.status == 'F':
     #       color = 'gray'  # ou qualquer outra cor para status 'F'
        diference= event.end - event.start
        minutes = diference.total_seconds() / 60
        out.append({                                                                                                   
                                                                                        
            'id': event.id,
            'title': event.client.name,
            'start': event.start,                                                         
            'end': event.end,
            'resourceId': event.professional.id,
            'description': event.service.description,
            'client': event.client.name,
            'client_id': event.client.id,
            'professional_id': event.professional.id,
            'servico_id': event.service.id,
            'observation': event.observation,
            'time_min': event.service.time_min,  
            'minutes': minutes,      
            'status': event.status, 
           # 'color': color,                                                
        })                                                                                                        
                                                                                                                      
    return JsonResponse(out, safe=False) 
 
def all_resources(request):
    profissionais = Profissional.objects.all()
    out = []
    for profissional in profissionais:
        out.append({
            'id': profissional.id,
            'title': profissional.name,
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
    event_id = request.GET.get("id", None)
    event = get_object_or_404(Events, id=event_id)    
    start_str = request.GET.get("start", None)
    start = datetime.strptime(start_str, "%Y-%m-%dT%H:%M")   
    time_min_str = request.GET.get("timeMin", None)
    # Convert the string to an integer
    time_min = int(time_min_str) 
    end = start + timedelta(minutes=time_min)
    client_id = request.GET.get("client", None)
    client = Client.objects.get(id=client_id)
    professional_id = request.GET.get("profissional", None)
    profissional = Profissional.objects.get(id=professional_id)
    service_id = request.GET.get("servico", None)
    service = Service.objects.get(id=service_id)
    observation = request.GET.get("obs", None)  
    status = request.GET.get("status", None)

    event.start = start
    event.end = end
    event.client = client
    event.professional = profissional
    event.service = service
    event.observation = observation  
    event.status = status  
    event.save()
    data = {}
    return JsonResponse(data)

@login_required(login_url='/login')
def move(request):
    event_id = request.GET.get("id", None)
    event = get_object_or_404(Events, id=event_id)
    start_str = request.GET.get("start", None)
    start = datetime.strptime(start_str, "%Y-%m-%dT%H:%M")      
    end_str = request.GET.get("end", None)    
    end = datetime.strptime(end_str, "%Y-%m-%dT%H:%M")  
    
    print(start_str, end_str)
    print(start, end)

    event.start = start
    event.end = end
    event.save()
    data = {}
    return JsonResponse(data)

