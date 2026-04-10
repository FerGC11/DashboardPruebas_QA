from django.shortcuts import render
from .models import Pruebas, EstatusPruebas, TiposPruebas

# Create your views here.

def mostrar_dashboard(request):
    
    try:
        #Consulta para cargar datos en tarjeta de total pruebas
        pruebas_totales = {
            'total': Pruebas.objects.count(),
            'totalMaquinas': Pruebas.objects.filter(IdTipoPrueba=1).count(),
            'totalAplicaciones': Pruebas.objects.filter(IdTipoPrueba=2).count(),
            'totalWeb': Pruebas.objects.filter(IdTipoPrueba=3).count()
        }
        
        #Consulta para cargar datos en tarjeta de total pruebas pendientes
        pruebas_pendientes = {
            'pendientes': Pruebas.objects.filter(IdEstatusPrueba=1).count(),
            'pendientesMaquinas': Pruebas.objects.filter(IdEstatusPrueba=1, IdTipoPrueba=1).count(),
            'pendientesAplicaciones': Pruebas.objects.filter(IdEstatusPrueba=1, IdTipoPrueba=2).count(),
            'pendientesWeb': Pruebas.objects.filter(IdEstatusPrueba=1, IdTipoPrueba=3).count()
        }
        
        #Consulta para cargar datos en tarjeta de total pruebas en proceso
        pruebas_enProceso = {
            'enProceso': Pruebas.objects.filter(IdEstatusPrueba=2).count(),
            'enProcesoMaquinas': Pruebas.objects.filter(IdEstatusPrueba=2, IdTipoPrueba=1).count(),
            'enProcesoAplicaciones': Pruebas.objects.filter(IdEstatusPrueba=2, IdTipoPrueba=2).count(),
            'enProcesoWeb': Pruebas.objects.filter(IdEstatusPrueba=2, IdTipoPrueba=3).count()
        }
        
        #Consulta para cargar datos en tarjeta de total pruebas bloqueadas
        pruebas_bloqueadas = {
            'bloqueadas': Pruebas.objects.filter(IdEstatusPrueba=3).count(),
            'bloqueadasMaquinas': Pruebas.objects.filter(IdEstatusPrueba=3, IdTipoPrueba=1).count(),
            'bloqueadasAplicaciones': Pruebas.objects.filter(IdEstatusPrueba=3, IdTipoPrueba=2).count(),
            'bloqueadasWeb': Pruebas.objects.filter(IdEstatusPrueba=3, IdTipoPrueba=3).count()
        }
        
        #Consulta para cargar datos en tarjeta de total pruebas liberadas
        pruebas_liberadas = {
            'liberadas': Pruebas.objects.filter(IdEstatusPrueba=4).count(),
            'liberadasMaquinas': Pruebas.objects.filter(IdEstatusPrueba=4, IdTipoPrueba=1).count(),
            'liberadasAplicaciones': Pruebas.objects.filter(IdEstatusPrueba=4, IdTipoPrueba=2).count(),
            'liberadasWeb': Pruebas.objects.filter(IdEstatusPrueba=4, IdTipoPrueba=3).count()
        }
        
        #Consulta para cargar datos en tarjeta de total pruebas rechazadas
        pruebas_rechazadas = {
            'rechazadas': Pruebas.objects.filter(IdEstatusPrueba=5).count(),
            'rechazadasMaquinas': Pruebas.objects.filter(IdEstatusPrueba=5, IdTipoPrueba=1).count(),
            'rechazadasAplicaciones': Pruebas.objects.filter(IdEstatusPrueba=5, IdTipoPrueba=2).count(),
            'rechazadasWeb': Pruebas.objects.filter(IdEstatusPrueba=5, IdTipoPrueba=3).count()
        }
        
        #Consulta para la llenar la tabla de detalle pruebas
        detalle_pruebas = Pruebas.objects.select_related('IdTester', 'IdEstatusPrueba', 'IdTipoPrueba').all().order_by('-FechaAlta')
        
        context = {
            'detalle_pruebas': detalle_pruebas,
            'pruebas_totales': pruebas_totales,
            'pruebas_pendientes': pruebas_pendientes,
            'pruebas_enProceso': pruebas_enProceso,
            'pruebas_bloqueadas': pruebas_bloqueadas,
            'pruebas_liberadas': pruebas_liberadas,
            'pruebas_rechazadas': pruebas_rechazadas,
        }
        return render(request, 'index.html', context)
    
    except Exception as e:
        print("Error en la funcion mostrar_dashboard")
