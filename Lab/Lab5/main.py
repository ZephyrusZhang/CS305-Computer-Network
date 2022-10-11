import struct
import dns.resolver


class DNSHeader:
    Struct = struct.Struct('!6H')

    def __init__(self):
        self.__dict__ = {
            field: None
            for field in
            ('ID', 'QR', 'OpCode', 'AA', 'TC', 'RD', 'RA', 'Z', 'RCode', 'QDCount', 'ANCount', 'NSCount', 'ARCount')
        }

    def parse_header(self, data):
        self.ID, misc, self.QDCount, self.ANcount, self.NScount, self.ARcount = DNSHeader.Struct.unpack_from(data)
        self.QR = (misc & 0x8000) != 0
        self.OpCode = (misc & 0x7800) >> 11
        self.AA = (misc & 0x0400) != 0
        self.TC = (misc & 0x200) != 0
        self.RD = (misc & 0x100) != 0
        self.RA = (misc & 0x80) != 0
        self.Z = (misc & 0x70) >> 4
        self.RCode = misc & 0xF

    def __str__(self):
        return f'<DNSHeader {str(self.__dict__)}>'


if __name__ == '__main__':
    while True:
        try:
            response = dns.resolver.resolve(qname=input('Domain name: '),
                                            rdtype=input('Query type: '),
                                            raise_on_no_answer=False)
            print(f'Who send the answer\n\033[32m{response.nameserver}\033[0m')
        except KeyboardInterrupt:
            pass
