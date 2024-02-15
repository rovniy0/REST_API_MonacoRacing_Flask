
from flask import Flask, request, jsonify, abort
from flask_restful import Resource
from report_racing_app.models import Driver
from flasgger import swag_from
from dicttoxml import dicttoxml
from peewee import DoesNotExist


app = Flask(__name__)


class GetReport(Resource):
    @swag_from('./swagger_docs/report.yml')
    def get(self):
        request_format = request.args.get('request_format', type=str, default='json')
        request_order = request.args.get('request_order', type=str, default='asc')

        if request_order not in ['asc', 'desc'] or request_format not in ['json', 'xml']:
            abort(400, 'Invalid request_format or request_order value')

        drivers = Driver.select()
        drivers = drivers.order_by(Driver.result_time.asc())
        report_dict = {}

        if request_order == 'desc':
            drivers = drivers.order_by(Driver.result_time.desc())

        for driver in drivers:
            report_dict[driver.id] = {
                'name': driver.name,
                'team': driver.team,
                'time': driver.result_time
            }

        if request_format == 'xml':
            xml_report = dicttoxml(report_dict)
            return xml_report.decode()
        return report_dict


class GetDrivers(Resource):
    @swag_from('./swagger_docs/drivers.yml')
    def get(self):
        request_format = request.args.get('request_format', type=str, default='json')

        if request_format not in ['json', 'xml']:
            abort(400, 'Invalid request_format value')

        drivers = Driver.select()
        report_dict = {}

        for driver in drivers:
            report_dict[driver.id] = {
                'name': driver.name,
            }

        if request_format == 'xml':
            xml_report = dicttoxml(report_dict)
            return xml_report.decode()

        return report_dict


class GetDriverById(Resource):
    @swag_from('./swagger_docs/driver_by_id.yml')
    def get(self, driver_id):
        request_format = request.args.get('request_format', type=str, default='json')

        if request_format not in ['json', 'xml']:
            abort(400, 'Invalid request_format value')

        report_dict = {}
        try:
            driver = Driver.get(Driver.id == driver_id)
            report_dict[driver.id] = {
                'name': driver.name,
                'team': driver.team,
                'time': driver.result_time
            }
        except DoesNotExist:
            abort(404, f'Driver with id {driver_id} not found')

        if request_format == 'xml':
            xml_report = dicttoxml(report_dict)
            return xml_report.decode()

        return jsonify(report_dict)
