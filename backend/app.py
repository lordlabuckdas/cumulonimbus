from flask import Flask, jsonify, abort, Response, request
from pymongo import MongoClient

from dcol import DCol

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


@app.route("/api/search", methods=["GET", "POST"])
def search() -> Response:
    categories = ["mac_address", "os", "domain", "workgroup", "ip_address", "hostname"]
    data = []
    if request.method == "GET":
        if request.args.get("category"):
            categories = [request.args.get("category")]
        query = request.args.get("query")
    else:
        if request.form["category"]:
            categories = [request.form["category"]]
        query = request.form["query"]
    for category in categories:
        data = list(systems_table.find({category: query}, {"_id": False}))
        if data:
            break
    resp = get_response(data)
    return resp


@app.route("/api/dcol", methods=["POST"])
def dcol_trigger() -> Response:
    collector = DCol(request.form["ip"])
    status = True
    try:
        collector.run()
    except Exception as err:
        print(err)
        status = False
    finally:
        collector.close()
    return jsonify({"success": status})


@app.errorhandler(404)
def error_404(err: Exception):
    return jsonify(error=str(err)), 404
