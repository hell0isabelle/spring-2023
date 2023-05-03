## Install podman dekstop on your laptop

Head to https://podman-desktop.io/ to download and install podman desktop. Follow the documentation at https://podman-desktop.io/docs/intro to get started.

Once podman machine has been started, you can use the GUI or follow the commands below to do it in your terminal as well.

## Create a Containerfile

Head to the directory you created under `assignments/[LASTNAME]` and add your Containerfile there.

Checkout a new branch
```
git checkout -b [new-branch] upstream/main
```

Create a Containerfile to package the script you wrote in the February 22nd assignment. Set the CMD of your container image to call your executable file.

```
...
CMD ./path/to/your/executable
...
```

This is what an example Containerfile looks like
```
FROM alpine
WORKDIR mydir
ADD joke.sh /mydir
RUN chmod +x /mydir/joke.sh
RUN apk add curl
CMD ./joke.sh
```
Head to https://docs.docker.com/get-started/02_our_app/ for a quick tutorial on Containerfiles/Dockerfiles. Google is your friend, use it!

## Build and tag your container image

```
$ podman build -t [image-name] -f [path/to/containerfile]
```

## Create a free account on Docker hub

Head to Docker hub (https://hub.docker.com/) and create a free account there. Make sure to remember your username and password!

## Push the built container image to your docker hub account

Login to the docker hub account you created above with podman and enter the username and password when prompted.
```
$ podman login docker.io
```

Now you can push the image you built to your docker hub account.
```
$ podman push [image-name] docker.io/[username]/[image-name]
```

Add a link to your container image to this doc https://docs.google.com/document/d/1fKh-2BkDilRNhH_bgAzQsNx1NF8_1TUJPC5M3EFyg8M/edit?usp=sharing

Make sure to run your container image with podman to ensure it runs successfully!
```
podman run [image-name]
```

## Run a classmate's container image locally

Look through the doc above and pick a container image that one of your classmate's built. Pull it down and run it locally on your machine.

```
$ podman pull [classmate-image]
$ podman run [classmate-image]
```

Answer the questions in this form https://forms.gle/pqEwui9Q7wmLQhrX8 and hit submit!
