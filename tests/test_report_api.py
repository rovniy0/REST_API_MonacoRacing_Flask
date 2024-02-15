
import pytest


class TestGetReportApiCases:

    def test_get_report_incorrect_arguments(self, client, db):
        response = client.get('/api/v1/report/?request_order=some_value')
        assert response.status_code == 400
        response = client.get('/api/v1/report/?request_format=some_value')
        assert response.status_code == 400
        response = client.get('/api/v1/report/?request_format=some_value&request_order=some_value')
        assert response.status_code == 400

    def test_get_report_format_json(self, client, db):
        response = client.get('/api/v1/report/')
        assert response.status_code == 200
        assert (b'{"SVF":{"name":"Sebastian Vettel",'
                b'"team":"FERRARI","time":"0:01:04.415000"}}') in response.data

    def test_get_report_order_desc(self, client, db):
        response = client.get('/api/v1/report/?request_order=desc')
        assert response.status_code == 200
        assert (b'{"SVF":{"name":"Sebastian Vettel",'
                b'"team":"FERRARI","time":"0:01:04.415000"}}') in response.data

    def test_get_report_format_xml(self, client, db):
        response = client.get('/api/v1/report/?request_format=xml')
        assert response.status_code == 200
        assert (b'"<?xml version=\\"1.0\\" encoding=\\"UTF-8\\" ?><root><SVF type=\\"dict\\"'
                b'><name type=\\"str\\">Sebastian Vettel</name><team type=\\"str\\">FERRARI</t'
                b'eam><time type=\\"str\\">0:01:04.415000</time></SVF></root>"\n') in response.data


class TestGetDriversApiCases:

    def test_get_drivers_incorrect_arguments(self, client, db):
        response = client.get('/api/v1/report/?request_format=some_value')
        assert response.status_code == 400

    def test_get_drivers_format_json(self, client, db):
        response = client.get('/api/v1/report/drivers/')
        assert response.status_code == 200
        assert b'{"SVF": {"name": "Sebastian Vettel"}}\n' in response.data

    def test_get_drivers_format_xml(self, client, db):
        response = client.get('/api/v1/report/drivers/?request_format=xml')
        assert response.status_code == 200
        assert (b'"<?xml version=\\"1.0\\" encoding=\\"UTF-8\\" ?><root><SVF type=\\"dict\\"'
                b'><name type=\\"str\\">Sebastian Vettel</name></SVF></root>"\n') in response.data


class TestGetDriverByIdApiCases:

    def test_get_drivers_incorrect_arguments(self, client, db):
        response = client.get('/api/v1/report/drivers/?request_format=some_value')
        assert response.status_code == 400
        response = client.get('/api/v1/report/drivers/AAA')
        assert response.status_code == 404

    def test_get_driver_by_id_format_json(self, client, db):
        response = client.get('/api/v1/report/drivers/SVF')
        assert response.status_code == 200
        assert (b'{"SVF":{"name":"Sebastian Vettel",'
                b'"team":"FERRARI","time":"0:01:04.415000"}}\n') in response.data

    def test_get_driver_by_id_format_xml(self, client, db):
        response = client.get('/api/v1/report/drivers/SVF?request_format=xml')
        assert response.status_code == 200
        assert (b'"<?xml version=\\"1.0\\" encoding=\\"UTF-8\\" ?><root><SVF type=\\"dict\\"'
                b'><name type=\\"str\\">Sebastian Vettel</name><team type=\\"str\\">FERRARI</t'
                b'eam><time type=\\"str\\">0:01:04.415000</time></SVF></root>"\n') in response.data


def test_swagger_status_code(client):
    response = client.get('/apidocs/')
    assert response.status_code == 200


if __name__ == '__main__':
    pytest.main()
