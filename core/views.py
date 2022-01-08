from django.http import HttpResponse
from django.template import Template
from django.template.context import Context
from datetime import datetime
from django.template import loader

def saludo(req):

    return HttpResponse('Hola a todos! Que rápido es codear en Django!')

def despedirse(req):

    return HttpResponse(
        """
        <h4>Adios, gracias por visitarnos!</h4>
        """
    )

def saluda_con_nombre(req, nombre):
    texto = f'Hola, mi nombre es:<br></br> {nombre}'

    return HttpResponse(texto)

def saluda_con_template(req):
    mi_dic = {
        "nombre": "Magali",
        "inicial": "B.",
        "ahora": datetime.now(),
        "notas": [5, 8, 10, 3]
    }

    # mi_html = open("C:/Users/magal/Desktop/Django/Proyecto1/core/Plantillas/template1.html")
    # mi_plantilla = Template(mi_html.read())
    # mi_html.close
    # mi_contexto = Context(mi_dic) #Le pone un diccionario.
    # documento = mi_plantilla.render(mi_contexto)
    mi_plantilla = loader.get_template('template1.html')
    documento = mi_plantilla.render(mi_dic)


    return HttpResponse(documento)