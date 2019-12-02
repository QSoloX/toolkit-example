# Almost A Web Toolkit

A Basic Web Crawler, Xss Injector, Sql Injector, Username lookup toolkit.

## Installation

**NOTE**: Python 3.7 or higher is required.

```bash
# Clone the repo
$ git clone https://github.com/QSoloX/AAWT.git

$ cd AAWT

# Install python 3.7, pip and pipenv if not already installed

# Install the enviroment
$ pipenv install
```

## Usage

```bash

# This is a shell based program running the main file will drop you into a shell
$ pipenv shell
$ python aawt.py
AWWT > load foobar_payload
AWWT foobar_payload > options
foobar_option value
AWWT foobar_payload > set foobar value
AWWT foobar_payload > shoot

Arguments:
    payloads                    displays all payloads currently inside payloads/
    load payload_name           loads the payload you want to use.
    options                     shows the options of the payload.
    set option_name value       sets the option to that value
    shoot                       runs the payload that you have selected.




```

## License

MIT © <br/>
Original Creator - [QSoloX](https://github.com/QSoloX)
