# Python app to read text files in the Container and local directories.


```
Download from github
  $ git clone https://github.com/maheshreddy7797/textreader

```
## Running Docker file

```
  $ cd textreader
  $ sudo docker build -t pyread .
  $ sudo docker run -v /path/to/text/file:/datadir pyread
```
# From Docker hub

```
  $ sudo docker pull maheshreddy7797/pyread
  $ sudo docker run -v /path/to/text/file:/datadir maheshreddy7797/pyread
