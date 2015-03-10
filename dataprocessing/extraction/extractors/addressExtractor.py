# -*- coding: utf-8 -*-
import re
import regex
from extraction.extractors.baseExtractor import BaseExtractor
from extractionkeys import KEYS

class AddressExtractor(BaseExtractor):
    regexPattern = r'(?:\W- ?Os\b|\W- ?os\b|\W- ?o5\b|\W- ?O5\b|\W- ?05\b)(?P<address>(?:.|\n)*?)(?=$|Rva|\.)'
    address = ""

    def extract(self, text):
        matches = self._executeSearchRegex(text)
        self.address = self._constructAddressFromMatch(matches)
        return self._constructReturnDict()

    def _constructAddressFromMatch(self, matches):
        if matches != None:
            self.address = matches.group("address")
        return self.address

    def _constructReturnDict(self):
        return {KEYS["address"] : self.address}

