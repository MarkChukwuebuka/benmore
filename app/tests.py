from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Task
from rest_framework import status

class TaskViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        
        self.task1 = Task.objects.create(
            title='Test Task 1',
            description='This is a test task 1',
            status='In Progress',
            priority='Medium',
            due_date='2023-01-01T00:00:00Z',
            category='Test Category',
            assigned_to=self.user
        )
        
        self.task2 = Task.objects.create(
            title='Test Task 2',
            description='This is a test task 2',
            status='Completed',
            priority='High',
            due_date='2023-02-01T00:00:00Z',
            category='Another Category',
            assigned_to=self.user
        )

    def test_task_list_view(self):
        response = self.client.get(reverse('task-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Task 1')
        self.assertContains(response, 'Test Task 2')

    def test_task_detail_view(self):
        response = self.client.get(reverse('task-detail', kwargs={'pk': self.task1.pk}))
        self.assertEqual(response.status_code, 200)
        # print(response)
        self.assertContains(response, 'Test Task 1')

    def test_task_create_view(self):
        data = {
            'title': 'New Task',
            'description': 'This is a new task',
            'status': 'In Progress',
            'priority': 'High',
            'due_date': '2023-03-01T00:00:00Z',
            'category': 'New Category',
            'assigned_to': self.user.id
        }
        response = self.client.post(reverse('task-create'), data)
        self.assertEqual(response.status_code, 302)  # Redirects after success
        self.assertEqual(Task.objects.count(), 3)
        self.assertEqual(Task.objects.last().title, 'New Task')

    def test_task_update_view(self):
        data = {
            'title': 'Updated Task 1',
            'description': 'This is an updated task 1',
            'status': 'In Progress',
            'priority': 'Low',
            'due_date': '2023-01-01T00:00:00Z',
            'category': 'Updated Category',
            'assigned_to': self.user.id
        }
        response = self.client.post(reverse('task-update', kwargs={'pk': self.task1.pk}), data)
        self.assertEqual(response.status_code, 302)  # Redirects after success
        self.task1.refresh_from_db()
        self.assertEqual(self.task1.title, 'Updated Task 1')

    def test_task_delete_view(self):
        response = self.client.post(reverse('task-delete', kwargs={'pk': self.task1.pk}))
        self.assertEqual(response.status_code, 302)  # Redirects after success
        self.assertEqual(Task.objects.count(), 1)


class TaskAPIByStatusTest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        refresh = RefreshToken.for_user(self.user)
        self.access_token = str(refresh.access_token)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        
        self.task1 = Task.objects.create(
            title='Test Task 1',
            description='This is a test task 1',
            status='In Progress',
            priority='Medium',
            due_date='2023-01-01T00:00:00Z',
            category='Test Category',
            assigned_to=self.user
        )
        
        self.task2 = Task.objects.create(
            title='Test Task 2',
            description='This is a test task 2',
            status='Completed',
            priority='High',
            due_date='2023-02-01T00:00:00Z',
            category='Another Category',
            assigned_to=self.user
        )

    def test_get_task_by_status(self):
        response = self.client.get(reverse('task-by-status', kwargs={'status': 'In Progress'}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Test Task 1')

        response = self.client.get(reverse('task-by-status', kwargs={'status': 'Completed'}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Test Task 2')
