# -*- coding: utf-8 -*-
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("""
            <html>
                <head>
                    <title>Funcionou!</title>
                    <style>
                        body {
                            text-align: center;
                        }
                    </style>
                </head>
                <body>
                    <h1> Funcionou! \o/</h1>
                    <img src="http://www.gifbin.com/bin/1237811519_chuck-norris-approves.gif"/>
                </body>
            </html>
        """)

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()

