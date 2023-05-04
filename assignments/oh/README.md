## Describe the script you wrote in the February 22nd assignment.

The random_jokes.py prints randome jokes from the list using python random libraries.

The jokes are inputed manually in a list called jokes.

## Describe how to build the container image.

You can use podman.

If your docker file is inside the directory you are in, you can run the following.

If not, then you will have to add extra path before like path/Dockerfile .

```bash
podman build -t ocmosk/dsassignment -f Dockerfile .

```

## Describe how to run the image.

After building the images, you can run the image running command below.

```bash
podman run ocmosk/dsassignment

```
