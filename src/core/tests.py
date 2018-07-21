from django.test import TestCase
from . import utils
from .models import Vehicle, Report

# Create your tests here.

class VehicleTrackerTest(TestCase):

    def setUp(self):
        self.r = Report.objects.create(xml_file='sample_vehicles.xml')
        self.sample_xml_types = ['Big Wheel', 'Bicycle', 'Motorcycle', 'Hang Glider', 'Car']
        utils.parse_xml_to_db(self.r)
        self.all_vehicles = Vehicle.objects.filter(report=self.r.id)

    def test_parse_xml_to_db(self):

        all_types = [i.type for i in self.all_vehicles]

        #To test if Sample contains all 5 types

        self.assertEqual(5,len(self.all_vehicles))
        self.assertEqual(self.sample_xml_types,all_types)

    def test_get_type_by_properties(self):


        for i,vehicle in enumerate(self.all_vehicles):
            self.assertEqual(self.sample_xml_types[i],\
                             utils.get_type_by_properties(vehicle.wheels,vehicle.power_train))

    def test_get_summary(self):

        # SAMPLE SUMMARY:[['Vehicle Type', 'No of Vehicles'], ['Car', 1], ['Hang Glider', 1], ['Bicycle', 1], ['Big Wheel', 1], ['Motorcycle', 1]]

        summary = utils.get_summary(self.r.id)
        summary.pop(0)
        summary_counts = [j for i,j in summary]


        self.assertEqual(5,len(summary_counts))
        self.assertEqual({1},set(summary_counts))

    def test_get_report_details(self):

        report = utils.get_report_details(self.r.id)
        report_types = [r.type for r in report]

        self.assertEqual(self.sample_xml_types,report_types)

    def test_get_history(self):
        r2 = Report.objects.create(xml_file='sample_vehicles.xml')
        history = utils.get_history()
        report_id_in_history = [i.id for i in history]

        # Checks if id of report is returned by latest timestamp
        self.assertEqual([2,1],report_id_in_history)
