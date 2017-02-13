#! /bin/env python3

import argparse
import json
import sys

class address:
	link_local = None
	mac = None

class link_local_to_mac:
	file = None
	json = False
	addresses=list()


	def convert_all(self):
		for i in self.addresses:
			i.mac = self.convert(i)

	def convert(self, link_local_address):
		mac_address_parts = list()

		local_var_link_local_address="{}".format(link_local_address.link_local)

		subnet_index = local_var_link_local_address.find("/")
		
		# strip CIDR
		if subnet_index != -1:
			local_var_link_local_address = local_var_link_local_address[:subnet_index]

		# strip interface part

		interface_index = local_var_link_local_address.find("%")

		if interface_index != -1:
			local_var_link_local_address = local_var_link_local_address[:interface_index]

		link_local_address_parts = local_var_link_local_address.split(":")

		for i in link_local_address_parts[-4:]:
			while len(i) < 4:
				i = "0{}".format(i)
			mac_address_parts.append(i[:2])
			mac_address_parts.append(i[-2:])

		mac_address_parts[0] = "%02x" % (int(mac_address_parts[0], 16) ^ 2)


		del mac_address_parts[4]
		del mac_address_parts[3]

		return ":".join(mac_address_parts)

	def read_input(self):
		input_file=None

		if self.file != None:
			input_file = open(self.file, "r")
		else:
			input_file = sys.stdin

		addresses = input_file.readlines()

		for i in range(0,len(addresses)):
			if addresses[i].strip() == "":
				continue

			addr = address()
			addr.link_local = addresses[i]
			self.addresses.append(addr)

	def print_output(self):

		if self.json:
			json = list()
			for i in self.addresses:
				json.append(i.mac)
			print (json)

		else:
			for i in self.addresses:
				print(i.mac)

	def run(self):
		parser = argparse.ArgumentParser(
    		description="Converts IPv6 link-local addresses to MAC addresses")
		parser.add_argument("-j",
    		"--json",
    		action = "store_true",
    		dest = "json",
    		default = False,
    		help =  "Whether to print addresses in a JSON array",
    		)
		parser.add_argument("file",
    		default = None,
    		nargs = "?",
    		help = "An optional file from which to read the link-local addresses from."
    		"It must contain one link-local address per line."
    		)

		args = parser.parse_args()
		self.json = args.json
		self.file = args.file

		self.read_input()

		self.convert_all()

		self.print_output()

if __name__ == "__main__":
	converter = link_local_to_mac()
	converter.run()