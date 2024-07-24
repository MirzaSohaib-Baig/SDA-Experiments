from flask import Flask
from flask_restful import Api, Resource, reqparse, abort


app = Flask( __name__ )
api = Api(app)

std_put = reqparse.RequestParser()
std_put.add_argument("Name", type=str, location='args')
std_put.add_argument("Rollno", type=str, location='args')

data = {
    1 : {"Name": "Sohaib", "Rollno": "20B-041-SE"}, 
    2 : {"Name": "Haris", "Rollno": "20B-100-SE"}, 
    3 : {"Name": "Rimmel", "Rollno": "20B-005-SE"},
    4 : {"Name": "Zaid", "Rollno": "20B-051-SE"}
}

def notFound(std_id):
    if std_id not in data:
        abort(404, message="Student id not Found")

class std(Resource):
    
    def get(self, std_id):
        notFound(std_id)
        return data[std_id]
    
    def put(self, std_id):
        newstd = std_put.parse_args()
        data[std_id] = newstd
        return data[std_id]
        
    def delete(self,std_id):
        del data[std_id]
        return '', 204
    
    def post(self, std_id):
        newstd = std_put.parse_args()
        data[std_id] = newstd
        return data[std_id]
    
api.add_resource(std, "/show/<int:std_id>")

if __name__ == "__main__":
    app.run(debug=True)