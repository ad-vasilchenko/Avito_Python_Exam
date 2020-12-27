import pytest
from pizza import *

def test_str():
	p = Margarita()
	s = str(p)
	assert str(p) == 'Margarita : tomatoes, cheese'