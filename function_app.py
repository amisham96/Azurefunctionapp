import azure.functions as func
import logging
from azure.identity import DefaultAzureCredential
import json

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="fa_adtest_frontend_trigger")
def fa_adtest_frontend_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    # When this import is removed, deployment works fine
    credential = DefaultAzureCredential()
    # Rest of the function code
