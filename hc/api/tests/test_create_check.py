import json

from hc.api.models import Channel, Check
from hc.test import BaseTestCase


class CreateCheckTestCase(BaseTestCase):
    URL = "/api/v1/checks/"

    def setUp(self):
        super(CreateCheckTestCase, self).setUp()

    def post(self, data, expected_error=None):
        r = self.client.post(self.URL, json.dumps(data),
                             content_type="application/json")

        if expected_error:
            self.assertEqual(r.status_code, 400)
            ### Assert that the expected error is the response error DONE
            
            self.assertEqual(expected_error,r.json()["error"])

        return r

    def test_it_works(self):
        r = self.post({
            "api_key": "abc",
            "name": "Foo",
            "tags": "bar,baz",
            "timeout": 3600,
            "grace": 60
        })

        self.assertEqual(r.status_code, 201)

        doc = r.json()
        assert "ping_url" in doc
        self.assertEqual(doc["name"], "Foo")
        self.assertEqual(doc["tags"], "bar,baz")
        
        self.assertEqual(doc["last_ping"],None)
        self.assertEqual(doc["n_pings"],0)
        ### Assert the expected last_ping and n_pings values DONE

        self.assertEqual(Check.objects.count(), 1)
        check = Check.objects.get()
        self.assertEqual(check.name, "Foo")
        self.assertEqual(check.tags, "bar,baz")
        self.assertEqual(check.timeout.total_seconds(), 3600)
        self.assertEqual(check.grace.total_seconds(), 60)

    def test_it_accepts_api_key_in_header(self):
        payload = json.dumps({"name": "Foo"})

        ### Make the post request and get the response DONE
        response=self.client.post(self.URL,payload,content_type="application/json",HTTP_X_API_KEY="abc")
        # r = {'status_code': 201} ### This is just a placeholder variable
        json_response=response.json()
        
        self.assertEqual(json_response["name"], "Foo")
        

    def test_it_handles_missing_request_body(self):
        ### Make the post request with a missing body and get the response DONE
        payload = json.dumps({"name": "Foo"})
        response=self.client.post(self.URL, content_type="application/json")
        response_json=response.json()
        # r = {'status_code': 400, 'error': "wrong api_key"} ### This is just a placeholder variable
        
        self.assertEqual(response_json["error"], "wrong api_key")

    def test_it_handles_invalid_json(self):
        ### Make the post request with invalid json data type DONE
        # r = {'status_code': 400, 'error': "could not parse request body"} ### This is just a placeholder variable
        response=self.client.post(self.URL,"invalid json",content_type="application/json")
        response_json=response.json()
        
        self.assertEqual(response_json["error"],"could not parse request body")
        # self.assertEqual(r['status_code'], 400)
        # self.assertEqual(r["error"], "could not parse request body")

    def test_it_rejects_wrong_api_key(self):
        self.post({"api_key": "wrong"},
                  expected_error="wrong api_key")

    def test_it_rejects_non_number_timeout(self):
        self.post({"api_key": "abc", "timeout": "oops"},
                  expected_error="timeout is not a number")

    def test_it_rejects_non_string_name(self):
        self.post({"api_key": "abc", "name": False},
                  expected_error="name is not a string")

    ### Test for the assignment of channels NOT DONE
    ### Test for the 'timeout is too small' and 'timeout is too large' errors DONE

    def test_timeout_too_long(self):
        self.post({"api_key": "abc", "timeout":1000000000},
                  expected_error="timeout is too large")

    def test_timeout_too_short(self):
        self.post({"api_key": "abc", "timeout":0},
                  expected_error="timeout is too small")



