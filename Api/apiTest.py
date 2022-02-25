import requests
from unittest import mock,TestCase
from job import Job


class ApiTest(TestCase):

    def setUp(self):
        self.mock_job = mock.Mock(spec=Job)
        self.mock_job.get_all_jobs = mock.Mock(return_value=200)
        self.mock_job.get_job = mock.Mock(return_value=200)
        self.mock_job.add_job = mock.Mock(return_value=201)
        self.mock_job.update_job = mock.Mock(return_value=201)
        self.mock_job.delete_job = mock.Mock(return_value=204)

    # Get request de L'api
    def test_1_get_all_jobs(self):
        r = self.mock_job.get_all_jobs()
        statuscode = 200
        self.assertEqual(r, statuscode)


    def test_2_get_job(self):
        r = self.mock_job.get_job(1)
        statuscode = 200
        self.assertEqual(r, statuscode)


    def test_3_add_job(self):
        r = self.mock_job.add_job("Octopus IT", "Paris 8e(75)", "", "Basée à Paris, New York et Lille...", "Lead développeur backend Node.Js")
        statuscode = 201
        self.assertEqual(r, statuscode)

    def test_4_update_job(self):
        r = self.mock_job.update_job(31,"Ubisoft", "Paris 8e(75)", "75.000 € - 100.000 € par an", "Vous travaillerez au sein d’une cellule DevOps...", "Senior Développeur")
        statuscode = 201
        self.assertEqual(r, statuscode)

    def test_5_delete_job(self):
        r = self.mock_job.delete_job(31)
        statuscode = 204
        self.assertEqual(r, statuscode)
