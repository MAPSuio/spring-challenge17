# Find pi in π
<img align="right" src="https://tstoaddicts.files.wordpress.com/2014/03/pi-pie.jpg" width="500px">
MAPS want to build a new computer and have serious storage needs. Sadly, FU
(Foreningsutvalget) won't provide us the sufficient funds, forcing us to do
more with less. Given our love of π and computer science, the obvious solution
to this problem is to develop a file system based on π which better fits with
our storage needs and limited funds.

π is an irrational number, thus there are an infinite number of digits in π.
In addition, π seems to be randomly distributed, informally meaning that what
digit is located in position `i` is anyone's guess. These two observations seem to
suggest that *any* finite sequence of digits can be found somewhere in π; let
us assume it is so for the rest of the day.

A file is simply a sequence of bits, and this sequence of bits is in turn just
another representation of a number, thus any file can be represented as a
decimal number. Our file system will find the decimal representation of a given
file, and simply store the length of the number (i.e. the number of digits) and
the index of which this number first occurs in π. This last bit is a bit
tricky, which is why we have left it for you to solve.

For simplicity, we will assume that all files are ASCII-encoded, and that there
is no auxiliary information that needs to be stored (i.e. no headers or any
fancy stuff). The decimal representation of an ASCII-encoded file is given by
concatenating the *binary* encoding of each ASCII-character (each of length
eight) and converting it to a decimal number.

The digits of π is indexed like so:

```
3.1415...
0 1234...
```

For instance, the number 15 occurs at index 3 in π.

The first file we want to store on our new computer is the file which only
contains `"PI"`. Your task is to provide the index in π where this file first
occurs.
