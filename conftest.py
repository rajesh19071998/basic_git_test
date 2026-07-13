import pytest
from py.xml import html

def pytest_configure(config):
    config._metadata['Project'] = 'HTTP Test'
    config._metadata['Environment'] = 'Jenkins CI'

def pytest_html_report_title(report):
    report.title = "Pytest HTTP Report"

def pytest_html_results_table_row(report, cells):
    if report.passed:
        cells.insert(1, html.td('✅ PASSED', class_='passed'))
    elif report.failed:
        cells.insert(1, html.td('❌ FAILED', class_='failed'))

def pytest_html_results_table_html(report, data):
    # Attach extras (like logs or response bodies) if present
    if hasattr(report, 'extra'):
        data.extend(report.extra)

@pytest.fixture
def extra(request):
    request.node.extra = []
    return request.node.extra
