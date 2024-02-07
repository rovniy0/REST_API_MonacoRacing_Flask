
from flask import Flask, render_template, url_for, request
from report_racing_app import print_report

app = Flask(__name__)


@app.route("/report/")
def report():
    order = request.args.get('order')
    common_statistics = print_report('data_files', order=order,)
    return render_template('report.html', report=common_statistics)


@app.route("/report/drivers/")
def report_drivers():
    driver_id = request.args.get('driver_id')
    if driver_id is None:
        drivers_statistic = print_report('data_files', driver="full")
        return render_template('report.html', drivers_report=drivers_statistic)
    else:
        driver_statistic = print_report('data_files', driver=driver_id)
        return render_template('report.html', report=driver_statistic)


if __name__ == '__main__':
    app.run(debug=True)
