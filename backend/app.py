from flask import Flask, jsonify, abort, Response, request
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb://db/")
systems_table = client.assets.systems


def get_response(data: list) -> Response:
    if not data:
        abort(404, description="Invalid query, no items found!")
    resp = jsonify(data)
    # resp.headers["X-Content-Type-Options"] = "nosniff"
    return resp


@app.route("/api")
def all_results() -> Response:
    data = list(systems_table.find({}, {"_id": False}))
    resp = get_response(data)
    return resp


@app.route("/api/os/<os>")
def os_results(os: str) -> Response:
    data = list(systems_table.find({"os": os}, {"_id": False}))
    resp = get_response(data)
    return resp


@app.route("/api/domain/<domain>")
def domain_results(domain: str) -> Response:
    data = list(systems_table.find({"domain": domain}, {"_id": False}))
    resp = get_response(data)
    return resp


@app.route("/api/workgroup/<workgroup>")
def workgroup_results(workgroup: str) -> Response:
    data = list(systems_table.find({"workgroup": workgroup}, {"_id": False}))
    resp = get_response(data)
    return resp

@app.route("/api/dcol", methods = ["POST"])
def dcol_trigger() -> Response:
    # collector = dcol(request.form["ip"])
    status = True
    # try:
    #     collector.run()
    # except Exception as err:
    #     print(err)
    #     status = False
    # finally:
    #     collector.close()
    return jsonify({"success": status})


@app.route("/api/search", methods=["GET", "POST"])
def search() -> Response:
    if request.method == "GET":
        data = list(systems_table.find({request.args.get("category"): request.args.get("query")}, {"_id": False}))
    else:
        data = list(systems_table.find({request.form["category"]: request.form["query"]}, {"_id": False}))
    resp = get_response(data)
    return resp


@app.errorhandler(404)
def error_404(err: Exception):
    return jsonify(error=str(err)), 404
