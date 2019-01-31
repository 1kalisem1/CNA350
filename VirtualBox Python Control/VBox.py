# Bill Erhard
# RTC CNT 150
# Controls VirtualBox using Python


def clone_vm(vm_os):
    print(vm_os)
    pass


def get_ip(vm):
    print("8.8.8.8")
    pass


def main():
    import sys
    from threading import Thread
    vm_create_number = int(sys.argv[1])  # Number of VMs to create
    vm_os = sys.argv[2]  # OS for the VM, out of 3 available

    threads = []
    for i in range(vm_create_number):
        t = Thread(target=clone_vm, args=(vm_os,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    install_upgrade.sh
    for vm in threads:
        print(get_ip(vm))


if __name__ == '__main__':
    main()
