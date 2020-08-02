# simple_htcondor_external_submitter
Component Repository for submitting test jobs to HTCondor CE using a network other than the one setup by the SIMPLE framework

# Installation Instructions

## Prequisites
- Ensure SELinux is disabled on your host machine.

    ```
    [root@simple-condor-generic-submitter ~]# sestatus
    SELinux status:                 disabled 
    
    ```
- Git clone the repository

  ```
    yum install -y git
    cd ~
    git clone https://github.com/simple-framework/simple_htcondor_external_submitter
  ```
  
- Copy your Grid User Certificate
  ```
   cd ~/simple_htcondor_external_submitter/sh/config
   ### copy your usercert.pem and userkey.pem in this directory ###
  ```
  The final directory structure would look as follows. Make sure your userkey has correct permissions.
  ```
  [root@simple-condor-generic-submitter config]# ls -la ~/simple_htcondor_external_submitter/sh/config/
  \total 12
  drwxr-xr-x 3 root root   77 Aug  2 12:48 .
  drwxr-xr-x 4 root root   56 Aug  2 12:32 ..
  -rwxr-xr-x 1 root root  897 Aug  2 12:32 init.sh
  drwxr-xr-x 2 root root   22 Aug  2 12:32 sleep_job
  -rw-r--r-- 1 root root 3322 Aug  2 12:48 usercert.pem
  -rw------- 1 root root 1958 Aug  2 12:48 userkey.pem
  ```

- Install Docker (>=19)
  - Follow instructions here: https://docs.docker.com/engine/install/centos/
  - ``` systemctl start docker ```
  
## Build the image and Start the container

``` 
cd ~/simple_htcondor_external_submitter/sh
docker build -t simple_htcondor_external_submitter .
docker run --name simple_htcondor_external_submitter -itd --net host --privileged -v ~/simple_htcondor_external_submitter/sh/config:/etc/simple_grid/config -v /sys/fs/cgroup/:/sys/fs/cgroup/ simple_htcondor_external_submitter
```

## Configure the container
- Enter the container:
    ```
    docker exec -it simple_htcondor_external_submitter bash
    ```
- Run the config script:
    ```bash
    /etc/simple_grid/config/init.sh
    ```
## Submit a Job to an HTCondor CE

- Enter the container:
    ```bash
    docker exec -it simple_htcondor_external_submitter bash
    ```

- Create the submit file:

    ```bash
    su condor_user
    cd ~/sleep_job
    voms-proxy-init
    vim sleep.sub
    ```
    Add the following contents to sleep.sub and replace the {FQDN OF CE} with the fqdn of the CE where you wish to submit the job to.
    ```text
    # sleep.sub -- simple sleep job
    
    universe = grid
    executable = sleep.sh
    log = sleep.log
    output = outfile.txt
    error = errors.txt
    should_transfer_files = Yes
    when_to_transfer_output = ON_EXIT
    use_x509userproxy = true
    +WantJobRouter = true
    +TransferOutput = ""
    grid_resource = condor {FQDN OF CE} {FQDN OF CE}:9619
    queue
    ```

- Submit the job
    ```bash
    condor_submit sleep.sub
    ```
 
 - Check the job status
    ```bash
    condor_q
    ```
