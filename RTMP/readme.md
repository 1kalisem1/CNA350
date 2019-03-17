This project is about getting an RTMP Server running on a raspberry pi zero. Start by following https://obsproject.com/forum/resources/how-to-set-up-your-own-private-rtmp-server-using-nginx.50/.
Note: that guide may or may not work well depending on your flavor of linux.
Specifically, using latest version of Ubuntu Desktop, the OpenSSL version pre-installed with the OS conflicts with the one needed for rtmp module on the nginx server. Uninstalling said OpenSSL version breaks Ubuntu Desktop(it ceases to be a desktop version...)

For Kubernetes control from a windows host with virtualbox installed, use these three guides to get started:
https://kubernetes.io/docs/tasks/tools/install-kubectl/
https://kubernetes.io/docs/tasks/tools/install-minikube/
https://kubernetes.io/docs/setup/minikube/

You may want to use my example powershell profile for some useful aliases. Make sure the kubectl/minikube aliases point to the directories where you installed the respective .exe files. (I used ~/Documents/kubectl/ and C:\Program Files (x86)\Kubernetes\Minikube)

or install kubernetes dashboard:
https://github.com/kubernetes/dashboard
