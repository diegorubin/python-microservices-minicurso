import tornado
import tornado.web
import os

from microservicesutils import logger
from microservicesutils.logger import general
from microservicesutils.settings import BOOKS_SERVER_PORT, DEBUG
from tornado_json.requesthandlers import APIHandler

BOOKS = [
    {
        'name': 'Código Limpo',
        'author': 'Robert C. Martin',
        'isbn': '8576082675',
        'cover': 'https://cache.skoob.com.br/local/images//-t2fmu20BoEUoLqW_vMS_0Ry3Xw=/200x/center/top/smart/filters:format(jpeg)/https://skoob.s3.amazonaws.com/livros/77509/CODIGO_LIMPO_1262882912B.jpg',
        'description': """
            Mesmo um código ruim pode funcionar, mas se ele não for limpo pode acabar com uma empresa de desenvolvimento. Perdem-se a cada ano horas incontáveis e recursos importantes devido a um código mal escrito. Mas não precisa ser assim.
            O renomado especialista em software Robert C. Martin apresenta um paradigma revolucionário com Código Limpo: habilidades práticas do Agile Software. Martin reuniu-se com seus colegas do Mentor Object para destilar suas melhores e mais ágeis práticas de limpar códigos “dinamicamente” em um livro que introduzirá gradualmente dentro de você os valores da habilidade de um profissional de softwares e lhe tornar um programador melhor.
            Que tipo de trabalho você fará? Você lerá códigos aqui, muitos códigos. E você deverá descobrir o que está correto e errado nos códigos. E o mais importante: você terá de reavaliar seus valores profissionais e seu comprometimento com o seu ofício.
            Código limpo está divido em três partes. Na primeira, há diversos capítulos que descrevem os princípios, padrões e práticas para criar um código limpo. A segunda parte consiste em diversos casos de estudo de complexidade cada vez maior. Cada um é um exercício para limpar um código – transformar o código base que possui alguns problemas em um melhor e eficiente. A terceira parte é a compensação: um único capítulo com uma lista de heurísticas e “odores” reunidos durante a criação dos estudos de caso. O resultado será um conhecimento base que descreve a forma como pensamos quando criamos, lemos e limpamos um código.
            Após ler este livro os leitores saberão:

            - Como distinguir um código bom de um ruim

            - Como escrever códigos bons e como transformar um ruim em um bom

            - Como criar bons nomes, boas funções, bons objetos e boas classes

            - Como formatar o código para ter uma legibilidade máxima

            - Como implementar completamente o tratamento de erro sem obscurecer a lógica

            - Como aplicar testes de unidade e praticar o desenvolvimento dirigido a testes

            - Este livro é essencial para qualquer desenvolvedor, engenheiro de software, gerente de projeto, líder de equipes ou analistas de sistemas com interesse em construir códigos melhores.
        """
    },
    {
        'name': 'Python Fluente',
        'author': 'Luciano Ramalho',
        'isbn': '857522462X',
        'cover': 'https://cache.skoob.com.br/local/images//WVGpITfarfB8QjD3zJKF-uDYOdw=/200x/center/top/smart/filters:format(jpeg)/https://skoob.s3.amazonaws.com/livros/535284/PYTHON_FLUENTE_1446838589535284SK1446838589B.jpg',
        'description': """
            A simplicidade de Python permite que você se torne produtivo rapidamente, porém isso muitas vezes significa que você não estará usando tudo que ela tem a oferecer. Com este guia prático, você aprenderá a escrever um código Python eficiente e idiomático aproveitando seus melhores recursos – alguns deles, pouco conhecidos.
            O autor Luciano Ramalho apresenta os recursos essenciais da linguagem e bibliotecas de Python mostrando como você pode tornar o seu código mais conciso, mais rápido e mais legível ao mesmo tempo.
            Muitos programadores experientes tentam dobrar o Python para que ele se enquadre em padrões aprendidos com outras linguagens e jamais descobrem os recursos do Python que estão além de sua experiência. Com este livro, esses programadores Python aprenderão a ser totalmente proficientes em Python 3.

            Este livro inclui:

            O modelo de dados do Python: entenda como os métodos especiais são o segredo para o comportamento consistente dos objetos.
            Estruturas de dados: tire total proveito dos tipos embutidos e entenda a dualidade entre texto e bytes na era do Unicode.
            Funções como objetos: veja as funções Python como objetos de primeira classe e entenda como isso afeta alguns padrões de projeto populares.
            Técnicas de orientação a objetos: crie classes após dominar referências, mutabilidade, interfaces, sobrecarga de operadores e herança múltipla.
            Controle de fluxo: tire proveito de gerenciadores de contexto, geradores, corrotinas e concorrência com os pacotes concurrent.futures e asyncio.
            Metaprogramação: entenda como funcionam propriedades, descritores de atributos, decoradores de classe e metaclasses.
        """
    },
    {
        'name': 'The Pragmatic Programmer',
        'author': 'Andrew Hunt, David Thomas',
        'isbn': '020161622X',
        'cover': 'https://cache.skoob.com.br/local/images//9eGzxcIAkt0o_M6xdIyc32tk39s=/200x/center/top/smart/filters:format(jpeg)/https://skoob.s3.amazonaws.com/livros/6427/THE_PRAGMATIC_PROGRAMMER_1231946617B.jpg',
        'description': """
            Programmers are craftspeople trained to use a certain set of tools (editors, object managers, version trackers) to generate a certain kind of product (programs) that will operate in some environment (operating systems on hardware assemblies). Like any other craft, computer programming has spawned a body of wisdom, most of which
            isn t taught at universities or in certification classes. Most programmers arrive at the so-called tricks of the trade over time, through independent experimentation. In The Pragmatic Programmer, Andrew Hunt and David Thomas codify many of the truths they ve discovered during their respective careers as designers of software and writers of code.

            Some of the authors nuggets of pragmatism are concrete, and the path to their implementation is clear. They advise readers to learn one text editor, for example, and use it for everything. They also recommend the use of version-tracking software for even the smallest projects, and promote the merits of learning regular expression syntax and a
            text-manipulation language. Other (perhaps more valuable) advice is more light-hearted. In the debugging section, it is noted that, "if you see hoof prints think horses, not zebras." That is, suspect everything, but start looking for problems in the most obvious places. There are recommendations for making estimates of time and
            expense, and for integrating testing into the development process. You ll want a copy of The Pragmatic Programmer for two reasons: it displays your own accumulated wisdom more cleanly than you ever bothered to state it, and it introduces you to methods of work that you may not yet have considered. Working programmers will enjoy this book. --David Wall


            Topics covered: A useful approach to software design and construction that allows for efficient, profitable development of high-quality products. Elements of the approach include specification development, customer relations, team management, design practices, development tools, and testing procedures. This approach is presented with
            the help of anecdotes and technical problems.
        """
    },
    {
        'name': 'TDD Desenvolvimento Guiado por Testes',
        'author': 'Kent Beck',
        'isbn': '857780724X',
        'cover': 'https://cache.skoob.com.br/local/images//_NvW_WpXbkMWn2-vRqlxNrGdrkQ=/200x/center/top/smart/filters:format(jpeg)/https://skoob.s3.amazonaws.com/livros/116735/TDD_DESENVOLVIMENTO_GUIADO_POR_TESTES_1317265394B.jpg',
        'description': """
            Este livro ilustra com exemplos práticos e reais como codificar e executar testes automatizados. O TDD prática que surgiu na XP é
            apresentado de modo simples e são abordadas algumas respostas a problemas e dúvidas comuns. O texto tem uma linguagem informal,
            criando a impressão de que o autor e o leitor estão juntos numa atividade real de desenvolvimento de software, trocando ideias, levantando dúvidas e realizando tarefas passo a passo.
        """
    },
]

class BooksController(APIHandler):
    def get(self):
        attributes = ['name', 'author', 'isbn', 'cover']
        books = []
        for data in BOOKS:
            book = {}
            for attribute in attributes:
                book[attribute] = data[attribute]
            books.append(book)

        return self.success(books)

class BookController(APIHandler):
    def get(self, isbn):
        books = [book for book in BOOKS if book['isbn'] == isbn]
        if len(books) > 0:
            self.success({'book': books[0]})
        else:
            self.set_status(404)
            self.fail({'message': 'not found'})


def make_app():
    app = tornado.web.Application(
        [
            (r"/api/books", BooksController),
            (r"/api/books/(\w+)", BookController)
        ],
        debug=DEBUG
    )
    return app


def start():

    logger.initialize_logging('books')

    app = make_app()
    app.listen(BOOKS_SERVER_PORT)

    general.info("starting server")

    tornado.ioloop.IOLoop.current().start()

if __name__ == '__main__':
    start()
