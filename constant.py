vt_api_key = "3a8a05aba7e59f4efb12071bc2afea794438d0e324f5cd3c4d01917b86e6a551"

vt_headers = {
    "Accept": "application/json",
    "x-apikey": vt_api_key
}


def make_response(state, message):
    return {"state": state, "message": message}
