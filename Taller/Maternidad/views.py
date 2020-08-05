from django.shortcuts import render
from Maternidad.models import paciente, hoja_indicaciones, cirugias, medicamentos
import json
from datetime import  timedelta, datetime, date

# Create your views here.

def main(request):
    return render(request,'main.html')

def cirugia(request):
    cir_pacientes=hoja_indicaciones.objects.values_list('Nombre_cirugias',flat=True)
    cir_pacientes=[i for i in cir_pacientes]
    vale=cirugias.objects.values_list('nombre_cirugia',flat=True)
    vale=[i for i in vale]
    contador=[cir_pacientes.count(i) for i in range(1,len(vale)+1)]
    lista=[[vale[j],contador[j]] for j in range(len(vale))]
    hola=[["Cirugias","Cantidad"]]
    lista=hola+lista
    modified_data=json.dumps(lista)

    return render(request,'graph_cirugia.html',{    
        'values':modified_data,
    })

def medicamento(request):
    todos_medicamentos=medicamentos.objects.values_list('nombre',flat=True)
    usados_medicamentos=hoja_indicaciones.objects.values_list('nombre_medicamento',flat=True)
    todos_medicamentos=[i for i in todos_medicamentos]
    usados_medicamentos=[i for i in usados_medicamentos]
    contador=[usados_medicamentos.count(i) for i in range(1,len(todos_medicamentos)+1)]
    lista=[[todos_medicamentos[j],contador[j]] for j in range(len(todos_medicamentos))]
    hola=[["Medicamentos","Cantidad"]]
    lista=hola+lista
    modified_data=json.dumps(lista)


    return render(request,'graph_med.html',{
        'values':modified_data,
    })

def embarazos(request):
    si_no=["Embarazada","No embarazada"]
    embarazo_paciente=paciente.objects.values_list('embarazada',flat=True)
    embarazo_paciente=[i for i in embarazo_paciente]
    for i in range(len(embarazo_paciente)):
        if embarazo_paciente[i]==True:
            embarazo_paciente[i]="Embarazada"
        else:
            embarazo_paciente[i]="No embarazada"
    contador=[embarazo_paciente.count(i) for i in si_no]
    lista=[[si_no[j],contador[j]] for j in range(len(si_no))]


    hola=[["Embarazadas","No embarazadas"]]
    lista=hola+lista
    modified_data=json.dumps(lista)


    return render(request, 'graph_emb.html',{
        'values':modified_data,
    
    
    })

def camas(request):
    camas_iniciales=45
    fechas_pacientes=paciente.objects.values_list('fecha_hospitalizacion',flat=True)
    fechas_pacientes=[i for i in fechas_pacientes]
    #Cantidad de nuevos pacientes por día
    fec_pacientes = []
    for i in fechas_pacientes:
       if i not in fec_pacientes:
          fec_pacientes.append(i)
    contador1=[-fechas_pacientes.count(i) for i in fec_pacientes]
    cont1=[fechas_pacientes.count(i) for i in fec_pacientes]
    #lista=[[fec_pacientes[j],contador[j]]for j in range(len(fec_pacientes))]

    #Cantidad de pacientes dados de alta
    fecha_hoja=hoja_indicaciones.objects.values_list('fecha',flat=True)
    fecha_hoja=[i for i in fecha_hoja]
    altas=hoja_indicaciones.objects.values_list('alta',flat=True)
    altas=[i for i in altas]
    fecha_alta=[]
    for i in range(len(altas)):
        if altas[i]==True:
            fecha_alta+=[fecha_hoja[i]]

    fec_hoja=[]
    for i in fecha_alta:
       if i not in fec_hoja:
          fec_hoja.append(i)
    contador2=[fecha_alta.count(i) for i in fec_hoja]
    #lista2=[[fec_hoja[j],contador2[j]]for j in range(len(fec_hoja))]
    contador=contador1+contador2
    fecha=fec_pacientes+fec_hoja
    fecha_no_dup=[]
    for i in fecha:
        if i not in fecha_no_dup:
            fecha_no_dup.append(i)
    aux=0
    val=[]
    for i in fecha_no_dup:
        for j in range(len(fecha)):
            if i==fecha[j]:
                aux+=contador[j]
        val+=[aux]
        aux=0
    cant_camas=[camas_iniciales]+val
    for i in range(1,len(cant_camas)):
        cant_camas[i]=cant_camas[i-1]+cant_camas[i]

    #for i in range(len(fecha_no_dup)):
    #    fecha_no_dup[i]=int(fecha_no_dup[i].day)
    fecha_no_dup=fecha_no_dup

    #a=[["Fecha", "Camas"]]
    #lista=[[fecha_no_dup[j],cant_camas[j]]for j in range(len(cant_camas))]
    #lista=a+lista
    #modified_data=json.dumps(lista)
    
    
    inicio = date(2020,8,1)
    fin    = date(2020,8,31)

    lista_fechas = [inicio + timedelta(days=d) for d in range((fin - inicio).days + 1)] 
    cont1=[fechas_pacientes.count(i) for i in fec_pacientes]
    cont2=contador2
    z=lista_fechas
    m=fec_pacientes
    a=[0]*len(z) #Lista completa de las pacientes que entran por día
    
    for i in range(len(m)):
        for j in range(len(z)):
            if m[i]==z[j]:
                a[j]=cont1[i]
        
    n=fec_hoja
    b=[0]*len(z)
    for i in range(len(n)):
        for j in range(len(z)):
            if n[i]==z[j]:
                b[j]=cont2[i]

    contador_r=[0]*len(z)    
    for i in range(len(z)):
        contador_r[i]=-a[i]+b[i]

    contador_r[0]=10
    for i in range(1,len(contador_r)):
        contador_r[i]=contador_r[i-1]+contador_r[i] #La cantidad de camas que hay disponibles

    camas_inicial=[10]*len(z)
    info=[["Fecha", "Hospitalizaciones", "Altas", "Camas disponibles"]]
    datos=[0]*len(z)
    feca=[i.strftime('%d-%m-%Y') for i in z]
    for i in range(len(z)):
        datos[i]=[feca[i],a[i],b[i],contador_r[i]]

    datos_todo=info+datos
    modified_data=json.dumps(datos_todo)

    return render(request,'graph_camas.html',{
        'values':modified_data,
 
    })