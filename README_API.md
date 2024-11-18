Startup the server
1. Run the below command in your root directory that contains src
    uvicorn src.pythonNewsAPI.main:app --reload

2. Change the address to your own device address in below file, for testing
    tests/pythonNewsAPI/test_newsAPI.py
    
3. Run the below command in your root directory that contains src
    pytest tests/pythonNewsAPI/test_newsAPI.py -p no:warnings