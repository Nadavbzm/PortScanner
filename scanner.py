# importing libraries
import socket

def portInfo(num):
    file_path = "Table.csv"

    with open(file_path) as f:
        for line in f:
            data = line.split(",")
            if (data[0].strip() == str(num)):
                print("[+] (" + str(num) + ") Protocol Name: " + data[1] + "\n     Comment: " + data[2])


# Makes connection to server
def Make_Connection(PORT, TEST_IP):

    try:
        # Connecting to remote adress
        server_address = (TEST_IP, PORT)

        # Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(server_address)

        # Closing the socket
        sock.close()
        return True

    except:
        return False

#main function
def main():
    open_ports = []
    ip = input("Enter IP of server to scan: ")
    port_range = int(input("Enter Port Range To Scan: "))
    for i in range(port_range):
        if Make_Connection(i, ip):
            open_ports += [i]
            print("[+]  [-- Open Port Found -- " + str(i) + " --] :: [" + str(i) + " / " + str(port_range) + "]")

        else:
            print("[-] Port " + str(i) + " Is Closed :: [" + str(i) + " / " + str(port_range) + "]")

    print("List of open Ports on Server (" + str(ip) + "): " + str(open_ports))
   # print("\nInformation about the ports")
    #for i in open_ports:
     #   portInfo(i)

if __name__ == '__main__':
    main()
