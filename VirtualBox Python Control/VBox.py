# Bill Erhard
# RTC CNT 350
# Controls VirtualBox using Python

import virtualbox

def clone_vm(vm_os):
    #from time import sleep
    print(vm_os)
    vm = vm_os
    vbox = virtualbox.VirtualBox()
    for machine in vbox.machines:
        print(machine.name)
    print(get_ip(vm))
    #sleep(3) # This checks that threads are async. 3 secs total sleep good, 3*num_threads bad.
    pass


def get_ip(vm):
    return "8.8.8.8"


def main():
    import sys
    from threading import Thread

    vm_create_number = int(sys.argv[1])  # Number of VMs to create
    vm_os = sys.argv[2]  # OS for the VM, out of 3 available

    threads = []
    for i in range(vm_create_number):
        #t = Thread(target=clone_vm, args=(vm_os,))
        #threads.append(t)
        #t.start()
        clone_vm(vm_os)
   # for t in threads:
     #   t.join()


if __name__ == '__main__':
    main()
