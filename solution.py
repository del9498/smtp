from socket import *
def smtp_client(port=1025, mailserver='smtp.gmail.com'):
    msg = "\r\n TEST HELLO EMAIL MESSAGE"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope
    # mailserver = 'smtp.gmail.com'
    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))

    recv = clientSocket.recv(1024).decode()

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()

    # Send MAIL FROM command and print server response.
    mailFrom = 'MAIL FROM: <devonvlcek@gmail.com>\r\n.'
    clientSocket.send(mailFrom.encode())
    recv2 = clientSocket.recv(1024)

    # Send RCPT TO command and print server response.
    rcptTo = 'RCPT TO: <devonelong@gmail.com>\r\n'
    clientSocket.send(rcptTo.encode())
    recv3 = clientSocket.recv(1024)

    # Send DATA command and print server response.
    data = 'DATA\r\n'
    clientSocket.send(data.encode())
    recv4 = clientSocket.recv(1024)

    # Send message data.
    clientSocket.send('SUBJECT: hello there\r\n'.encode())
    clientSocket.send(msg.encode())

    # Message ends with a single period.
    clientSocket.send(endmsg.encode())
    recv5 = clientSocket.recv(1024)

    # Send QUIT command and get server response.
    quitCmd = 'QUIT\r\n'
    clientSocket.send(quitCmd.encode())
    recv6 = clientSocket.recv(1024)


if __name__ == '__main__':
    smtp_client(1025, 'smtp.gmail.com')
