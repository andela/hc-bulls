from hc.api.models import Check
from hc.test import BaseTestCase
from datetime import timedelta as td
from django.utils import timezone


class MyChecksTestCase(BaseTestCase):
	def setUp(self):
        super(MyChecksTestCase, self).setUp()
        self.check = Check(user=self.alice, name="Alice Was Here")
        self.check.save()

    def test_it_works(self):
        url = "/checks/add/"
        self.client.login(username="alice@example.org", password="password")
        r = self.client.post(url)
        self.assertRedirects(r, "/checks/")
        assert Check.objects.count() == 1

    def test_it_contains_message_for_no_unresolved_checks(self):
    	url = "checks/unresolved/"
    	self.client.login(username="alice@example.org", password="password")
        r = self.client.post(url)
        self.assertContains(r, "You don't have any checks not been resolved yet", status_code=200)
