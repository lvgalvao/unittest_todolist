from datetime import datetime
from unittest import TestCase, mock
from app.todo import nova_task, process_date
# from app.database import insert_task

"""
{
    'id': int,
    'task_name': str,
    'date': str,
    'state': str['Backlog', 'Fazendo', 'Pronto']
}

"""

class TestNovaTask(TestCase):
    def test_nova_task(self):
        esperado = {
            'id': 1,
            'task_name': 'Ligar para o will',
            'date': datetime(2022, 2, 19, 0, 0, 0),
            'state': 'TODO'
        }
        result = nova_task('Ligar para o will', '19/02/2022')
        
        self.assertEqual(esperado, result)
    
    @mock.patch('app.todo.process_date')
    def test_process_date_deve_ser_chamado_com_19_02_2022(self, mocked):
        nova_task('', '19/02/2022')
        mocked.assert_called_with('19/02/2022')
    
    @mock.patch('app.todo.insert_task')
    def test_insert_task_deve_ser_chamado_com_o_objeto_da_task(self, mocked):
        # chama a função
        result = nova_task('Ligar para o will', '19/02/2022')
        mocked.assert_called_with(result)

class TestProcessData(TestCase):
    def test_process_date_deve_converter_para_datetime_a_string_passada(self):
        """
        19/02/2022 -> datetime(2022, 2, 19, 0, 0, 0)
        """
        esperado = datetime(2022, 2, 19, 0, 0, 0)
        
        result = process_date('19/02/2022')

        self.assertEqual(esperado, result)

class TestListarTasks(TestCase):
    ...