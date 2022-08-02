from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
import json

from common.json import ModelEncoder
from .models import Technician, ServiceAppointment, AutomobileVO


class AutomobileVOEncoder(ModelEncoder):
    model = AutomobileVO
    properties = ["vin"]

class TechnicianEncoder(ModelEncoder):
    model = Technician
    properties = [
        "name",
        "employee_number",

    ]


@require_http_methods(["GET", "POST"])
def api_technicians(request):
    if request.method == "GET":
        # show all technicians
        technician = Technician.objects.all()
        print("technicians all", technician)
        print("type", type(technician))
        return JsonResponse(
            {"": technician},
            encoder=TechnicianEncoder,
        )
    else: # POST
        content = json.loads(request.body)
        print("content", content)
        try:
            tech = Technician.objects.create(**content)
        except Technician.DoesNotExist:
            return JsonResponse(
                {"message": "Invalid technician"},
                status=400,
            )
        return JsonResponse(
            tech,
            encoder=TechnicianEncoder,
            safe=False,
        )

@require_http_methods(["DELETE", "GET", "PUT"])
def api_technician(request, pk):
    if request.method == "DELETE":
        count, _ = technicians.objects.filter(id=pk).delete()
        return JsonResponse({"deleted": count > 0})
    elif request.method == "GET":
        technicians = technicians.objects.get(id=pk)
        return JsonResponse(
            technicians,
            encoder=TechnicianEncoder,
            safe=False,
        )
    else: # PUT
        try:
            content = json.loads(request.body)
            Technician.objects.filter(id=pk).update(**content)
            technicians = Technician.objects.get(id=pk)
            return JsonResponse(
                technicians,
                encoder=TechnicianEncoder,
                safe=False,
            )
        except Technician.DoesNotExist:
            return JsonResponse(
                {"message": "Invalid technician"},
                status=400,
            )

class ServiceAppointmentEncoder (ModelEncoder):
    model = ServiceAppointment
    properties = ["vin",
    "customer_name",
    "appointment_date",
    "appointment_time",
    "assigned_technician",
    "service_reason",]
    
    encoders = {
        "assigned_technician": TechnicianEncoder(),
    }

@require_http_methods(["GET", "POST"])
def api_serviceapps(request):
    if request.method == "GET":
        # show all technicians
        serviceapp = ServiceAppointment.objects.all()
        print("technicians all", serviceapp)
        print("type", type(serviceapp))
        return JsonResponse(
            {"": serviceapp},
            encoder=ServiceAppointmentEncoder,
        )
    else: # POST
        content = json.loads(request.body)
        print("content", content)
        try:
            app = ServiceAppointment.objects.create(**content)
        except ServiceAppointment.DoesNotExist:
            return JsonResponse(
                {"message": "Invalid service appointment"},
                status=400,
            )
        return JsonResponse(
            app,
            encoder=ServiceAppointmentEncoder,
            safe=False,
        )

@require_http_methods(["DELETE", "GET", "PUT"])
def api_serviceapp(request, pk):
    if request.method == "DELETE":
        count, _ = ServiceAppointment.objects.filter(id=pk).delete()
        return JsonResponse({"deleted": count > 0})
    elif request.method == "GET":
        service_apps = ServiceAppointment.objects.get(id=pk)
        return JsonResponse(
            service_apps,
            encoder=ServiceAppointmentEncoder,
            safe=False,
        )
    else: # PUT
        try:
            content = json.loads(request.body)
            ServiceAppointment.objects.filter(id=pk).update(**content)
            service_apps = ServiceAppointment.objects.get(id=pk)
            return JsonResponse(
                service_apps,
                encoder=ServiceAppointmentEncoder,
                safe=False,
            )
        except ServiceAppointment.DoesNotExist:
            return JsonResponse(
                {"message": "Invalid service appointment"},
                status=400,
            )