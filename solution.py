from socket import *
import ssl
import base64

def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n A nice test message."
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope
    mailserver = "smtp.gmail.com"
    serverPort = 465

    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    clientSocket = socket(AF_INET,SOCK_STREAM)
    clientSocket.connect((mailserver, serverPort))
    clientSocketSSL = ssl.wrap_socket(clientSocket)
    recv = clientSocketSSL.recv(1024).decode()
   
    # Send HELO command and print server response.
    heloCommand = b"Hello devon\r\n"
    clientSocketSSL.send(heloCommand)
    recv1 = clientSocketSSL.recv(1024).decode()


  
    username = "devonelong@gmail.com"
    password = "afakepassword"
    base64Authcredentials = ("\x00"+username+"\x00"+password).encode()
    base64Authcredentials = base64.b64encode(base64Authcredentials)
    authMessage = "AUTH PLAIN ".encode()+base64Authcredentials+'\r\n'.encode()
    clientSocketSSL.send(authMessage)
    recv2 = clientSocketSSL.recv(1024).decode()
   
    # Send MAIL FROM command and print server response.
    mailFrom = b"MAIL FROM:<devonelong@gmail.com>\r\n"
    clientSocketSSL.send(mailFrom)
    recv3 = clientSocketSSL.recv(1024).decode()
  
    # Send RCPT TO command and print server response.
    rcptTo = b"RCPT TO:<del9498@nyu.edu>\r\n"
    clientSocketSSL.send(rcptTo)
    recv4 = clientSocketSSL.recv(1024).decode()
   
    # Send DATA command and print server response.
    dataCmd = b"DATA\r\n"
    clientSocketSSL.send(dataCmd)
    recv5 = clientSocketSSL.recv(1024).decode()

    # Send message data.
    clientSocketSSL.send(msg)

    # Message ends with a single period.
    clientSocketSSL.send(endmsg)

    # Send QUIT command and get server response.
    #print('reached the end')
    quitCmd = b"QUIT\r\n"
    clientSocketSSL.send(quitCmd)
    recv6 = clientSocketSSL.recv(1024).decode()
   
    clientSocketSSL.close()


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
