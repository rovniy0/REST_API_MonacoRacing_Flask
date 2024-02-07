
import pytest
from bs4 import BeautifulSoup


def test_report_content(client):
    response = client.get('/report/')
    soup = BeautifulSoup(response.data, 'html.parser')
    h1 = soup.find('h1')
    assert h1.text == 'Report of Monaco Racing'
    ul = soup.find('ul')
    assert ul is not None


def test_report_content_with_order(client):
    response = client.get('/report/?order=desc')
    soup = BeautifulSoup(response.data, 'html.parser')
    h1 = soup.find('h1')
    assert h1.text == 'Report of Monaco Racing'
    ul = soup.find('ul')
    assert ul is not None


def test_report_all_drivers_content(client):
    response = client.get('/report/drivers/')
    soup = BeautifulSoup(response.data, 'html.parser')
    h1 = soup.find('h1')
    assert h1.text == 'Report of Monaco Racing'
    ul = soup.find('ul')
    assert ul is not None


def test_report_driver_id_content(client):
    response = client.get('/report/drivers/?driver_id=DRR')
    soup = BeautifulSoup(response.data, 'html.parser')
    h1 = soup.find('h1')
    assert h1.text == 'Report of Monaco Racing'
    ul = soup.find('ul')
    assert ul is not None


def test_report_status_code(client):
    response = client.get('/report/?order=desc')
    assert response.status_code == 200


def test_report_all_drivers_status_code(client):
    response = client.get('/report/drivers/')
    assert response.status_code == 200


def test_report_driver_id_status_code(client):
    response = client.get('/report/drivers/?driver_id=DRR')
    assert response.status_code == 200


if __name__ == '__main__':
    pytest.main()
