import pytest

def pytest_html_report_title(report):
    report.title = "Pytest HTTP Report"

def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend([pytest_html.extras.text("Project: HTTP Test")])
    prefix.extend([pytest_html.extras.text("Environment: Jenkins CI")])

def pytest_html_results_table_html(report, data):
    if hasattr(report, 'extra'):
        data.extend(report.extra)

@pytest.fixture
def extra(request):
    request.node.extra = []
    return request.node.extra
