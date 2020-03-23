from flask import Flask, render_template
from flask_graphql import GraphQLView
import graphene

app = Flask(__name__)


#graphql con graphene

class Query(graphene.ObjectType):
    saludo = graphene.String()
    
    def resolve_saludo(self, info):
        return "Hola como estas?"


schema = graphene.Schema(query=Query)

schema.execute('''
  query {
    saludo
  }
''')
#ruta de configuracion de flask_graphql
app.add_url_rule('/graphql', view_func=GraphQLView.as_view('/graphql', schema=schema, graphiql=True))

if __name__ == '__main__':
    app.run(debug=True, port=3000)