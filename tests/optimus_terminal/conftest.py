import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

def pytest_generate_tests():
    os.environ['COHERE_API_KEY'] = "pbMSOmk98DtRQtbVqc9NB2XYUn1KzNgpc4GDsHCv" # Fill the string with the COHERE_API_KEY: pbMSOmk98DtRQtbVqc9NB2XYUn1KzNgpc4GDsHCv