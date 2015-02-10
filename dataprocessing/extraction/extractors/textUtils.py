# -*- coding: utf-8 -*-
import re
import regex
import regexUtils

def takeSubStrBasedOnPos(text, start, width=None):
    if width is not None:
        t = text[start:(start+width)]
    else:
        t = text[start:]
    return t

def takeSubStrBasedOnFirstRegexOccurrence(text, pattern, options=re.UNICODE):
    pos = regexUtils.findFirstPositionWithRegexSearch(pattern, text, options)
    if pos == -1:
        return text
    else:
        return text[0:pos]


def removeSpacesFromText(text):
    return text.replace(" ","")