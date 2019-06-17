Opis komunikacji master – węzły obliczeniowe.

Do komunikacji pomiędzy serwerem (masterem) a węzłami obliczeniowymi (slave) wykorzystaliśmy dwa laptopy z systemem Linux (Ubuntu oraz Pop!_OS). Poniżej kroki, które wykonaliśmy na systemach.
1.	Oba środowiska - wykonanie update: <br/>
  a.	sudo apt-get update<br/>
2.	Oba środowiska - instalacja podstawowych narzędzi – Python, MPI, OpenSSH:<br/>
  a.	sudo apt-get install -y python<br/>
  b.	sudo apt-get install -y python-mpi4py<br/>
  c.	sudo apt­get install -y openssh-server<br/>
3.	Oba środowiska – dodanie IP w pliku /etc/hosts (użycie np. nano/vim)<br/>
  a.	Sprawdzanie IP poprzez np. ip addr (komputery powinny znajdować się w jednej sieci)<br/>
  b.	sudo nano /etc/hosts <br/>
    i.	Umieszczamy adresy wraz z hostname i zapisujemy, np. <br/>
        192.168.43.148 master<br/>
        192.168.43.127 slave<br/>
4.	Oba środowiska - stworzenie nowych użytkowników i przełączenie się na niego<br/>
  a.	sudo adduser mpiuser (hasło dowolne)<br/>
  b.	su – mpiuser<br/>
5.	Oba środowiska – wygenerowanie kluczy ssh, skopiowanie ich na pozostałe node (pozwolą one na komunikację pomiędzy – bez konieczności podawania hasła)<br/>
  a.	ssh-keygen -t rsa<br/>
  b.	ssh-copy-id slave/master/etc.<br/>
  c.	eval `ssh-agent`<br/>
  d.	ssh-add ~/.ssh/id_rsa.pub<br/>
  e.	od tego momentu powinniśmy móc się dostać na nody poprzez ssh, np. <br/>
      ssh slave/master/etc.<br/>
6.	Server (master) - instalacja server nfs i stworzenie dowolnego folderu (np. cloud) – umieścić w nim program<br/>
  a.	sudo apt-get install nfs-kernel-server<br/>
  b.	mkdir ~/cloud<br/>
7.	Server (master) – do udostępnienia folderu na pozostałe node edycja /etc/exports<br/>
  a.	sudo nano /etc/exports<br/>
  b.	/home/mpiuser/cloud *(rw,sync,no_root_squash,no_subtree_check)<br/>
  c.	exportfs -a<br/>
  d.	sudo service nfs-kernel-server restart<br/>
8.	Slave (client) – intalacja nfs client i podmontowanie udostępnionego folder<br/>
  a.	sudo apt-get install nfs-common<br/>
  b.	mkdir ~/cloud<br/>
  c.	sudo mount -t nfs master:/home/mpiuser/cloud ~/cloud<br/>
  d.	sprawdzenie czy zamontowano df -h<br/>
9.	Server (master) – uruchomienie programu z podziałem na node (podanie hostname <br/>
  a.	mpiexec -np 2 -hosts master, slave python main.py<br/>
 
