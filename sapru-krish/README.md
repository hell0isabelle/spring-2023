## Introduction
This markdown file provides instructions on how to build and run a container image that contains a simple shell script to download and print a joke from the public site "https://icanhazdadjoke.com".

## Prerequisites
Before proceeding, you need to have Docker installed on your machine. If you haven't installed Docker yet, please follow the installation guide for your platform from the official Docker website https://docs.docker.com/get-docker/.

## Getting the Code
To get started, clone the Git repository that contains the joke shell script:
 
git clone https://github.com/ksapru/spring-2023
Alternatively, you can download the script directly from the repository page on GitHub https://github.com/ksapru/spring-2023.

Building the Container Image
Once you have the joke script, navigate to the folder that contains the script in your terminal or command prompt.

Next, create a Dockerfile with the following contents:


## dockerfile

FROM alpine
WORKDIR mydir
ADD joke.sh /mydir
RUN chmod +x /mydir/joke.sh
RUN apk add curl
CMD ./joke.sh
This Dockerfile uses the latest version of Alpine Linux as the base image, installs curl, copies the joke script to the appropriate location, and sets the command to run the joke script when the container starts.

Save the Dockerfile and build the container image by running the following command from the folder that contains the Dockerfile and joke script:

docker build -t my-joke .
This command builds an image with the name "my-joke" using the Dockerfile and the joke script in the current folder. The dot at the end of the command specifies the build context, which is the current folder.

## Running the Container Image
Once the container image is built, you can run it using the following command:

docker run my-joke

This command starts a container from the "my-joke" image and runs the joke script inside the container. The output should display a random joke from "https://icanhazdadjoke.com".

