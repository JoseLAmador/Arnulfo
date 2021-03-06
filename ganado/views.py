from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import EditAnimalSerializer, AnimalSerializer, CorralSerializer, LoteSerializer, AlimentoSerializer, BasicAnimalSerializer, BasicLoteSerializer, PesoSerializer, BasicPesoSerializer, RazaSerializer, FacturaSerializer
from .models import Animal, Lote, GastoAnimal, Corral, Peso, Raza, Factura
from .pagination import AnimalPagination, LotePagination, FacturaPagination
from django.db.models import Q, Avg, Count, Min, Sum

from datetime import datetime, timedelta


class FacturaViewSet(viewsets.ModelViewSet):
	queryset = Factura.objects.all()
	serializer_class = FacturaSerializer
	pagination_class = FacturaPagination

	def get_queryset(self, *args, **kwargs):
		query = self.request.GET.get("q")
		query_list = super(FacturaViewSet, self).get_queryset()
		if query:
			query_list = query_list.filter(
				Q(factura__icontains=query)
			).distinct()
		return query_list


#VIews for the API

# class AnimalAPI(APIView):

# 	def post(self, request):
# 		data = request.data
# 		print(data)
# 		animal = BasicAnimalSerializer(data=request.data)
# 		animal.is_valid()
# 		animal.save()
# 		instance = Animal.objects.get(id=animal.data['id'])
# 		serializer2 = AnimalSerializer(instance)
# 		serializer2.is_valid()
# 		return Response(serializer2.data)


class AnimalViewSet(viewsets.ModelViewSet):
	#queryset = Animal.objects.all().filter(status=True)
	queryset = Animal.objects.all()
	serializer_class = AnimalSerializer
	pagination_class = AnimalPagination

	def get_serializer_class(self):
	 	if self.action == 'update':
	 		return EditAnimalSerializer
	 	if self.action == 'partial_update':
	 		return EditAnimalSerializer
	 	return AnimalSerializer 

	def get_queryset(self, *args, **kwargs):
		query = self.request.GET.get("q")
		lote_query = self.request.GET.get("lote")
		queryset_list = super(AnimalViewSet,self).get_queryset()
		if query:
			queryset_list = queryset_list.filter(
				Q(arete_rancho__icontains=query)|
				Q(arete_siniga__icontains=query)|
				Q(owner__icontains=query)
				).distinct()
		if lote_query:
			queryset_list = queryset_list.filter(Q(lote__name__iexact=lote_query))
		return queryset_list

class LoteViewSet(viewsets.ModelViewSet):
	queryset = Lote.objects.all()
	serializer_class = LoteSerializer
	#pagination_class = LotePagination

	def get_serializer_class(self):
		if self.action == 'list':
			return LoteSerializer
		if self.action == 'retrieve':
			return LoteSerializer
		return BasicLoteSerializer

	def get_queryset(self, *args, **kwargs):
		query = self.request.GET.get("q")
		
		queryset_list = super(LoteViewSet,self).get_queryset()
		if query:
			queryset_list = queryset_list.filter(
				Q(name__icontains=query)
				).distinct()
	
		return queryset_list

class CorralViewSet(viewsets.ModelViewSet):
	queryset = Corral.objects.all()
	serializer_class = CorralSerializer

class AlimentoViewSet(viewsets.ModelViewSet):
	queryset = GastoAnimal.objects.all()
	serializer_class = AlimentoSerializer

class PesoViewSet(viewsets.ModelViewSet):
	queryset = Peso.objects.all()
	#serializer_class = PesoSerializer

	def get_serializer_class(self):
		if self.action == 'list':
			return PesoSerializer
		if self.action == 'retrieve':
			return PesoSerializer
		return BasicPesoSerializer 





class RazasViewSet(viewsets.ModelViewSet):
	queryset = Raza.objects.all()
	serializer_class = RazaSerializer


class ResumenView(APIView):
	def get(self, request):

		#Básicos
		aretes = Animal.objects.all().filter(status=True).annotate(aliments_total_kg=Sum('aliments__cantidad'))
		aretes_activos = aretes.aggregate(valor_inicial=Sum('costo_inicial'), count=Count('id'), gastos_cash=Sum('aliments__costo'))
		aretes_inactivos = len(Animal.objects.all().filter(status=False))
		proximos = Animal.objects.all().filter(pesadas__peso__gte=350, status=True).distinct()
		cuenta_proximos = len(proximos)

		proximos = AnimalSerializer(proximos, many=True)		
		gastos = GastoAnimal.objects.all().filter(animal__status=True ).aggregate(suma_gastos=Sum('costo'))
		gastos_alimento = GastoAnimal.objects.all().filter(animal__status=True, tipo='Alimento').aggregate(costo_alimento=Sum('costo'), kg_alimento=Sum('cantidad'))
		gastos_vacuna = GastoAnimal.objects.all().filter(animal__status=True, tipo='Vacuna').aggregate(suma_gastos_vacuna=Sum('costo'))					

		#gdp y esas formulas locas
		conversionPromedio = 0
		gdpPromedio = 0
		# (ultima_pesada - peso_inicial)/(fecha_ultima_pesada - fecha_inicial) y luego promediar el de todos los aretes activos
		for a in aretes:
			if a.last_pesada() != None:	
				print(a.aliments_total_kg)			
				diff_days=(a.last_pesada().created-a.fecha_entrada.date()).days
				if diff_days!= 0:
					gdp = (a.last_pesada().peso-a.peso_entrada)/diff_days				
				gdpPromedio += gdp
		gdpPromedio = gdpPromedio/len(aretes)


		
		data = {
			"aretes_activos":aretes_activos,
			"aretes_inactivos":aretes_inactivos,
			"cuenta_proximos":cuenta_proximos,
			"gdpPromedio":gdpPromedio,
			"conversionPromedio":conversionPromedio,
			"gastos":gastos,
			"gastos_alimento":gastos_alimento,
			"gastos_vacuna":gastos_vacuna,	
			"proximos":proximos.data,
			
				
		}
		return Response(data)




