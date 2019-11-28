import argparse
from send_requests import *

# Create Argument Parser
Parser = argparse.ArgumentParser(description='')
Parser.add_argument('--url', action="store", type=str,
                    help='input the url you want to run a scan/attack on.', required=True)
Parser.add_argument('--type', action="store", type=str, default="get",
                    help='The type of Http Request you would like to send. (get, post, del)')
Parser.add_argument('--list', action="store", type=str,  default="url_list.aawt",
                    help="Path to your list to test the site against")
Parser.add_argument('--output', action="store", type=str,
                    help='set a output filename to write all the found links too.')
Parser.add_argument('-crawl', type=int,  default=0,
                    help="The Severity of the crawl (1-2)")
args = Parser.parse_args()
