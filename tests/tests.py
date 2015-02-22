import unittest
import json

from pyresm.app import app
from pyresm.models import Resources


USERS = ['bob', 'john', 'mary']
RNAME = 'r'
RCOUNT = 3
Resources().init(RCOUNT, RNAME)


class MainTest (unittest.TestCase):

    def setUp (self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def getAnswer (self, url):
        response = self.app.get(url)
        try:
            data = json.loads(response.data)
        except ValueError:
            data = None
        return response.status_code, data

    def allocate (self, user):
        return self.getAnswer('/allocate/{0}'.format(user))

    def assertAnswer (self, answer, need):
        self.assertEqual(answer[0], need[0])
        self.assertEqual(answer[1], need[1])

    def assertLenAnswer (self, answer, need):
        self.assertEqual(answer[0], need[0])
        self.assertEqual(len(answer[1]), need[1])

    def assertResources (self, answer, need):
        self.assertEqual(answer[0], need[0])
        self.assertEqual(len(answer[1]['allocated']), need[1])
        self.assertEqual(len(answer[1]['deallocated']), need[2])

    def test_1_list (self):
        self.assertResources(self.getAnswer('/list'), (200, 0, RCOUNT))

    def test_2_allocate (self):
        self.assertAnswer(self.allocate(USERS[0]), (201, '{0}{1}'.format(RNAME, 0)))
        self.assertAnswer(self.allocate(USERS[1]), (201, '{0}{1}'.format(RNAME, 1)))
        self.assertAnswer(self.allocate(USERS[0]), (201, '{0}{1}'.format(RNAME, 2)))
        self.assertAnswer(self.allocate(USERS[2]), (503, 'Out of resources.'))

    def test_3_list (self):
        self.assertLenAnswer(self.getAnswer('/list/{0}'.format(USERS[0])), (200, 2))
        self.assertLenAnswer(self.getAnswer('/list/{0}'.format(USERS[1])), (200, 1))
        self.assertLenAnswer(self.getAnswer('/list/{0}'.format(USERS[2])), (200, 0))
        self.assertResources(self.getAnswer('/list'), (200, RCOUNT, 0))
        
    def test_4_deallocate (self):
        self.assertAnswer(self.getAnswer('/deallocate/{0}{1}'.format(RNAME, 0)), (204, None))
        self.assertAnswer(self.getAnswer('/deallocate/{0}{1}'.format(RNAME, RCOUNT + 1)), (404, 'Not allocated.'))
        self.assertResources(self.getAnswer('/list'), (200, RCOUNT-1, 1))

    def test_5_reset (self):
        self.assertAnswer(self.getAnswer('/reset'), (204, None))
        self.assertResources(self.getAnswer('/list'), (200, 0, RCOUNT))


if __name__ == '__main__':
    unittest.main()

