import xml.etree.ElementTree as ET
from .models import Vehicle,Report
from collections import Counter

def get_type_by_properties(wheels,power_train):
    no_of_wheels = len(wheels)
    type=None
    options = {0:"Hang Glider",3:"Big Wheel",4:"Car"}
    if no_of_wheels == 2:
        type = "Bicycle" if power_train.lower() == "human" else "Motorcycle"
    else:
        type = options.get(no_of_wheels)
    return type


def parse_xml_to_db(report_object):
    tree = ET.parse(report_object.xml_file)
    root = tree.getroot()

    all_vehicles = root.findall('vehicle')
    for vehicle in all_vehicles:
        frame = vehicle.find('frame/material').text
        power_train = vehicle.find('powertrain')[0].tag
        all_wheels = vehicle.find('wheels') or []
        wheels=[]
        for w in all_wheels:
            material = w.find('material').text
            position = w.find('position').text
            wheels.append({"material":material,"position":position})
        vehicle_type = get_type_by_properties(wheels,power_train)
        Vehicle.objects.create(type=vehicle_type,frame=frame,power_train=power_train,wheels=wheels,report=report_object)

def get_summary(report_id):
    vehicle_types = [v.type for v in Vehicle.objects.filter(report=report_id)]
    c = dict(Counter(vehicle_types))
    summ=[[key,value] for key,value in zip(c.keys(),c.values())]
    summ.insert(0,['Vehicle Type','No of Vehicles'])
    return summ

def get_report_details(report_id):
    vehicles = list(Vehicle.objects.filter(report=report_id))
    return vehicles


print(get_summary(12))
