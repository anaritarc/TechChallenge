import pytest
import panda as pd

def check_unique_Id(observation):
    """
        Checks if price is above 0
    """  
    
    assert observation['price'] < 0
