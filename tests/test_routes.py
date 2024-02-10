
import pytest


def test_get_report_format_json(client):
    response = client.get('/api/v1/report/')
    assert response.status_code == 200
    assert (b'{"BHS":{"name":"Brendon Hartley | SCUDERIA TORO ROSSO HONDA","time":"0:01:13'
            b'.179000"}') in response.data


def test_get_report_format_xml(client):
    response = client.get('/api/v1/report/?format=xml')
    assert response.status_code == 200
    assert (b'"<?xml version=\\"1.0\\" encoding=\\"UTF-8\\" ?><root><SVF type=\\"dict\\"'
            b'><name type=\\"str\\">Sebastian Vettel | FERRARI</name><time type=\\"str\\">'
            b'0:01:04.415000</time></SVF>') in response.data


def test_get_drivers_format_json(client):
    response = client.get('/api/v1/report/drivers/')
    assert response.status_code == 200
    assert b'{"BHS":"Brendon Hartley | SCUDERIA TORO ROSSO HONDA"' in response.data


def test_get_drivers_format_xml(client):
    response = client.get('/api/v1/report/drivers/?format=xml')
    assert response.status_code == 200
    assert (b'<BHS type=\\"str\\">Brendon Har'
            b'tley | SCUDERIA TORO ROSSO HONDA</BHS>') in response.data


def test_get_driver_by_id_format_json(client):
    response = client.get('/api/v1/report/drivers/DRR')
    assert response.status_code == 200
    assert (b'{"DRR": {"name": "Daniel Ricciardo | RED BULL RACING TAG HEUER",'
            b' "time": "0:02:47.987000"}}\n') in response.data


def test_get_driver_by_id_format_xml(client):
    response = client.get('/api/v1/report/drivers/DRR?format=xml')
    assert response.status_code == 200
    assert (b'"<?xml version=\\"1.0\\" encoding=\\"UTF-8\\" ?><root><DRR type=\\"dict\\"'
            b'><name type=\\"str\\">Daniel Ricciardo | RED BULL RACING TAG HEUER</name><'
            b'time type=\\"str\\">0:02:47.987000</time></DRR></root>"\n') in response.data


def test_swagger_status_code(client):
    response = client.get('/apidocs/')
    assert response.status_code == 200


if __name__ == '__main__':
    pytest.main()
