from django.urls import reverse
from django.test import TestCase
import unittest
from unittest.mock import Mock, patch
import json
from .services import ConsumeEachEndpointProperty, ValidateService


filejson_get_properties = open('./app_properties/static/app_properties/get_properties.json',encoding="utf8")
contents_get_properties = json.load(filejson_get_properties)

filejson_get_property = open('./app_properties/static/app_properties/get_property.json',encoding="utf8")
contents_get_property = json.load(filejson_get_property)

# Create your tests here.

class TestConsumeEachEndpointGetProperties(unittest.TestCase):


    def test_getting_properties_when_response_is_ok(self):
        actual = contents_get_properties['pagination']
        actual_keys = actual

        # Call the service to hit the mocked API.
        with patch('app_properties.services.requests.get') as mock_get:
            mock_get.return_value.ok = False
            mock_get.return_value.json.return_value = { 
                "limit": 15,
                "page": 1,
                "total": 460,
                "next_page": "https://api.stagingeb.com/v1/properties?limit=15&page=2&search%5Bstatuses%5D%5B%5D=published"
            }
        
            code, mocked = ConsumeEachEndpointProperty().get_properties_response()
            
            mocked_keys = mocked

        # An object from the actual API and a object from the mocked API should have
        # the same data structure.
        self.assertListEqual(list(actual_keys), list(mocked_keys))
        filejson_get_properties.close()

class TestConsumeEachEndpointGetProperty(TestCase):

    def test_getting_completed_property_when_property_is_ok(self):
        actual = contents_get_property
        actual_keys = actual

        with patch('app_properties.services.requests.get') as mock_get:
            mock_get.return_value.ok = False
            mock_get.return_value.json.return_value = contents_get_property
            
            code, datadata_get_property_response = ConsumeEachEndpointProperty().get_property_response()
        
            mocked_keys = datadata_get_property_response

        self.assertListEqual(list(actual_keys), list(mocked_keys))
        filejson_get_properties.close()

class TestConsumeEachEndpointPostContact(TestCase):

    def test_getting_completed_contact_request_when_response_is_ok(self):
        actual = {"status": "successful"}
        actual_keys = actual
        json_boy ={
            'name':"Argeo Thelia",
            'phone':"2222123123", 
            'email':"EB-B5338",
            'message':"I'm interested in this property. Please contact me.",
        }

        with patch('app_properties.services.requests.post') as mock_post:
            mock_post.return_value.ok = False
            mock_post.return_value.json.return_value = {"status": "successful"}
            
            code, datadata_post_contact_requests_response = ConsumeEachEndpointProperty().post_contact_request(source="127.0.0.1:8000",property_id="EB-B5338",data_validate=json_boy)
        
            mocked_keys = datadata_post_contact_requests_response

        self.assertListEqual(list(actual_keys), list(datadata_post_contact_requests_response))
        filejson_get_properties.close()


class TestHomeView(TestCase):
    def test_view_home_page(self):
        
        response = self.client.get(reverse('easybroker:home'))
        
        self.assertEqual(response.status_code, 200)
        
        self.assertListEqual(list(response.context['properties_data']), list(['pagination', 'content']))