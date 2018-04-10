from django.shortcuts import render
from django.http import HttpResponse
from .models import Urls_acortadas
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
formulario = """
		<form method="POST" >
 		 URL a acortar:<br>
	   <input type="text" name="url" value=""><br>
  	   <input type="submit" value="Enviar"><br><br>
	   </form> 
		"""
@csrf_exempt
def list(request):
	lista = Urls_acortadas.objects.all()		# devuelve una lista con todos los objetos de la base de datos
	if request.method == 'GET':
		salida = formulario
		salida += "<html><body><br><br><h1>Lista de URLs acortadas: </h1></body></html><ul>"
		for urls in lista:
			salida += '<li><a href="' + urls.url + '">' + urls.url + "</a> tiene el índice: " + str(urls.indice)
		salida += "</ul>"
	elif request.method == 'POST':
		page = request.POST['url']
		if page.startswith('http',0) or page.startswith('http',0):		#si no tiene http/https añadimos http por defecto
				pass
		else:
			page = "http://" + page
		for urls in lista:		#miramos si esta en la lista ya
			if page in urls.url:
				return HttpResponse ("Ya está en la lista.")
		nueva = Urls_acortadas(url = page, indice = len(lista))
		nueva.save()
		salida = "<html><body>""URL real: <a href=" + nueva.url + ">" + nueva.url + "</a><br><br>URL acortada: " + str(nueva.indice) + "</body></html>"
	return HttpResponse(salida)

def redirect(request, num):
	lista = Urls_acortadas.objects.all()
	try:
		page = lista[int(num)].url
		salida = "<html><head><meta http-equiv='Refresh' content=3;url=" + page +"></head><body><h1>""HTTP REDIRECT<br></h1>""Espere a ser redirigido""</body></html>"
	except Urls_acortadas.DoesNotExist:
			return HttpResponse("No existe")	
	return HttpResponse(salida)
