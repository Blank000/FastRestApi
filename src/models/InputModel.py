from typing import Optional
from pydantic import BaseModel

"""
Combined range of the numbers not allowed is [13, 14] & [16, 19]
"""
VALUES_NOT_ALLOWED = [13, 14, 17, 18, 19]

class InputModel(BaseModel):
    """
    values is a expected list of numbers. It's an empty list by default
    """
    values = []
