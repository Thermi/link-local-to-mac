link-local-to-mac
================

Description
================

This script reads IPv6 link-local addresses from stdin or a file that can be
specified as the first argument and prints the MAC addresses from the input.

Usage
===============

Run the python script and either supply a newline seperated list of link-local
addresses or specify a file with the same format as the first argument.

By default, the script prints out a newline seperated list of lower-case
MAC addresses. The original order of the addresses is preserved.

It can optionally print the output as a list in JSON format by using --json

./link-local-to-mac.py [-j --json] [input file]

Options
===============

-j --json Makes the script write the output as a JSON list