from django.shortcuts import render
from django.http import HttpResponse #new

def index(request): #new
    return render(request,'principal/index.html')

def update_equipa(request, equipa_id):
    equipa_id = int(equipa_id)
    try:
        equipa_sel = Equipa.objects.get(id=equipa_id)
    except Equipa.DoesNotExist:
        return redirect('equipas')
    if request.method == 'POST':
        upEquipaForm = crudEquipaForm(request.POST, instance=equipa_sel)
        if upEquipaForm.is_valid():
            upEquipaForm.save()
            return redirect('equipas')

    else:
        upEquipaForm = crudEquipaForm(instance=equipa_sel)
    return render(request, 'pgfut_djapp/crudEquipa.html', {'Form': upEquipaForm})

