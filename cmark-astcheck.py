#!/usr/bin/env python
# 2014 - cmark-astcheck.py, roland shoemaker
# tool to check validity of CommonMark spec AST structure.
import json, argparse, sys

def check_block(ast, isJSON=True, struct=""):
	failed = 0
	if isJSON:
		block = json.loads(ast)
	else:
		block = ast
	if not type(block) is dict:
		print("block is not a object. "+str(type(block)))
		failed += 1
	else:
		for name in block.keys():
			if not name in ["t", "c", "open", "last_line_blank", "start_line", "start_column", "end_line", "children", "string_content", "strings", "inline_content", "destination", "label", "title", "list_data", "info", "tight", "parent", "level", "isOpen"]:
				if not struct is "":
					print(struct+"."+name+" is not a valid key.")
					failed += 1
				else:
					print(name+" is not a valid key.")
					failed += 1
	if not type(block['t']) is str:
		print(struct+".*something* is not a string.")
		failed += 1
	if block.get('c', None) and not type(block['c']) is list and not type(block['c']) is str:
		print(struct+block['t']+".c is not a string or list.")
		failed += 1
	elif block.get('c', None) and type(block['c']) is list:
		for i, b in enumerate(block['c']):
			if not type(b) is dict:
				print(struct+block['t']+".c["+str(i)+"] is not a object.")
				failed += 1
			else:
				failed += check_block(b, False, struct+block['t']+".c["+str(i)+"].")
	if block.get('open', None) and not type(block.get('open')) is bool: #type(block['open']) is bool:
		print(struct+block['t']+".open is not a boolean. ")
		failed += 1
	if not type(block['last_line_blank']) is bool:
		print(struct+block['t']+".last_line_blank is not a boolean.")
		failed += 1
	if block.get('start_line', None) and not block['start_line'] in [None, ""] and not type(block['start_line']) is int:
		print(struct+block['t']+".start_line is not a integer.")
		failed += 1
	else:
		if not block.get('start_line', "not") == "not" and not block['start_line'] in [None, ""] and block['start_line'] < 0:
			print(struct+block['t']+".start_line is less that 0.")
			failed += 1
	if not block.get('start_column', "not") == "not" and not type(block['start_column']) is int:
		print(struct+block['t']+".start_column is not a integer.")
		failed += 1
	elif not block.get('start_column', "not") == "not" and not block['start_column'] in [None, ""] and block['start_column'] < 0:
		print(struct+block['t']+".start_column is less that 0.")
		failed += 1
	if not block.get('end_line', "not") == "not" and not block['end_line'] in [None, ""] and not type(block['end_line']) is int:
		print(struct+block['t']+".end_line is not a integer.")
		failed += 1
	elif not block.get('end_line', "not") == "not" and not block['end_line'] in [None, ""] and block['end_line'] < 0:
		print(struct+block['t']+".end_line is less that 0.")
		failed += 1
	if not block.get('children', "not") == "not" and not type(block['children']) is list:
		print(struct+block['t']+".children is not a list.")
		failed += 1
	elif not block.get('children', "not") == "not":
		for i, b in enumerate(block['children']):
			if not type(b) is dict:
				print(struct+block['t']+".block.children["+str(i)+"] is not a object.")
				failed += 1
			else:
				failed += check_block(b, False, struct+block['t']+".children["+str(i)+"].")
	if block.get('string_content', None) and not type(block['string_content']) is str:
		print(struct+block['t']+".string_content is not a string.")
		failed += 1
	if block.get('strings', None) and not type(block['strings']) is list:
		print(struct+block['t']+".strings is not a list.")
		failed += 1
	elif block.get('strings', None):
		for i, s in enumerate(block['strings']):
			if not type(s) is str:
				print(block['t']+".strings["+str(i)+"] is not a string.")
				failed += 1
	if block.get('inline_content', None) and not type(block['inline_content']) is list:
		print(struct+block['t']+".inline_content is not a list.")
		failed += 1
	elif block.get('inline_content', None):
		for i, b in enumerate(block['inline_content']):
			if not type(b) is dict:
				print(struct+block['t']+".inline_content["+str(i)+"] is not a object.")
				failed += 1
			else:
				failed += check_block(b, False, struct+block['t']+".inline_content["+str(i)+"].")
	if block.get('destination', None) and not type(block['destination']) is str:
		print(struct+block['t']+".destination is not a string.")
		failed += 1
	if block.get('label', None) and (not type(block['label']) is str and not type(block['label']) is list):
		print(struct+block['t']+".label is not a string.")
		failed += 1
	elif block.get('label', None) and type(block['label']) is list:
		for i, b in enumerate(block['label']):
			if not type(b) is dict:
				print(struct+block['t']+".label["+str(i)+"] is not a object.")
				failed += 1
			else:
				failed += check_block(b, False, struct+block['t']+".label["+str(i)+"].")
	if block.get('title', None) and not type(block['title']) is str:
		print(struct+block['t']+".title is not a string.")
		failed += 1
	if block.get('list_data', None) and not type(block['list_data']) is dict:
		print(struct+block['t']+".list_data is not a object.")
		failed += 1
	else:
		if block.get('list_data', None) and block['list_data'].get('type', None) and not type(block['list_data']['type']) is str:
			print(struct+block['t']+".list_data.type is not a string.")
			failed += 1
		if block.get('list_data', None) and block['list_data'].get('delimiter', None) and not type(block['list_data']['delimiter']) is str:
			print(struct+block['t']+".list_data.delimiter is not a string.")
			failed += 1
		if block.get('list_data', None) and block['list_data'].get('start', None) and not type(block['list_data']['start']) is int:
			print(struct+block['t']+".list_data.start is not a integer.")
			failed += 1
		elif block.get('list_data', None) and block['list_data'].get('start', None) and block['list_data']['start'] < 0:
			print(struct+block['t']+".list_data.start is less than 0.")
			failed += 1
		if block.get('list_data', None) and block['list_data'].get('bullet_char', None) and not type(block['list_data']['bullet_char']) is str:
			print(struct+block['t']+".list_data.bullet_char is not a string.")
			failed += 1
		if block.get('list_data', None) and block['list_data'].get('padding', None) and not type(block['list_data']['padding']) is int:
			print(struct+block['t']+".list_data.padding is not a integer.")
			failed += 1
		else:
			if block.get('list_data', None) and block['list_data'].get('padding', None) and block['list_data']['padding'] < 0:
				print(struct+block['t']+".list_data.padding is less than 0.")
				failed += 1
	if block.get('info', None) and not type(block['info']) is str:
		print(struct+block['t']+".info is not a string.")
		failed += 1
	if block.get('tight', None) and not type(block['tight']) is bool:
		print(struct+block['t']+".tight is not a boolean.")
		failed += 1
	return failed

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Check validity of CommonMark JSON AST files or from STDIN.")
	parser.add_argument('infile', nargs="?", type=argparse.FileType('r'), default=sys.stdin, help="JSON file to check, defaults to STDIN.")
	args = parser.parse_args()

	lines = []
	for line in args.infile:
	    lines.append(line)
	data = "".join(lines)

	tests = check_block(data)

	if tests > 0:
		print("## AST invalid, "+str(tests)+" tests failed.")
	else:
		print("## AST valid.")