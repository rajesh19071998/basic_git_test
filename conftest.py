import pytest

@pytest.fixture
def extra(request):
    # Provide a list to collect extras per test
    request.node.extra = []
    return request.node.extra

def pytest_html_results_table_extra(report, extra):
    if hasattr(report, 'extra'):
        extra.extend(report.extra)
