import json
import logging

import azure.functions as func
from azure.storage.blob import BlobClient, BlobServiceClient, ContainerClient
from azure.storage.queue import QueueClient, QueueServiceClient

app = func.FunctionApp()

@app.route(route="http_trigger", auth_level=func.AuthLevel.ANONYMOUS)
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # Extract the input data from the request body
    try:
        input_data = req.get_json()  # Get JSON body from the request
    except ValueError:
        return func.HttpResponse(
            "Invalid JSON format.",
            status_code=400
        )
    
    # Initialize the response_values list
    response_values = []

    # Process each record in the input data
    if "values" in input_data:
        for record in input_data["values"]:
            record_id = record.get("recordId")

            # Append the modified record to response_values
            response_values.append({
                "recordId": record_id,
                "data": {
                    "layout_intelligence_data": {
                        "$type": "file",
                        "url": "https://microsoft-my.sharepoint.com/:x:/p/v-jgs/EQI41ZvJ1VBBsI_j0n7DG6EBvEWcJer1vPvjlsdUxzTgFw?e=jah1Zl"  # Replace "url1" with your actual URL or dynamic value
                    }
                }
            })

        # Create the final response as JSON
        return func.HttpResponse(
            json.dumps({"values": response_values}),  # Return as JSON
            status_code=200,
            mimetype="application/json"  # Specify that the response is in JSON format
        )
    else:
        return func.HttpResponse(
            json.dumps({"error": "Request body does not contain 'values'."}),
            status_code=400,
            mimetype="application/json"
        )
