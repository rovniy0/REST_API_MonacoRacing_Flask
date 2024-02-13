
from flasgger import Swagger
from flask import Flask
from flask_restful import Api
from report_racing_app.api.report_api import GetReport, GetDrivers, GetDriverById

app = Flask(__name__)
api = Api(app)
swagger = Swagger(app)

api.add_resource(GetReport, '/api/v1/report/')
api.add_resource(GetDrivers, '/api/v1/report/drivers/')
api.add_resource(GetDriverById, '/api/v1/report/drivers/<string:driver_id>')

if __name__ == '__main__':
    app.run(debug=False)
