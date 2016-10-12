import os

INTERFACES = [
    ('enp0s8', '10.0.3.15', '10.0.3.0/24', '10.0.3.2'),
    ('enp0s9', '10.0.4.15', '10.0.4.0/24', '10.0.4.2'),
]


def run(cmd):
    print(cmd)
    os.system(cmd)


def main(interfaces=INTERFACES):

    # Run some commands for every interface we have.
    for i, (dev, ip, subnet, gateway) in enumerate(interfaces, start=1):

        # First add a rule to use separate routing table for source IP
        run('ip rule add from {ip} table {i}'.format(**locals()))

        # Now routing tables for each interface:
        run('ip route add {subnet} dev {dev} scope link table {i}'.format(**locals()))
        run('ip route add default via {gateway} dev {dev} table {i}'.format(**locals()))

        # Use the first interface as default
        if i == 1:
            run('ip route add default scope global nexthop via {gateway} dev {dev}'.format(**locals()))


if __name__ == '__main__':
    main()
