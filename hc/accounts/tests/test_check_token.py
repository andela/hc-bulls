from django.contrib.auth.hashers import make_password
from hc.test import BaseTestCase
from hc.accounts import views


class CheckTokenTestCase(BaseTestCase):

    def setUp(self):
        super(CheckTokenTestCase, self).setUp()
        self.profile.token = make_password("secret-token")
        self.profile.save()

    def test_it_shows_form(self):
        r = self.client.get("/accounts/check_token/alice/secret-token/")
        self.assertContains(r, "You are about to log in")

    def test_it_redirects(self):
        r = self.client.post("/accounts/check_token/alice/secret-token/")
        self.assertRedirects(r, "/checks/")

        # After login, token should be blank
        self.profile.refresh_from_db()
        self.assertEqual(self.profile.token, "")

    ### Login and test it redirects already logged in
    def test_it_redirects_already_logged_in(self):
        # Login
        self.client.login(username="alice@example.org", password="password")
        # Login again, check it redirects
        url = "/accounts/check_token/alice/secret-token/"
        r = self.client.post(url)
        self.assertRedirects(r, "/checks/")

    ### Login with a bad token and check that it redirects
    def test_it_redirects_after_login_with_a_bad_token(self):
        # Login with a bad token
        resp = views.check_token("alice", "bad-token")
        self.assertRedirects(resp, "/accounts/login/")
        self.assertContains(r, "Bad token")

    ### Any other tests?