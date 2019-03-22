This project is about getting an RTMP Server running on a raspberry pi zero. Start by following https://obsproject.com/forum/resources/how-to-set-up-your-own-private-rtmp-server-using-nginx.50/.
Note: that guide may or may not work well depending on your flavor of linux.
Specifically, using latest version of Ubuntu Desktop, the OpenSSL version pre-installed with the OS conflicts with the one needed for rtmp module on the nginx server. Uninstalling said OpenSSL version breaks Ubuntu Desktop(it ceases to be a desktop version...)

Steps I used to try to build and start the nginx server with RTMP module can be found at https://github.com/billerhard/CNA335/blob/master/RTMP/configure.sh This is really just a shell script that could be run with some modifications to quickly and automatically set up the server (great for kubernetes/vm/docker use!).

For Kubernetes control from a windows host with virtualbox installed, use these three guides to get started:
https://kubernetes.io/docs/tasks/tools/install-kubectl/

https://kubernetes.io/docs/tasks/tools/install-minikube/

https://kubernetes.io/docs/setup/minikube/

You may want to use my example powershell profile for some useful aliases. Make sure the kubectl/minikube aliases point to the directories where you installed the respective .exe files. (I used ~/Documents/kubectl/ and C:\Program Files (x86)\Kubernetes\Minikube)

or install kubernetes dashboard:
https://github.com/kubernetes/dashboard

For some reason minikube with kubectl sometimes works and sometimes doesn't on my windows 10 host using virtualbox. It didn't work during my presentation in class but did work 2x times I tried it at home. Dashboard has a lot of permission issues that I was unable to resolve. I wasn't able to get any useful RTMP server up and running in the cluster due to aforementioned OpenSSL/dependency issues on ubuntu.
