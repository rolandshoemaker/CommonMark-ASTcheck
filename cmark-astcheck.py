#!/usr/bin/env python
import json, argparse

def check_block(ast, isJSON=True, struct=""):
	if isJSON:
		block = json.loads(ast)
	else:
		block = ast
	if not type(block) is object:
		print("block is not a object.")
	else:
		for t in block.keys():
			if not t in ["t", "c", "open", "last_line_blank", "start_line", "start_column", "end_line", "children", "string_content", "strings", "inline_content", "destination", "label", "title", "list_data", "info", "tight"]:
				if not struct is "":
					print(struct+"."+t+" is not a valid key.")
				else:
					print(t+" is not a valid key.")
	if not type(block['t']) is str:
		print(struct+block['t']+".t is not a string.")
	if not type(block['c']) is list or not type(block['c']) is str:
		print(struct+block['t']+".c is not a string or list.")
	elif type(block['c']) is list:
		for i, b in enumerate(block['c']):
			if not type(b) is object:
				print(struct+block['t']+".c["str(i)+"] is not a object.")
			else:
				check_block(b, False, struct+block['t']+".c["+str(i)+"].")
	if not type(block['open']) is bool:
		print(struct+block['t']+".open is not a boolean.")
	if not type(block['last_line_blank']) is bool:
		print(struct+block['t']+".last_line_blank is not a boolean.")
	if not type(block['start_line']) is int:
		print(struct+block['t']+".start_line is not a integer.")
	else:
		if block['start_line'] < 0:
			print(struct+block['t']+".start_line is less that 0.")
	if not type(block['start_column']) is int:
		print(block['t']+".start_column is not a integer.")
	else:
		if block['start_column'] < 0:
			print(struct+block['t']+".start_column is less that 0.")
	if not type(block['end_line']) is int:
		print(struct+block['t']+".end_line is not a integer.")
	else:
		if block['end_line'] < 0:
			print(struct+block['t']+".end_line is less that 0.")
	if not type(block['children']) is list:
		print(struct+block['t']+".children is not a list.")
	else:
		for i, b in block['children']:
			if not type(b) is object:
				print(struct+block['t']+".block.children["+str(i)+"] is not a object.")
			else:
				check_block(b, False, struct+block['t']+".children["+str(i)+"].")
	if not type(block['string_content']) is str:
		print(struct+block['t']+".string_content is not a string.")
	if not type(block['strings']) is list:
		print(struct+block['t']+".strings is not a list.")
	else:
		for i, s in enumerate(block['strings']):
			if not type(s) is str:
				print(block['t']+".strings["+str(i)+"] is not a string.")
	if not type(block['inline_content']) is list:
		print(struct+block['t']+".inline_content is not a list.")
	else:
		for i, b in block['inline_content']:
			if not type(b) is object:
				print(struct+block['t']+".inline_content["+str(i)+"] is not a object.")
			else:
				check_block(b, False, struct+block['inline_content']+".inline_content["+str(i)+"].")
	if not type(block['destination']) is str:
		print(struct+block['t']+".destination is not a string.")
	if not type(block['label']) is str:
		print(struct+block['t']+".label is not a string.")
	if not type(block['title']) is str:
		print(struct+block['t']+".title is not a string.")
	if not type(block['list_data']) is object:
		print(struct+block['t']+".list_data is not a object.")
	else:
		if not type(block['list_data']['type']) is str:
			print(struct+block['t']+".list_data.type is not a string.")
		if not type(block['list_data']['delimiter']) is str:
			print(struct+block['t']+".list_data.delimiter is not a string.")
		if not type(block['list_data']['start']) is int:
			print(struct+block['t']+".list_data.start is not a integer.")
		else:
			if block['list_data']['start'] < 0:
				print(struct+block['t']+".list_data.start is less than 0.")
		if not type(block['list_data']['bullet_char']) is str:
			print(struct+block['t']+".list_data.bullet_char is not a string.")
		if not type(block['list_data']['padding']) is int:
			print(struct+block['t']+".list_data.padding is not a integer.")
		else:
			if block['list_data']['padding'] < 0:
				print(struct+block['t']+".list_data.padding is less than 0.")
	if not type(block['info']) is str:
		print(struct+block['t']+".info is not a string.")
	if not type(block['tight']) is bool:
		print(struct+block['t']+".tight is not a boolean.")

if __name__ == "__main__":
	parser = argparser.ArgumentParser(description="Check validity of CommonMark JSON AST files or from STDIN.")
	parser.add_argument('infile', nargs="?", type=argparse.FileType('r'), default=sys.stdin, help="JSON file to check, defaults to STDIN.")
	args = parser.parse_args()

	lines = []
	for line in args.infile:
	    lines.append(line)
	data = "".join(lines)

	check_block(data)