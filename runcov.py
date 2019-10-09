#!/usr/bin/env python
import coverage

from runtests import run_tests

def run_cov():

    # Set coverage to starwarsdemo app
    cov = coverage.Coverage(source=['starwarsdemo/apps', 'starwarsdemo/tests'])
    cov.start()

    # Run tests
    failures = run_tests(verbosity=1, interactive=False, failfast=True)

    cov.stop()
    cov.save()

    # Show report only when have not failures
    if not bool(failures):
        # Show report on terminal
        cov.report()
        # Save html report on htmlcov folder
        cov.html_report(directory='htmlcov')

if __name__ == '__main__':
    run_cov()
