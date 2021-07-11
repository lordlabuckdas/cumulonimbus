from flask import Flask, jsonify, abort, Response, request
from flask_cors import CORS
from pymongo import MongoClient, DESCENDING, ASCENDING

# from dcol import DCol

app = Flask(__name__)
CORS(app, origins=["http://localhost:3000", "http://127.0.0.1:3000"])
client = MongoClient("mongodb://db/")
systems_table = client.assets.systems
MAX_RESULTS_PER_PAGE = 5


def get_paginated_data(data: list, page_num: int) -> list:
    if not data:
        return data
    if page_num * MAX_RESULTS_PER_PAGE <= len(data):
        data = data[(page_num - 1) * MAX_RESULTS_PER_PAGE : page_num * MAX_RESULTS_PER_PAGE]
    elif page_num * MAX_RESULTS_PER_PAGE > len(data) and (page_num - 1) * MAX_RESULTS_PER_PAGE <= len(data):
        data = data[(page_num - 1) * MAX_RESULTS_PER_PAGE : len(data)]
    else:
        abort(404, description="No more results to show")
    return data


def get_response(data: list) -> Response:
    if not data:
        abort(404, description="No items found!")
    resp = jsonify(data)
    # resp.headers["X-Content-Type-Options"] = "nosniff"
    return resp


@app.route("/api", methods=["GET"])
def all_results() -> Response:
    sort_key = request.args.get("sort") if request.args.get("sort") else "last_seen"
    sort_order = ASCENDING if request.args.get("asc") == "1" else DESCENDING
    page_num = int(request.args.get("page", "1"))
    data = list(systems_table.find({}, {"_id": False}, sort=[(sort_key, sort_order)]))
    data = get_paginated_data(data, page_num)
    resp = get_response(data)
    return resp


@app.route("/api/search", methods=["GET"])
def search() -> Response:
    categories = (
        [request.args.get("category")]
        if request.args.get("category")
        else ["mac_address", "os", "domain", "workgroup", "ip_address", "hostname"]
    )
    query = request.args.get("query")
    sort_key = request.args.get("sort") if request.args.get("sort") else "last_seen"
    sort_order = ASCENDING if request.args.get("asc") == "1" else DESCENDING
    page_num = int(request.args.get("page", "1"))
    if not query:
        abort(404, description="No query passed")
    data = []
    for category in categories:
        data = list(systems_table.find({category: query}, {"_id": False}, sort=[(sort_key, sort_order)]))
        if data:
            break
    data = get_paginated_data(data, page_num)
    resp = get_response(data)
    return resp


# @app.route("/api/dcol", methods=["POST"])
# def dcol_trigger() -> Response:
#     collector = DCol(request.form["ip"])
#     status = True
#     try:
#         collector.run()
#     except Exception as err:
#         print(err)
#         status = False
#     finally:
#         collector.close()
#     return jsonify({"success": status})


@app.errorhandler(404)
def error_404(err: Exception):
    return jsonify(error=str(err)), 404
