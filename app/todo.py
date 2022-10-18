from datetime import datetime
from .database import insert_task, select_tasks

def identificador():
    state = 0
    while True:
        state += 1
        yield state

def process_date(string_date: str):
    """insere a data fim da task"""
    return datetime.strptime(string_date,'%d/%m/%Y')

def nova_task(task_name: str, date: str):
    """insere uma nova task na lista de task"""

    task = {
        'id': next(identificador()),
        'task_name': task_name,
        'date': process_date(date),
        'state': 'TODO'
    }
    result_db = insert_task(task)
    return task
    
def listar_tasks(task_name: str, state: str = ''):
    return select_tasks(task_name, state)