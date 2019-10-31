from flask import Flask, render_template, request, redirect
from pprint import pprint

import httplib2
from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

credentials = GoogleCredentials.get_application_default()

service = discovery.build('cloudresourcemanager', 'v1', credentials=credentials)

crm = discovery.build(
    'cloudresourcemanager', 'v1', http=credentials.authorize(httplib2.Http()))

projects = crm.projects().list().execute()

app = Flask(__name__)

class Projeto:
    def __init__(self, createTime, lifecycleState, name, parent, projectId, projectNumber):
        self.createTime = createTime
        self.lifecycleState = lifecycleState
        self.name = name
        self.parent = parent
        self.projectId = projectId
        self.projectNumber = projectNumber

lista = projects['projects']
pprint(lista)

service = discovery.build('sqladmin', 'v1beta4', credentials=credentials)
#request = service.instances().list(project='fine-justice-257413', zone='us-west1')
project = 'fine-justice-257413'
instance = 'smarterp-teste'
database_instance_body = {

}
request = service.instances().patch(project=project, instance=instance, body=database_instance_body)
response = request.execute()

# TODO: Change code below to process the `response` dict:
pprint(response)

@app.route('/')
def index():
    return render_template('home.html', titulo='Projetos no GCP',
                           projetos=lista)

@app.route('/criardb', methods=['POST',])
def criar():
    # The Project ID (for example, `my-project-123`).
    # Required.
    #project_id = 'fine-justice-257413'

    #request = service.projects().get(projectId=project_id)
    #response = request.execute()

    #pprint(response)

    nome = request.form['nome']
    categoria = request.form['categoria']
    codigo = request.form['codigo']
    projeto = Projeto(nome, categoria, codigo)
    lista.append(projeto)
    return redirect('/')

app.run(debug=True)
