# -*- coding: utf-8 -*-
import tornado.ioloop
import tornado.web
import math

from tornado_json.requesthandlers import APIHandler
from tornado_json import schema

PI = 3.14
# Dicas
# Para setar o status http use o método self.set_status(numero)
# Para retornar o json, use return {}
class GeometriaController(APIHandler):

    @schema.validate(
        input_schema={
            "type": "object",
            "properties": {
                "figura": {"type": "string"}
            }
        }
    )
    def post(self):
        request = self.body
        if not "figura" in request:
            self.set_status(422)
        else:
            if hasattr(self, request["figura"]):
                return getattr(self, request["figura"])(request)
            else:
                self.set_status(404)

    def circulo(self, request):
        if not "raio" in request:
            self.set_status(422)
        else:
            raio = request['raio']
            return {
                'diametro': raio * 2,
                'circunferencia': 2 * PI * raio,
                'area': PI * math.pow(raio,2)
            }

    def retangulo(self, request):
        if (not "altura" in request) and (not "largura" in request):
            self.set_status(422)
        else:
            altura = request['altura']
            largura = request['largura']
            return {
                'area': altura * largura,
                'quadrado': altura == largura
            }


def make_app():
    return tornado.web.Application([
        (r"/geometria", GeometriaController),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()

