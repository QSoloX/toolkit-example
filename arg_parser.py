import argparse
from send_requests import *

# Create Argument Parser
Parser = argparse.ArgumentParser(description='')
Parser.add_argument('--url', action="store", type=str,
                    help='input the url you want to run a scan/attack on.', required=True)
Parser.add_argument('--type', action="store", type=str, default="get",
                    help='The type of Http Request you would like to send. (get, post, del)')
Parser.add_argument('--output', action="store", type=str,
                    help='set a output filename to write all the found links too.')
Parser.add_argument('-crawl',  type=int, default=0,
                    help="Usage: -crawl int (1 and 2 are currently supported commands.)")
args = Parser.parse_args()
