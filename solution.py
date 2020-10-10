from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n This is a nice test message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))
    # Fill in end

    recv = clientSocket.recv(1024).decode()
    # print(recv)
    if recv[:3] != '220':
        recv = '220 reply not received from server.'

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    print(recv1)
    if recv1[:3] != '250':
        recv1 = '250 reply not received from server.'

    # Send MAIL FROM command and print server response.
    mailFrom = 'MAIL FROM: <del9498@nyu.edu> \r\n'
    clientSocket.send(mailFrom.encode())
    recv2 = clientSocket.recv(1024)
    if recv2[:3] != '250':
        recv2 = '250 reply not received from server.'

    # Send RCPT TO command and print server response.
    rcptTo = 'RCPT TO: <devonelong@gmail.com> \r\n'
    clientSocket.send(rcptTo.encode())
    recv3 = clientSocket.recv(1024)
    if recv3[:3] != '250':
        recv3 = '250 reply not received from server.'

    # Send DATA command and print server response.
    mailData = 'DATA\r\n'
    clientSocket.send(mailData.encode())
    recv4 = clientSocket.recv(1024)

    # Send message data.
    clientSocket.send(msg.encode)
    
    # Message ends with a single period.
    msgEnd = '.\r\n'
    clientSocket.send(msgEnd.encode())
    recv5 = clientSocket.recv(1024)

    # Send QUIT command and get server response.
    sendQuit = 'QUIT\r\n'
    clientSocket.send(sendQuit.encode())
    recv6 = clientSocket.recv(1024)
    clientSocket.close()


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
