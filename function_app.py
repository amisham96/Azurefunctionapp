import azure.functions as func
import datetime
import json
import logging

from azure.identity import DefaultAzureCredential
app = func.FunctionApp()

@app.route(route="fa_adtest_frontend_trigger", auth_level=func.AuthLevel.FUNCTION)
def fa_adtest_frontend_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    credential = DefaultAzureCredential()
