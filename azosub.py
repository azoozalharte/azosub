from prettytable import PrettyTable

from pyfiglet import Figlet
custom_fig = Figlet(font='graffiti')
print(custom_fig.renderText('Azosub'))


#################################################################

ipStr = input('Please inter the IP: ')
subnetStr = input('How many subnet do you want: ')

ip = float(ipStr[0:3])
subnetI = int(subnetStr)


# store new subnets form netwrokId function
subnetList = []


def netwrokId(n, subnetRange, submask):
    # give the last number on ipStr
    lastnum = int(ipStr[-1])
    usableHost = subnetRange - 2
    Broadcast = subnetRange - 1
    if lastnum > 0:
        print("Sorry Azosub don't subnetting a subnet")
    else:
        # if subnet(4) - 1 = 3 and 3 * host(64) = lastnetworkIP(192)
        n = subnetI - 1
        lastnetID = n * subnetRange

        # EX: 0 <= 192
        while lastnum <= lastnetID:
            subnetList.append(lastnum)
            lastnum = lastnum + subnetRange

        table = PrettyTable(['Network ID', 'Subnet mask',
                             "Host Id range", "#of usable Host", "Broadcast ID"])
        for i in subnetList:
            fullnwIP = ipStr[:-1]+str(i)
            fullnwBroadcast = ipStr[:-1]+str(Broadcast)
            firstHost = i + 1
            lastHost = Broadcast - 1
            hostRange = "{}{} - {}{}".format(
                ipStr[:-1], firstHost, ipStr[:-1], lastHost)
            table.add_row([fullnwIP, submask, hostRange,
                           usableHost, fullnwBroadcast])
            Broadcast = subnetRange + Broadcast

        print(table)


def subnetC(sub):
    if sub == 1:
        netwrokId(sub, 256, "/24")
    elif sub == 2:
        netwrokId(sub, 128, "/25")
    elif sub in range(3, 5):
        netwrokId(sub, 64, "/26")
    elif sub in range(5, 9):
        netwrokId(sub, 32, "/27")
    elif sub in range(9, 17):
        netwrokId(sub, 16, "/28")
    elif sub in range(17, 33):
        netwrokId(sub, 8, "/29")
    elif sub in range(33, 65):
        netwrokId(sub, 4, "/30")
    elif sub in range(65, 129):
        netwrokId(sub, 2, "/31")
    elif sub in range(129, 257):
        netwrokId(sub, 1, "/32")
    else:
        print('I Cant the last range for subnetting is 256, Please try again')


if ip in range(192, 224):
    subnetC(subnetI)
else:
    print("Sorry Azosub support just class C IP")
