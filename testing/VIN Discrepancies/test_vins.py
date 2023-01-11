import pytest
from vins import fetch_vins_from_db

@pytest.fixture
def vins():
    return set(fetch_vins_from_db())

@pytest.fixture
def file_vins():
    with open("vins.txt") as file: 
        data = file.readlines() 
    return set(data)

def test_vin_discrepancies(vins, file_vins):
    """Check for discrepancies in VINs between vins.txt and the database"""
    
    diff_vins = vins.difference(file_vins)
    diff_file_vins = file_vins.difference(vins)
    
    try:
        assert diff_vins == diff_file_vins
    
    except AssertionError:
        print("Missing vins")
        if diff_vins:
            print("extra vins fetched from database: \n", diff_vins)
        if diff_file_vins:
            print("Missing vins from database: \n", diff_file_vins)
    
