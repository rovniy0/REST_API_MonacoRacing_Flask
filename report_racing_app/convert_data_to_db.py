
from models import Driver
from report_racing_app.report import build_report
from os import environ

DATA_FILES = environ.get('DATA_FILES')

result_abbreviations, result_time_dict = build_report(DATA_FILES)

for driver_id, description in result_abbreviations.items():
    parts = description.split(" | ")
    driver = Driver.create(
        id=driver_id,
        name=parts[0],
        team=parts[1],
        result_time=result_time_dict[driver_id]
    )
