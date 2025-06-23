from django.test import TestCase, Client
import json


class TimestampAPITestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_valid_unix_timestamp(self):
        """Test that a valid Unix timestamp returns correct data"""
        response = self.client.get('/api/timestamp/1451001600000/')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertIsNotNone(data['unix'])
        self.assertIsNotNone(data['utc'])
        self.assertEqual(data['unix'], 1451001600000)

    def test_valid_date_string(self):
        """Test that a valid date string returns correct data"""
        response = self.client.get('/api/timestamp/2015-12-25/')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertIsNotNone(data['unix'])
        self.assertIsNotNone(data['utc'])
        self.assertEqual(data['utc'], 'Fri, 25 Dec 2015 00:00:00 GMT')

    def test_invalid_input_returns_null(self):
        """Test that invalid input returns null for both properties"""
        # Test with non-date, non-timestamp string
        response = self.client.get('/api/timestamp/invalid-input/')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertIsNone(data['unix'])
        self.assertIsNone(data['utc'])

    def test_empty_string_returns_null(self):
        """Test that empty string returns null for both properties"""
        response = self.client.get('/api/timestamp//')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertIsNone(data['unix'])
        self.assertIsNone(data['utc'])

    def test_garbage_string_returns_null(self):
        """Test that garbage string returns null for both properties"""
        response = self.client.get('/api/timestamp/abc123def456/')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertIsNone(data['unix'])
        self.assertIsNone(data['utc'])

    def test_malformed_date_returns_null(self):
        """Test that malformed date returns null for both properties"""
        response = self.client.get('/api/timestamp/13-45-2023/')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertIsNone(data['unix'])
        self.assertIsNone(data['utc'])

    def test_negative_unix_timestamp_returns_null(self):
        """Test that negative Unix timestamp returns null for both properties"""
        response = self.client.get(
            '/api/timestamp/-1451001600000/'
        )
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertIsNone(data['unix'])
        self.assertIsNone(data['utc'])

    def test_response_structure(self):
        """Test that response always has the correct structure"""
        response = self.client.get('/api/timestamp/2015-12-25/')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertIn('unix', data)
        self.assertIn('utc', data)
        self.assertIsInstance(data['unix'], (int, type(None)))
        self.assertIsInstance(data['utc'], (str, type(None)))
