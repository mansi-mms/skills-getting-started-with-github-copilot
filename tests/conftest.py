import copy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app

BASELINE_ACTIVITIES = copy.deepcopy(activities)


@pytest.fixture(autouse=True)
def reset_activities_state():
    """Reset shared in-memory activities before every test."""
    activities.clear()
    activities.update(copy.deepcopy(BASELINE_ACTIVITIES))
    yield


@pytest.fixture
def client():
    return TestClient(app)
