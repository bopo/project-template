# -*- coding: utf-8 -*-
from django.contrib.auth import get_user_model
from rest_framework import status

from .common import BaseAPITestCase


class TestAppFeedbackCase(BaseAPITestCase):
    def setUp(self):
        self.init()

        owenr = get_user_model()()
        owenr.save()

        self._generate_uid_and_token(user=owenr)
        self.client.credentials(HTTP_AUTHORIZATION='Token %s' % self.token)

    def test_feedback_commit(self):
        data = {
            "title": "test",
            "content": "content",
            "phone": "12312312"
        }
        response = self.client.post("/api/feedback/", data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_feedback_list(self):
        response = self.client.get("/api/feedback/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
