
from flask import Flask, request, jsonify
from flask_restful import Resource
from report_racing_app import build_report
from flasgger import swag_from
from dicttoxml import dicttoxml
from collections import OrderedDict


app = Flask(__name__)


class GetReport(Resource):
    def get(self):
        request_format = request.args.get('format', type=str)
        request_order = request.args.get('order', type=str)
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
    def get(self):
        request_format = request.args.get('format', type=str)
        result_abbreviations, sorted_time_result = build_report('data_files')
        if request_format == 'xml':
            xml_report = dicttoxml(result_abbreviations)
            return xml_report.decode()
        return jsonify(result_abbreviations)


class GetDriverById(Resource):
    def get(self, driver_id):
        request_format = request.args.get('format', type=str)
        result_abbreviations, sorted_time_result = build_report('data_files')
        report_dict = {}
        if driver_id in result_abbreviations:
            time_str = str(sorted_time_result[driver_id])
            report_dict[driver_id] = {
                "name": result_abbreviations[driver_id],
                "time": time_str
            }
        if request_format == 'xml':
            xml_report = dicttoxml(report_dict)
            return xml_report.decode()
        return report_dict
