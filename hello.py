import json

from src.randomstring import *

import azure.functions as func

from motivate.motivate import quote


def quote(req) -> str:
    q, a = quote()

    return json.dumps({
        "status_code": 200,
        "headers" : {
            "Content-Type": "application/json"
        },
        "body": {
            "quote": q,
            "author": a
        }

    })

