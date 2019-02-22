# Bill Erhard
# RTC CNT 350
# Controls VirtualBox using Python

import virtualbox
from virtualbox.library_base import VBoxError
from virtualbox import library


# Along with pyvbox and VBoxAPI docs, the following stuff helped on this.
# https://github.com/sethmlarson/virtualbox-python/blob/master/virtualbox/library_ext/machine.py
def clone_vm(vm_os, i):
    # from time import sleep
    vbox = virtualbox.VirtualBox()
    try:
        vm = vbox.find_machine(vm_os)
    except VBoxError:
        print("No VM by that name found. Cannot clone.")
        return

    clone = vbox.create_machine("",vm.name+str(i),[],"","")
    vm.clone_to(clone,library.CloneMode.all_states,[])
    vbox.register_machine(clone)

    session = clone.create_session()
    login = session.console.guest.create_session('bill', 'password')
    process, stdout, stderr = login.execute('~/install_upgrade.sh')
    print(stdout)
    print(clone.name)
    print(get_ip(vm))
    # sleep(3) # This checks that threads are async. 3 secs total sleep good, 3*num_threads bad.
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
        # t = Thread(target=clone_vm, args=(vm_os,))
        # threads.append(t)
        # t.start()
        clone_vm(vm_os, i)


# for t in threads:
#   t.join()


if __name__ == '__main__':
    main()
