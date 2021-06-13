# REST API using Python (FastAPI)

## Project setup:

1) ### Clone the project:
                
        git  clone git@github.com:Blank000/FastRestApi.git
2) ### Installing the project dependencies:
   
   ##### NOTE: - `It's better to have a python virtual environment setup before installing the requirements`
   
         pip install -r requirements.txt

3) ### Running the server:

         cd src
   
         uvicorn main:app --reload

4) ### Debugging RestAPI endpoints:

         SwaggerUI: - http://127.0.0.1:8000/docs.
   
         ReDoc: - http://127.0.0.1:8000/redoc
    

### Endpoints available:
1) #### PUT Request -> "http://127.0.0.1:8000/sum": 
        
       a. Expected input from user- User must pass a json object in the header as below
            {"values": [x, y, z]}
   
       b. Constraints:
            Filter out the values lying in the range [13, 14] and [17, 19] inclusive
       
       c. Response:
           Case I:
                if list corresponding to key "values" has elements more or less than 3, 
                Expected response from the server:
   
                {"status": 400, "error": "Exactly 3 numbers are required"}
            
           Case II:
                If any one of x, y, z are not an integer value,
                Expected response from the server:
   
                {"status": 400, "error": "All inputs must be numeric"}
    
           Case III:
                When the list values has three elements and all are numbers,
                total_sum = Sum of numbers excluding from the range mentioned in the constraints
                Expected response from the server:
                
                {"status": 200, "sum": <total_sum>}

### Testing

1) `pytest` will already be installed from the `requirements.txt`. All test files and test functions must be named as `test_` as per standard pytest conventions


2) Get inside the project folder on terminal and execute `pytest`. This will run all the test cases ( will recursively search for `test_` files and function inside it and will execute and check)
