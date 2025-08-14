import uuid
from splice_lib import random_number

def test_random_number():
    assert type(random_number()) == uuid.UUID
