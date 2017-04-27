# Log creater using Python.

## Download repo from github

```
  :~$ mkdir fileread && cd filereader
  :~/filereader$ 
  :~/filereader$ git clone https://github.com/maheshreddy7797/textreader

```
 #### Running Docker file

```
  $ cd textreader
  $ sudo docker build -t pyread .
  $ sudo docker run -v /path/to/text/file:/datadir pyread

example: sudo docker run -v /home/mahesh/datadir1:/datadir pyread
         sudo docker run -v /home/mahesh/datadir2:/datadir pyread
```
## From Docker hub

```
  $ sudo docker pull maheshreddy7797/pyread
  $ sudo docker run -v /path/to/text/file:/datadir maheshreddy7797/pyread
```
