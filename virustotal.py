import pymongo
import requests
from flask import Blueprint, request

from constant import make_response, vt_headers

vt = Blueprint('vt', __name__, url_prefix='/vt')
mongo_client = pymongo.MongoClient("mongodb://192.168.50.17:27017/")
vt_database = mongo_client["virustotal"]


@vt.route("/domain", methods=["get"])
def domain_endpoint():
    if not request.args["domain"]:
        return make_response("error", "Miss key arg domain")
    url = "https://www.virustotal.com/api/v3/domains/" + request.args["domain"]
    response = requests.request("GET", url, headers=vt_headers)
    result = response.json()
    if "error" in result:
        return make_response("error", "VT server error, please try again")
    else:
        domain = result["data"]["attributes"]
        domain["_id"] = result["data"]["id"]
        domain_collection = vt_database["domain"]
        exist_domain = domain_collection.find_one({"_id": domain["_id"]})
        if exist_domain is None:
            domain_collection.insert_one(domain)
            return make_response("success", "success query domain=" + domain["_id"])
        else:
            domain_collection.replace_one({"_id": domain["_id"]}, domain)
            return make_response("success", "success update domain=" + domain["_id"])
