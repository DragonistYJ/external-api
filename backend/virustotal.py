import base64

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


@vt.route("/ip", methods=["get"])
def ip_endpoint():
    if not request.args["ip"]:
        return make_response("error", "Miss key arg ip")
    url = "https://www.virustotal.com/api/v3/ip_addresses/" + request.args["ip"]
    response = requests.request("GET", url, headers=vt_headers)
    result = response.json()
    if "error" in result:
        return make_response("error", "VT server error, please try again")
    else:
        ip = result["data"]["attributes"]
        ip["_id"] = result["data"]["id"]
        ip_collection = vt_database["ip"]
        exist_ip = ip_collection.find_one({"_id": ip["_id"]})
        if exist_ip is None:
            ip_collection.insert_one(ip)
            return make_response("success", "success query ip=" + ip["_id"])
        else:
            ip_collection.replace_one({"_id": ip["_id"]}, ip)
            return make_response("success", "success update ip=" + ip["_id"])


@vt.route("/url", methods=["get"])
def url_endpoint():
    if not request.args["url"]:
        return make_response("error", "Miss key arg url")
    url = "https://www.virustotal.com/api/v3/urls/" + request.args["url"]
    response = requests.request("GET", url, headers=vt_headers)
    result = response.json()
    if "error" in result:
        return make_response("error", "VT server error, please try again")
    else:
        url = result["data"]["attributes"]
        url["_id"] = result["data"]["id"]
        url_collection = vt_database["url"]
        exist_url = url_collection.find_one({"_id": url["_id"]})
        if exist_url is None:
            url_collection.insert_one(url)
            return make_response("success", "success query url=" + url["_id"])
        else:
            url_collection.replace_one({"_id": url["_id"]}, url)
            return make_response("success", "success update url=" + url["_id"])


@vt.route("/file_report", methods=["get"])
def file_report_endpoint():
    if not request.args["file"]:
        return make_response("error", "Miss key arg file")
    url = "https://www.virustotal.com/api/v3/files/" + request.args["file"]
    response = requests.request("GET", url, headers=vt_headers)
    result = response.json()
    if "error" in result:
        return make_response("error", "VT server error, please try again")
    else:
        file_report = result["data"]["attributes"]
        file_report["_id"] = result["data"]["id"]
        file_report_collection = vt_database["file_report"]
        exist_file_report = file_report_collection.find_one({"_id": file_report["_id"]})
        if exist_file_report is None:
            file_report_collection.insert_one(url)
            return make_response("success", "success query url=" + file_report["_id"])
        else:
            file_report_collection.replace_one({"_id": file_report["_id"]}, file_report)
            return make_response("success", "success update url=" + file_report["_id"])
