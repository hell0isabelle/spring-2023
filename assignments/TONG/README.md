# Begin the Countdown!

## Description
The executable script outputs a countdown from 10 to 1, inclusively, displaying the following output:
```
10 9 8 7 6 5 3 2 1
```

It performs 10 iterations of a for-loop. In each iteration, it prints the current value of the variable counter that represents the iteration number. The variable counter is decremented at the end of each iteration. The output is displayed in a single line. 


## Building the Container Image
We get started by installing [Podman Desktop](https://podman-desktop.io/).

Afterwards, we create a Containerfile to package the script. We set the <code>CMD</code> of the container image to call the executable file. An example of a Containerfile is displayed below.

```
FROM [--platform=<platform>] <image> [AS <name>]
WORKDIR /path/to/workdir
COPY [--chown=<user>:<group>] [--chmod=<perms>] <src>... <dest>
RUN <command>
CMD <command>
```

The <code>FROM</code> instruction initializes a new build stage and sets the Base Image for subsequent instructions.

The <code>WORKDIR</code> instruction sets the working directory for any <code>RUN</code>, <code>CMD</code>, and <code>COPY</code> instructions that follow it in the Containerfile. 

The <code>COPY</code> instruction copies new files or directories from <code>src</code> and adds them to the filesystem of the container at the path <code>dest</code>.

The <code>RUN</code> instruction will execute any commands in a new layer on top of the current image and commit the results. The resulting committed image will be used for the next step in the Containerfile.

The <code>CMD</code> instruction provides defaults for an executing container. These defaults can include an executable. When used in the shell or exec formats, the <code>CMD</code> instruction sets the command to be executed when running the image.


Followingly, we build and tag the container image, using the code format below (in the terminal):
```
podman build -t [image-name] -f [path/to/containerfile]
```

## Running the Image
After building the container image, we are able to run the image with the code format below:
```
podman run [image-name] 
```

Note that you may login to [Docker Hub](https://hub.docker.com) with podman with the code:
```
podman login docker.io
```
You will enter the username and password when prompted in the terminal.

You can push the built container image into your Docker Hub account with the code:
```
podman push [image-name] docker.io/[username]/[image-name:tag]
```
