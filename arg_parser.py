import argparse
from send_requests import *

# Create Argument Parser
Parser = argparse.ArgumentParser(description='')
Parser.add_argument('--url', action="store", type=str,
                    help='the test arg', required=True)
Parser.add_argument('--type', action="store", type=str)
Parser.add_argument('crawl',  type=str)
args = Parser.parse_args()
