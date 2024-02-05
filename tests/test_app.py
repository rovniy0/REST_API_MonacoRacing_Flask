
import pytest


def test_report_status_code(client):
    response = client.get('/report/?order=desc')
    assert response.status_code == 200


def test_report_all_drivers_status_code(client):
    response = client.get('/report/drivers/')
    assert response.status_code == 200


def test_report_drivers_status_code(client):
    response = client.get('/report/drivers/?driver_id=DRR')
    assert response.status_code == 200


if __name__ == '__main__':
    pytest.main()
