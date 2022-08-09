from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.views.generic import TemplateView
from django.urls import reverse

from . import services


class HomeView(TemplateView):
    template_name = 'app_properties/card.html'
    
    def get_context_data(self, *args, **kwargs):
        payload, pagination_data  = validate_kwargs_home(kwargs)
        context = {
            'properties_data': payload,
            'pagination_data': pagination_data
        }
        return context


def validate_kwargs_home(kwargs):
    cosume_properties = services.PropertiesService()
    kwargs = kwargs if kwargs else {'page':1}  
    payload, pagination_data = cosume_properties.get_properties_object(params={'page':kwargs['page']})
    if int(pagination_data['current_page']) > int(pagination_data['num_pages']):
        kwargs['page'] = 1
        payload, pagination_data = cosume_properties.get_properties_object(params={'page':kwargs['page']})
    return payload, pagination_data


class PropertyView(TemplateView):
    template_name = 'app_properties/property.html'
    cosume_property = services.PropertyService()
    def get_context_data(self, *args, **kwargs):
        if not('status' in kwargs):
            kwargs['status'] = ''
        payload_property = self.cosume_property.get_property_object(id_property =kwargs['property_id'])
        context = {
            'payload_property': payload_property,
            'status': kwargs['status']
        }
        return context 


class Error400View(TemplateView):
    template_name = 'app_properties/page400.html'

class Error404View(TemplateView):
    template_name = 'app_properties/page404.html'
    

def ContactView(request,property_id):   
    data_validate ={}
    try:
        data_validate = request.POST
        context_data = services.ValidateService().validate_contact_form(data_validate)
        if (context_data):
            raise ValueError("Data incompleta")
    except :
        payload_property = services.PropertyService().get_property_object(id_property = property_id)
        return render(request, 'app_properties/property.html',{
            'payload_property': payload_property,
            'property_images': payload_property['property_images'],
            'error_message': context_data,
            'data_validate': data_validate
        })
    else:
        payload_response = services.ContactService().post_contact_object(request.META['HTTP_HOST'], property_id, data_validate)

        if 'error' in payload_response:
            message = payload_response['error']
        else:
            message = payload_response['status']
        return HttpResponseRedirect(reverse('easybroker:property', kwargs={'property_id':property_id, 'status': message}))

