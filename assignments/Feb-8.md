## SSH Practice 

Note: `directory` and `folder` are interchangeable in the following tasks.

0. You should have already shared your `public SSH key` in [this document](https://docs.google.com/document/d/1In6AP09tpR55C3jno_HZntkNrDZtqnz-KJuZMI07E5I/edit?usp=sharing).

1. SSH into the machine running at IP address `34.71.128.214`. Use the username `fedora`.
  - _hint_ $ ssh -i ~/.ssh/id_rsa fedora@34.71.128.214

2. Create a new directory using your last and first names in the folder `/home/fedora/feb-8`. Use `ls -al ~/feb-8` to view what's in the `feb-8` directory. Use yourlastname-yourfirstname as the directory name.

  - _hint_ The directory I created is /home/fedora/feb-8/omalley-sally

3. Write the output of the `date` command into a file named `<yourfirstname>-today` located in the directory you created in Step 2.

4. Run the following:

```bash
curl -o /home/fedora/feb-8/<your-named-directory>/joke.sh https://gist.githubusercontent.com/DS219/spring/9aedbaa80a92681cf271313ca29bd5aa/raw/a75f8cdf44b962eb57d25827514ad7cd323512db/dadjoke.sh
```

5. Use chmod to make it possible to run the command `/home/fedora/feb-8/<your-named-directory>/joke.sh`

6. Run the script and append the joke to the file you created in Step 3. You can copy/paste _or_ use `>>` to redirect the output of the script to the file.

**HAVE FUN and ASK QUESTIONS!!**
