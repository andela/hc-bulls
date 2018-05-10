from hc.api.models import Check
from hc.test import BaseTestCase
from datetime import timedelta as td
from django.utils import timezone
from .test_my_checks import MyChecksTestCase

class UserAccessReportDashboard(BaseTestCase):
    def setUp(self):
        """ Start the test by setting up a check """
        super(UserAccessReportDashboard, self).setUp()
        self.check = Check(user=self.alice, name="confirm reports", timeout=td(seconds=120), grace=td(seconds=120))
        self.check.save()

    def test_the_dashboard_works(self):
        """ Test dashboard exists but without check reports """
        url = "/accounts/reports/"
        self.client.login(username="alice@example.org", password="password")
        r = self.client.get(url)
        self.assertContains(r, "You don't have any reports yet.", status_code=200)

    def test_reports_display_on_dashboard(self):
        """ Test a report exists after a check is pinged """
        # ping a check
        self.check.last_ping = timezone.now()
        self.check.save()
        # now a report exists
        url = "/accounts/reports/"
        self.client.login(username="alice@example.org", password="password")
        r = self.client.get(url)
        self.assertContains(r, "confirm reports", status_code=200)
