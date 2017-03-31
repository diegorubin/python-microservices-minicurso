from tornado_json.requesthandlers import APIHandler

from frontend.services.comment import create

from microservicesutils.logger import application

class CommentsAPIController(APIHandler):

    def post(self):
        comment = {
            "comment": self.get_body_argument('comment'),
            "user": self.get_body_argument('user'),
            "resource_type": self.get_body_argument('resource_type'),
            "resource_uid": self.get_body_argument('resource_uid')
        }
        try:
            create(comment)
            self.success({'message': 'Comentário criado com sucesso!'})
        except Exception as e:
            application.error('error on create comment in api:' + str(e))
            self.set_status(422)
            self.fail({'message': 'Não foi possível criar o comentário'})

