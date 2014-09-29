CommonMark-ASTcheck
===================

tool to check validity of [CommonMark](http://commonmark.org) spec AST structure read from JSON (or directly by importing the function), this will eventually be merged into [CommonMark-py](https://github.com/rolandshoemaker/CommonMark-py) most likely.

**note:** *this is extremely rough at the moemnt, i plan to add proper structure checking later but currently it just validates the variable types in the ugliest way possible (i'm sorry i've not slept ._.)*

Usage
-----

    rolands@kamaji:~/utils/CommonMark-ASTcheck$ cmark.py README.md -aj | cmark-astcheck.py
    ## AST valid.
    rolands@kamaji:~/utils/CommonMark-ASTcheck$ python3 cmark-astcheck.py README.json 
    ## AST valid.
    rolands@kamaji:~/utils/CommonMark-ASTcheck$ python3 cmark-astcheck.py BROKEN.json 
    Document.start_column is not a integer.
    Document.children[0].SetextHeader.end_line is not a integer.
    SetextHeader.strings[0] is not a string.
    Document.children[0].SetextHeader.inline_content[1] is not a object.
    Document.children[0].SetextHeader.tight is not a boolean.
    Document.children[1].Paragraph.inline_content[0].bar is not a valid key.
    Document.children[1].Paragraph.inline_content[1].Link.label[0].Str.last_line_blank is not a boolean.
    SetextHeader.strings[0] is not a string.
    Document.children[3].IndentedCode.start_column is not a integer.
    ## AST invalid, 9 tests failed.
    rolands@kamaji:~/utils/CommonMark-ASTcheck$
