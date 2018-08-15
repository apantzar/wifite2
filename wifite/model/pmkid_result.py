#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ..util.color import Color
from .result import CrackResult

class CrackResultPMKID(CrackResult):
    def __init__(self, bssid, essid, pmkid_hash, key):
        self.result_type = 'PMKID'
        self.bssid = bssid
        self.essid = essid
        self.pmkid_hash = pmkid_hash
        self.key = key
        super(CrackResultPMKID, self).__init__()

    def dump(self):
        if self.essid:
            Color.pl('{+} %s: {C}%s{W}' %
                ('Access Point Name'.rjust(19), self.essid))
        if self.bssid:
            Color.pl('{+} %s: {C}%s{W}' %
                ('Access Point BSSID'.rjust(19), self.bssid))
        Color.pl('{+} %s: {C}%s{W}' %
            ('Encryption'.rjust(19), self.result_type))
        if self.pmkid_hash:
            Color.pl('{+} %s: {C}%s{W}' %
                ('PMKID'.rjust(19), self.pmkid_hash))
        if self.key:
            Color.pl('{+} %s: {G}%s{W}' % ('PSK (password)'.rjust(19), self.key))
        else:
            Color.pl('{!} %s  {O}key unknown{W}' % ''.rjust(19))

    def to_dict(self):
        return {
            'type'  : self.result_type,
            'date'  : self.date,
            'essid' : self.essid,
            'bssid' : self.bssid,
            'key'   : self.key,
            'pmkid' : self.pmkid_hash
        }

if __name__ == '__main__':
    w = CrackResultPMKID('AA:BB:CC:DD:EE:FF', 'Test Router', 'abc*def*ghi*jkl', 'abcd1234')
    w.dump()

    w = CrackResultPMKID('AA:BB:CC:DD:EE:FF', 'Test Router', 'abc*def*ghi*jkl', 'Key')
    print('\n')
    w.dump()
    w.save()
    print(w.__dict__['bssid'])

