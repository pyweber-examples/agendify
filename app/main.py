import pyweber as pw
from database.database import Database
from datetime import datetime
import requests

app = pw.Pyweber()
db = Database()

def set_tasks(tasks: list[list]):
    return {str(task[0]): {
        'title': task[1],
        'description': task[2],
        'datetime': task[3],
        'email': task[4],
        'status': task[5]
        } for task in tasks
    }

class TaskCard(pw.Element):
    def __init__(self, id, **kwargs):
        super().__init__(tag='div', classes=['task-card'])
        self.id = id
        self.kwargs = kwargs
        self.childs = [
            pw.Element(
                tag='div',
                classes=['task-header'],
                childs=[
                    pw.Element(tag='h3', content=kwargs.get('title')),
                    pw.Element(
                        tag='span',
                        content=kwargs.get('status'),
                        classes=['status-badge', f'status-{kwargs.get('status')}']
                    )
                ]
            ),
            pw.Element(
                tag='p',
                content=kwargs.get('description'),
                classes=['task-description']
            ),
            pw.Element(
                tag='div',
                classes=['task-meta'],
                childs=[
                    pw.Element(
                        tag='span',
                        classes=['task-mail'],
                        childs=[
                            pw.Element(
                                tag='a',
                                attrs={'href': f'mailto:{kwargs.get('email')}'},
                                content='Email'
                            )
                        ]
                    ),
                    pw.Element(tag='span', classes=['task-date'], content=kwargs.get('datetime'))
                ]
            ),
            pw.Element(
                tag='div',
                classes=['task-actions'],
                childs=[
                    pw.Element(
                        tag='button',
                        classes=['btn', 'btn-edit'],
                        content='Editar',
                        events=pw.TemplateEvents(onclick=self.edit)
                    ),
                    pw.Element(
                        tag='button',
                        classes=['btn', 'btn-delete'],
                        content='Apagar',
                        events=pw.TemplateEvents(onclick=self.delete)
                    )
                ]
            )
        ]
    
    def edit(self, e: pw.EventHandler):
        e.template.querySelector('.modal').style['display'] = 'block'

        e.template.querySelector('#editTitle').value = self.kwargs.get('title')
        e.template.querySelector('#editDescription').value = self.kwargs.get('description')
        e.template.querySelector('#editEmail').value = self.kwargs.get('email')
        e.template.querySelector('#editStatus').value = self.kwargs.get('status')
        e.template.querySelector('#editTaskId').value = self.id

        e.update()
    
    def delete(self, e: pw.EventHandler):
        task = e.element.parent.parent
        db.delete_data(id=task.attrs.get('data-id'))
        task.parent.childs.remove(task)

        e.update()

class Home(pw.Template):
    def __init__(self):
        super().__init__(template='index.html', title='Agendify')
        self.scroll_to_start = lambda _: pw.window.scroll_to(x=0, y=0, behavior='smooth')

        self.querySelector('#btn-create-task').add_event(
            event_type=pw.EventType.CLICK,
            event_handler=self.create_task
        )

        self.querySelector('#btn-filtrar').add_event(
            event_type=pw.EventType.CLICK,
            event_handler=self.list_tasks
        )

        self.querySelector('#statusFilter').add_event(
            event_type=pw.EventType.INPUT,
            event_handler=self.list_tasks
        )

        self.querySelector('.to-up').add_event(
            event_type=pw.EventType.CLICK,
            event_handler=self.scroll_to_start
        )

        self.querySelector('.to-up').childs[-1].add_event(
            event_type=pw.EventType.CLICK,
            event_handler=self.scroll_to_start
        )

        self.querySelector('.close').add_event(
            event_type=pw.EventType.CLICK,
            event_handler=self.close_modal
        )

        self.querySelector('#edit-cancel').add_event(
            event_type=pw.EventType.CLICK,
            event_handler=self.close_modal
        )

        self.querySelector('#edit-save').add_event(
            event_type=pw.EventType.CLICK,
            event_handler=self.edit_task
        )

        self.list_tasks(e=None)
    
    def close_modal(self, e: pw.EventHandler):
        e.template.querySelector('.modal').style['display'] = 'none'
        e.update()
    
    def edit_task(self, e: pw.EventHandler):
        id = e.template.querySelector('#editTaskId').value

        data = {
            'title': e.template.querySelector('#editTitle').value,
            'description': e.template.querySelector('#editDescription').value,
            'email': e.template.querySelector('#editEmail').value,
            'status': e.template.querySelector('#editStatus').value
        }

        if all(value for value in data.values()):
            requests.request(
                url=f'{pw.window.location.origin}/api/tasks/{id}',
                method='put',
                data=data
            )

        self.close_modal(e)
        self.list_tasks(e)
    
    def create_task(self, e: pw.EventHandler):
        template = e.template

        title = template.querySelector('#title')
        description = template.querySelector('#description')
        email = template.querySelector('#email')
        status = template.querySelector('#status')

        data: dict[str, str] = {
            'title': title.value,
            'description': description.value,
            'datetime': datetime.now(),
            'email': email.value,
            'status': status.value
        }

        if all(value for value in data.values()):
            requests.request(
                url=f'{pw.window.location.origin}/api/task',
                method='POST',
                data=data
            )

        
            title.value = ''
            description.value = ''
            email.value = ''

            self.list_tasks(e)

            e.update()
    
    def list_tasks(self, e: pw.EventHandler):
        container = e.template.querySelector('#tasksContainer') if e else self.querySelector('#tasksContainer')
        status = e.template.querySelector('#statusFilter').value if e else self.querySelector('#statusFilter').value

        container.childs.clear()
        
        container.childs.extend([
            TaskCard(
                id=id,
                **task
            ) for id, task in set_tasks(tasks=db.get_task(status=status)).items()
        ])

        if e:
            e.update()

@app.route('/redirect')
def redirect():
    return pw.Element(tag='h2', content='Hello world')

@app.route('/', title='Hello world')
def home():
    return Home()

@app.route('/api/task', methods=['post'])
def create_task():
    task_details = app.request.body

    title = task_details.get('title')
    description = task_details.get('description')
    full_date = datetime.now()
    email = task_details.get('email')
    status = task_details.get('status')

    if title and description and datetime and email and status:
        task_id = db.insert_task(title, description, full_date, email, status)

        if isinstance(task_id, int):
            return task_id
        else:
            return {'message': f'Error: {task_id}', 'status': 'error'}
    
    return {'message': 'Please fill all fields', 'status': 'warning'}

@app.route('/api/tasks')
def get_tasks():
    params = app.request.query_params.get('status', None)
    return set_tasks(tasks=db.get_task(status=params))

@app.route('/api/tasks/{id}', methods=['put', 'get'])
def edit_task(id: str):
    if app.request.method.lower() == 'get':
        return set_tasks(tasks=db.get_task_by_id(id=id))
    else:
        response = db.update_task(id=id, **app.request.body)

        if response:
            return {'message': f'Task with id {id} was updatted sucessfully', 'status': 'sucess'}
        
        elif response == False:
            return {'message': f'None task with id {id} founded', 'status': 'error'}
        
        return {'message': 'None value to change, because request body is null', 'status': 'warning'}

if __name__ == '__main__':
    app.run()