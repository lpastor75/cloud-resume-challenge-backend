import os
import re
import json
from unittest import mock

from lambda_function import handler

with open('resources/resources.yml', 'r') as f:
    TABLENAME = re.search(r'TableName: (.*)?', f.read()).group(1)

@mock.patch.dict(os.environ, {"TABLENAME": TABLENAME})
def test_lambda_handler():
    # Check AWS creds
    assert "AWS_ACCESS_KEY_ID" in os.environ
    assert "AWS_SECRET_ACCESS_KEY" in os.environ

    ret = handler.lambda_handler("", "")

    # Assert return keys
    assert "statusCode" in ret
    assert "headers" in ret
    assert "body" in ret

    # Check for CORS in Headers
    assert "Access-Control-Allow-Origin"  in ret["headers"]

    # Check status code
    if ret["statusCode"] == 200:
        assert "visits" in ret["body"]
        assert ret["body"]["visits"].isnumeric()
    else:
        assert ret["body"]["visits"] == -1

    return