from job import *


# route to get all movies
@app.route('/jobs', methods=['GET'])
def get_jobs():
    '''Function to get all the jobs in the database'''
    return jsonify(Job.get_all_jobs())


# route to get movie by id
@app.route('/jobs/<int:id>', methods=['GET'])
def get_job_by_id(id):
    return_value = Job.get_job(id)
    return jsonify(return_value)


# route to add new movie
@app.route('/jobs', methods=['POST'])
def add_job():
    '''Function to add new job to our database'''
    request_data = request.get_json()  # getting data from client
    Job.add_job(request_data["title"], request_data["company"],
                request_data["location"], request_data["salary"], request_data["summary"])
    response = Response("Job added", status=201, mimetype='application/json')
    return response


# route to update movie with PUT method
@app.route('/jobs/<int:id>', methods=['PUT'])
def update_job(id):
    '''Function to edit a job in our database using movie id'''
    request_data = request.get_json()
    Job.update_job(id, request_data["title"], request_data["company"],
                   request_data["location"], request_data["salary"], request_data["summary"])
    response = Response("Job Updated", status=201, mimetype='application/json')
    return response


# route to delete movie using the DELETE method
@app.route('/jobs/<int:id>', methods=['DELETE'])
def delete_job(id):
    '''Function to delete a job from our database'''
    Job.delete_job(id)
    response = Response("Job Deleted", status=204, mimetype='application/json')
    return response


if __name__ == "__main__":
    app.run(port=5000, debug=True)
