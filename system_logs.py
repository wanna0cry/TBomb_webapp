import platform
import socket

def platform_details():
 
    system = platform.uname()

    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)

    data = {
        "System": "{}".format(system.system),
        "Node Name": "{}".format(system.node),
        "Release": "{}".format(system.release),
        "Version": "{}".format(system.version),
        "Machine": "{}".format(system.machine),
        "Processor": "{}".format(system.processor),
        "IP Address": "{}".format(IPAddr)
    }

    return data


def system_log():
    pass