CommonMark-ASTcheck
===================

tool to check validity of [CommonMark](http://commonmark.org) spec AST structure read from JSON (or directly by importing the function.)

Usage
-----

    rolands@kamaji:~/utils/CommonMark-ASTcheck$ cmark.py README.md -aj | cmark-astcheck.py
    ## AST valid.
    rolands@kamaji:~/utils/CommonMark-ASTcheck$ cmark-astcheck.py test.json
    ## AST valid.
    rolands@kamaji:~/utils/CommonMark-ASTcheck$ cmark-astcheck.py -h
    usage: cmark-astcheck.py [-h] [infile]

	Check validity of CommonMark JSON AST files or from STDIN.

	positional arguments:
	  infile      JSON file to check, defaults to STDIN.

	optional arguments:
	  -h, --help  show this help message and exit