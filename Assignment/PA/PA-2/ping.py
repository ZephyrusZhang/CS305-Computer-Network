import argparse
import sys

from models import *
from sockets import *
from time import time

PING_INTERVAL = 0.05
PING_TIMEOUT = 3


def ping(address, n=4, payload=None, id=None):
    """
        Create ICMPRequest and send through socket, then receive and parse reply.

        Hint: use ICMPSocket.send() to send packet and use ICMPSocket.receive() to receive

        Parameter
        ---------
        address : str
            IP of destination.
        n : int
            The number of ICMP request.
        payload : bytes
            Payload of datagram
        id : int
            The identifier of ICMP Request.

        Returns
        -------
        out : Host
            Ping result.
    """
    if is_hostname(address):
        address = resolve(address)[0]

    sock = ICMPSocket()
    id = id or unique_identifier()
    payload = payload or random_byte_message(56)
    reply = None
    packets_sent = 0
    rtts = []
    # TODO:
    for idx in range(n):
        request = ICMPRequest(address, id, idx, payload)
        start = time()
        sock.send(request)
        packets_sent += 1
        reply = sock.receive(request)
        end = time()
        rtts.append((end - start) * 1000)

    sock.close()
    if reply:
        return Host(
            address=reply.source,
            packets_sent=packets_sent,
            rtts=rtts)
    return None


if __name__ == "__main__":
    target = sys.argv[1]
    parser = argparse.ArgumentParser(description="ping")
    parser.add_argument('--n', type=int, default=4)
    parser.add_argument('--p', type=str, default=None)
    parser.add_argument('--i', type=int, default=None)
    args = parser.parse_args(sys.argv[2:])
    n = args.n
    i = args.i
    p = None
    if args.p:
        p = args.p.encode()
    host = ping(target, n, p, i)
    print(host.__str__())
