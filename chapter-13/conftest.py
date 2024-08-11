import random
import string

import pytest


@pytest.fixture
def random_token() -> str:
    """Generate radom token"""
    token_1 = []
    char_pool = string.ascii_lowercase + string.digits
    for _ in range(32):
        token_1.append(random.choice(char_pool))
    return "".join(token_1)
