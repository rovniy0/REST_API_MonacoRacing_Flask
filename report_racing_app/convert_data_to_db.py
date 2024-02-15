
from models import Driver
from report_racing_app.report import build_report


result_abbreviations, result_time_dict = build_report('data_files')


for driver_id, description in result_abbreviations.items():
    parts = description.split(" | ")
    driver = Driver.create(
        id=driver_id,
        name=parts[0],
        team=parts[1],
        result_time=result_time_dict[driver_id]
    )
