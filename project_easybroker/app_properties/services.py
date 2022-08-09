import math
import requests
import re 
from urllib.parse import urljoin
from .constants import BASE_URL, BASE_URL_PROPERTIES, HEADERS,HEADERS_CONTENT,BASE_URL_CONTACT

class PropertiesService:
    
    payload = {}
    pagination = {}
    
    def __init__(self):
        print(" --- PropertiesService --- ")
    
    def get_properties_object(self, params={}):
        code, payload = ConsumeEachEndpointProperty().get_properties_response(params)
        self.payload = ValidateService().validate_properties_response(code, payload)
        pagination_data = self.get_pagination_data()
        return self.payload, pagination_data 
    
    def get_pagination_data(self):
        if 'pagination' in self.payload: 
            self.pagination = self.payload['pagination']
            num_pages = math.ceil(int(self.pagination['total'])/ int(self.pagination['limit']))
            current_page_int = int(self.pagination['page'])
            return ValidateService().validate_pagination_data(num_pages,current_page_int)
        else:
            return {'num_pages':0, 'current_page':0}

class PropertyService:

    def __init__(self):
        print(" --- PropertyService --- ")

    def get_property_object(self, id_property={}):
        code, payload = ConsumeEachEndpointProperty().get_property_response(id_property)
        payload = ValidateService().validate_properties_response(code, payload)
        return payload

class ContactService:

    def __init__(self):
        print(" --- ContactService --- ")

    def post_contact_object(self, source, property_id,data_validate):
        code, payload = ConsumeEachEndpointProperty().post_contact_request( source, property_id,data_validate)
        payload = ValidateService().validate_properties_response(code, payload)
        return payload

class ConsumeEachEndpointProperty:
     
    PARAMS = { 'limit':15 , 'search[statuses][]':'published'}
    
    def __init__(self):
        print(" --- ConsumeEachEndpointProperty --- ")
    
    def get_properties_response(self, params={}):
        response = requests.get(BASE_URL_PROPERTIES, params={**self.PARAMS,**params}, headers=HEADERS)
        return response.status_code, response.json()

    def get_property_response(self, id_property=''):
        url = urljoin(BASE_URL_PROPERTIES+'/',id_property)
        response = requests.get(url, headers=HEADERS)
        return response.status_code, response.json()

    def post_contact_request(self, source, property_id,data_validate):
        json_body = self.create_json_body(source, property_id, data_validate)
        response = requests.post(BASE_URL_CONTACT, json = json_body, headers=HEADERS_CONTENT)
        return response.status_code, response.json()
        
    def create_json_body(self, source, property_id,data_validate):
        json_body = {
            'name':data_validate['name'],
            'phone':data_validate['phone'],
            'email':data_validate['email'],
            'property_id':property_id,
            'message':data_validate['message'],
            'source':source
        }
        return json_body

  

class ValidateService:

    def validate_properties_response(self, code, payload):
        if code == 200:
            return payload
        else:
            if isinstance(payload,PropertiesService): 
                return {**{'pagination':{}},**{'content':[]},**payload}
            else:
                return payload
    
    def validate_contact_form(self, data_form):
        context_data={}
        if not(data_form['name']):
            context_data['valida_nombre'] = '*Falta agregar nombre'
        if not(data_form['phone']):
            context_data['valida_phone'] = '*Falta agregar número'     
        else:
            if len(data_form['phone']) < 10:
                context_data['valida_phone'] = '*Número incompleto'     
        if not(data_form['email']):
            context_data['valida_email'] = '*Falta agregar email'
        if not(re.match(r"^[^@]+@[^@]+\.[a-zA-Z]{2,}$",data_form['email'])):
            context_data['valida_email'] = '*Email inválido'
        if not(data_form['message']):
            context_data['valida_message'] = '*Aguegar un mensaje'
        return context_data

    def validate_pagination_data(self, num_pages,current_page_int):
        pagination_data ={}

        if num_pages > 2 :
            pagination_data = {'num_pages':num_pages,'current_page':current_page_int}
            if 2 <= current_page_int <= (num_pages - 1):
                pagination_data = {**pagination_data, **{'previous_page':current_page_int-1, 'next_page':current_page_int+1}}
            elif current_page_int == 1: 
                pagination_data = {**pagination_data, **{'next_page1':current_page_int+1, 'next_page2':current_page_int+2}}
            else: 
                pagination_data = {**pagination_data, **{'previous_page2':current_page_int-2,'previous_page1':current_page_int-1}}
        else: 
            pagination_data = {'num_pages':num_pages, 'current_page': num_pages,}
            if num_pages == 2 and num_pages < current_page_int:
                pagination_data = {**pagination_data, **{'next_page':num_pages+1}}
        return pagination_data