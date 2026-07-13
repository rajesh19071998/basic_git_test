import pytest

def pytest_configure(config):
    config._metadata['Project'] = 'HTTP Test'
    config._metadata['Environment'] = 'Jenkins CI'

def pytest_html_report_title(report):
    report.title = "Pytest HTTP Report"

def pytest_html_results_table_row(report, cells):
    if report.passed:
        cells.insert(1, "✅ PASSED")
    elif report.failed:
        cells.insert(1, "❌ FAILED")

def pytest_html_results_table_html(report, data):
    if hasattr(report, 'extra'):
        data.extend(report.extra)

@pytest.fixture
def extra(request):
    request.node.extra = []
    return request.node.extra
