import json
import os
from google.cloud import firestore

# Initialize Firestore client
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "firebay-6554f-54d04c3b13d2.json"
db = firestore.Client()

def lambda_handler(event, context):
    # Define the document path (update this as per your Firestore structure)
    doc_ref = db.collection("tests").document("person")

    # Get current count and increment it
    doc = doc_ref.get()
    if doc.exists:
        current_count = doc.to_dict().get("num", 0)
    else:
        current_count = 0

    # Update the count
    new_count = current_count + 1
    doc_ref.update({"num": new_count})

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Count updated successfully",
            "new_count": new_count
        })
    }
