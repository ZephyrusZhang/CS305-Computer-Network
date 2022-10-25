import logging

import dns.resolver

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO,
                    format='\033[37m%(asctime)s ~ %(funcName)s: %(message)s\033[0m',
                    datefmt='%H:%M:%S')


def get_authoritative_nameserver(domain):
    n = dns.name.from_text(domain)

    depth = 2
    default = dns.resolver.get_default_resolver()
    nameserver = default.nameservers[0]

    last = False
    while not last:
        s = n.split(depth)

        last = s[0].to_unicode() == u'@'
        sub = s[1]

        logger.info(f"Looking up \033[34m{sub}\033[0m \033[37mon\033[0m \033[32m{nameserver}\033[0m")
        query = dns.message.make_query(sub, dns.rdatatype.NS)
        response = dns.query.udp(query, nameserver)

        rcode = response.rcode()
        if rcode != dns.rcode.NOERROR:
            if rcode == dns.rcode.NXDOMAIN:
                raise Exception('%s does not exist.' % sub)
            else:
                raise Exception('Error %s' % dns.rcode.to_text(rcode))

        if len(response.authority) > 0:
            rrset = response.authority[0]
        else:
            rrset = response.answer[0]

        rr = rrset[0]
        if rr.rdtype == dns.rdatatype.SOA:
            logger.info(f"Same server is authoritative for {sub}")
        else:
            authority = rr.target
            logger.info(f"{authority} is authoritative for {sub}")
            nameserver = default.resolve(authority).rrset[0].to_text()

        depth += 1

    return nameserver


if __name__ == '__main__':
    try:
        while True:
            domain = input('Enter domain: ')
            logger.info(f"IP for {domain} is \033[32m{get_authoritative_nameserver(domain=domain)}\033[0m")
    except KeyboardInterrupt:
        pass
