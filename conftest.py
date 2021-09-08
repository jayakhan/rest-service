from main import get_research_materials
import pytest

@pytest.fixture
def app():
    app = get_research_materials()
    return app