# Tests (test_myapp.py)

from myapp import app


def test_hello():
    response = app.test_client().get("/")

    assert response.status_code == 200
    assert response.data == b"Hello World!"


def test_ci_demo_intentional_assertion_failure():
    """Deterministic assertion failure used to verify CI diagnosis."""
    assert 2 + 2 == 5
