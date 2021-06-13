from fastapi import FastAPI, status, Response
from src.models.InputModel import *

# FastAPI Object to create all APIs
app = FastAPI()

@app.put("/sum", status_code=200)
def update_item(item: InputModel, response: Response):
    """
    POST request with API endpoint as  '/sum'
    :param response: To update the return status code
    :param item:
    :param InputModel
    :rtype dict
    :return {}

    Expectations: Expects the InputModel.values list to have 3 elements and all of them must be Integer
    """

    if len(item.values) != 3:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"status": status.HTTP_400_BAD_REQUEST, "error": "Exactly 3 numbers are required"}
    try:
        # Mapping values of lists from str to int
        values_mapped_to_int = list(map(int, item.values))

        # Filtering the values from the list which lies in the range [13, 14] and [17, 19]
        values_filtered = list(filter(lambda x: x not in VALUES_NOT_ALLOWED, values_mapped_to_int))

    except ValueError:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"status": status.HTTP_400_BAD_REQUEST, "error": "All inputs must be numeric"}

    return {"status": status.HTTP_200_OK, "result": sum(values_filtered)}
