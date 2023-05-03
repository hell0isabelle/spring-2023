## Fork and clone PacMan repository

```
# first, fork https://github.com/jduimovich/mongo-pacman.git

cd /your/git/repos
git clone git@github.com:yourname/mongo-pacman.git
cd mongo-pacman
```

## Check out a new branch

```bash
git checkout -b [new-branch]
```

## The folder/directory you'll be working from is frontend

We'll roughly follow the [README.md](https://github.com/jduimovich/mongo-pacman/tree/main/frontend)
for the program's frontend.


## Build & Run PacMan

Use the commands and submit the form listed below.
If you forget to add the `it` flags to the run command, it will be tricky to stop the container.
If this happens, open another terminal and run `podman stop --all`

```
cd frontend
podman build -t docker.io/yourname/pacman:latest -f ./docker/Dockerfile .
podman run --rm -it -p 8080:8000 docker.io/yourname/pacman:latest
```

Fill out this [Google Form](https://forms.gle/gaZLPbik3w6sNiW57) with the answers to the following
1. Notice the `LICENSE`. You'll have to go back to the [original repository](https://github.com/font/pacman). Do you have permission to use this code as you wish?
2. Try to run the program locally. The README describes how to do this. Were you successful?
3. Look at the Dockerfile (hint: it's in `docker/Dockerfile`). Do you understand what it's doing?
4. Build an image and push it to your Docker repository. List your image on the form.
5. Run your image. Does it work? What command did you use to run the image?

* `EXTRA CREDIT`: Make a change (any change!) that is visible when the program is run. Build and push that image.
* `EXTRA EXTRA CREDIT`: Configure the mongo database to keep records of games played with best scores. Explain how you did it.

You can use Podman, Docker, or any other container build tool.
