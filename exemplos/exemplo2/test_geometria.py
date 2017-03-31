import json

from tornado.escape import json_encode
from tornado.testing import AsyncHTTPTestCase

from geometria import make_app, GeometriaController

class GeometriaController(AsyncHTTPTestCase):

    def get_app(self):
        return make_app()

    def test_sem_figura(self):
        body = json_encode({})
        response = self.fetch('/geometria', method='POST', body=body)
        self.assertEqual(response.code, 422)

    def test_circulo_sem_informacoes(self):
        body = json_encode({'figura': 'circulo'})
        response = self.fetch('/geometria', method='POST', body=body)
        self.assertEqual(response.code, 422)

    def test_circulo_com_informacoes(self):
        body = json_encode({'figura': 'circulo', 'raio': 3})
        response = self.fetch('/geometria', method='POST', body=body)
        data = json.loads(response.body.decode())["data"]
        self.assertEqual(response.code, 200)
        self.assertEqual(data['diametro'], 6)
        self.assertEqual(data['circunferencia'], 18.84)
        self.assertEqual(data['area'], 28.26)

    def test_circulo_raio_4(self):
        body = json_encode({'figura': 'circulo', 'raio': 4})
        response = self.fetch('/geometria', method='POST', body=body)
        data = json.loads(response.body.decode())["data"]
        self.assertEqual(response.code, 200)
        self.assertEqual(data['diametro'], 8)
        self.assertEqual(data['circunferencia'], 25.12)
        self.assertEqual(data['area'], 50.24)

    def test_retangulo_sem_informacoes(self):
        body = json_encode({'figura': 'retangulo'})
        response = self.fetch('/geometria', method='POST', body=body)
        self.assertEqual(response.code, 422)

    def test_retangulo(self):
        body = json_encode({'figura': 'retangulo', 'largura': 3, 'altura': 4})
        response = self.fetch('/geometria', method='POST', body=body)
        data = json.loads(response.body.decode())["data"]
        self.assertEqual(response.code, 200)
        self.assertEqual(data['area'], 12)
        self.assertFalse(data['quadrado'])

    def test_quadrado(self):
        body = json_encode({'figura': 'retangulo', 'largura': 3, 'altura': 3})
        response = self.fetch('/geometria', method='POST', body=body)
        data = json.loads(response.body.decode())["data"]
        self.assertEqual(response.code, 200)
        self.assertEqual(data['area'], 9)
        self.assertTrue(data['quadrado'])

    def test_figura_nao_existe(self):
        body = json_encode({'figura': 'outra'})
        response = self.fetch('/geometria', method='POST', body=body)
        self.assertEqual(response.code, 404)
