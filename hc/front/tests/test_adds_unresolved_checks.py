from hc.api.models import Check
from hc.test import BaseTestCase
from datetime import timedelta as td
from django.utils import timezone


class MyChecksTestCase(BaseTestCase):
	def setUp(self):
		super(MyChecksTestCase, self).setUp()
		self.check = Check(user=self.alice, name="A simple test ping", timeout="td(seconds=60)", grace="td(seconds=60)")
		self.check.save()

	def test_it_creates_the_check(self):
		self.client.login(username='alice@example.org', password='password')
		response = self.client.get("/checks/")
		self.assertContains(response, "A simple test ping", status_code=200)