from django.test import TestCase, Client

from .models import Student

# Create your tests here.


class StudentTestCase(TestCase):

    def setUp(self):
        Student.objects.create(
            name='the5fire',
            sex=1,
            email='text@example.com',
            profession='程序员',
            qq='3333',
            phone='1234566',
        )

    def test_create_and_sex_show(self):
        student = Student.objects.create(
            name='huyang',
            sex=2,
            email='text@example.com',
            profession='程序员',
            qq='3333',
            phone='1234566',
        )
        self.assertEqual(student.sex_show, '男', '性别字段内容跟展示的不一致！')

    def test_filter(self):
        Student.objects.create(
            name='huyang',
            sex=1,
            email='text@example.com',
            profession='程序员',
            qq='3333',
            phone='1234566',
        )
        name = 'the5fire'
        students = Student.objects.filter(name=name)
        self.assertEqual(students.count(), 1, '应该只存在一条名称为{}的记录'.format(name))

    def test_get_index(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200, 'status code must be 200!')

    def test_post_student(self):
        client = Client()
        data = dict(
            name='test_for_post',
            sex=1,
            email='text@example.com',
            profession='程序员',
            qq='3333',
            phone='1234566',
        )
        response = client.post('/', data)
        self.assertEqual(response.status_code, 302, 'status code must be 302!')

        response = client.get('/')
        self.assertTrue(b'test_for_post' in response.content, 'response content must contain \'test_for_post\'')
