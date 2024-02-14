
from flask import Flask, request, jsonify, abort
from flask_restful import Resource
from report_racing_app import build_report
from flasgger import swag_from
from dicttoxml import dicttoxml
from collections import OrderedDict


app = Flask(__name__)


class GetReport(Resource):
    @swag_from('./swagger_docs/report.yml')
    def get(self):
        request_format = request.args.get('request_format', type=str, default='json')
        request_order = request.args.get('request_order', type=str, default='asc')

        if request_order not in ['asc', 'desc'] or request_format not in ['json', 'xml']:
            abort(400, 'Invalid request_format or request_order value')

        result_abbreviations, sorted_time_result = build_report('data_files')
        report_dict = {}

        if request_order == 'desc':
            sorted_time_result = OrderedDict(reversed(sorted_time_result.items()))

        for driver_id in sorted_time_result:
            time_str = str(sorted_time_result[driver_id])
            report_dict[driver_id] = {
                "name": result_abbreviations[driver_id],
                "time": time_str
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

        result_abbreviations, sorted_time_result = build_report('data_files')

        if request_format == 'xml':
            xml_report = dicttoxml(result_abbreviations)
            return xml_report.decode()

        return jsonify(result_abbreviations)


class GetDriverById(Resource):
    @swag_from('./swagger_docs/driver_by_id.yml')
    def get(self, driver_id):
        request_format = request.args.get('request_format', type=str, default='json')

        if request_format not in ['json', 'xml']:
            abort(400, 'Invalid request_format value')

        result_abbreviations, sorted_time_result = build_report('data_files')
        report_dict = {}

        if driver_id in result_abbreviations:
            time_str = str(sorted_time_result[driver_id])
            report_dict[driver_id] = {
                "name": result_abbreviations[driver_id],
                "time": time_str
            }
        else:
            abort(400, f'Driver with id {driver_id} not found')

        if request_format == 'xml':
            xml_report = dicttoxml(report_dict)
            return xml_report.decode()

        return jsonify(report_dict)
