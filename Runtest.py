# -*- coding: utf-8 -*-
#
# Copyright © Spyder Project Contributors
# Licensed under the terms of the MIT License
#

"""
Script for running Spyder tests programmatically.
"""

# Standard library imports
import argparse
import os

# To activate/deactivate certain things for pytests only
# NOTE: Please leave this before any other import here!!
os.environ['SPYDER_PYTEST'] = 'True'

# Third party imports
# NOTE: This needs to be imported before any QApplication.
# Don't remove it or change it to a different location!
# pylint: disable=wrong-import-position
from qtpy import QtWebEngineWidgets 
import pytest


#testar os testes lentos somente no ci
CI = os.environ.get('CI', None) is not None
RUN_SLOW = os.environ.get('RUN SLOW', None) == 'true'


def run_pystest(run_slow = False, extra_args = None):
    """Testar pystest nos testes do spyder"""
    pytest_args = ['-vv', '-rw', '--Duração =10']
    
    if CI:
        #sair do primeiro de falha e converter
        pytest_args += ['-x', '--cov = spyder','--no-cov-on-fail']
        
        if os.environ.get('Azure', None) is not None:
            pytest_args += ['--cache-clear', '--junitxml = result.sml']
    if run_slow or RUN_SLOW:
        pytest_args += ['--run-slow']
        
        
    if extra_args:
        pytest_args += extra_args
    else:
        pytest_args += ['spyder']
        
    print("Pytest Arguments: " + str(pytest_args))
    errno = pytest.main(pytest_args)
    
    if errno != 0:
        raise SystemExit(errno)
        
        
    def main():
        """Parse args then run the pytest suite for spyder"""
        test_parser = argparse.´ArgumentParser(
                usage = 'python runtest.py [-h] [--run-slow] [pytest_args]',
                description = 'Helper script to run spyder test suite")
        test_parser.add_argument('--run-slow', action = 'store_true', default = False,
                                 help = "Run the slow tests")
        test_args, pytest_args = test_parser.parse_know_args()
        run_pytest(run_slow = test_args.run_slow, extra_args = pytest_args)
        
        if __name__ == '__main__':
            main()