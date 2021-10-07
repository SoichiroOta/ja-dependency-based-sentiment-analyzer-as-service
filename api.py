import json
import os
from typing import Any

import responder
from analysis import Analyzer

env = os.environ
DEBUG = env["DEBUG"] in ["1", "True", "true"]


api = responder.API(debug=DEBUG)
analyzer = Analyzer()


@api.route("/")
async def analyze(req: Any, resp: Any) -> None:
    body = await req.text
    texts = json.loads(body)
    parsed_list = [analyzer.analyze(text) for text in texts]
    resp.media = dict(data=parsed_list)


if __name__ == "__main__":
    api.run()
