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
        pass


def make_app():
    return tornado.web.Application([
        (r"/geometria", GeometriaController),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()

