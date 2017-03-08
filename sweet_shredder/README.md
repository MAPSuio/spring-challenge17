# Sweet Shredder

Your name is Mary and you work at the biggest lawfirm in town as a
secretary. Unfortunately, there is not much to do and you are extremly
bored. You have therefore spent your last two weeks creating a
beautiful ASCII piece of art inspired by your sweetest client.

Sally-Anne is your enemy. One day, she took your beautiful art and
shredded it to pieces. You were devestated. Then she picked up the
pieces and shedded them again!

Luckily though, you have managed to collect the scraps in the correct
order from left to right, top to bottom. Each strip consists of 5
pixels and can be found below. The original artwork was 200 pixels
wide and 200 pixel tall. So you know that there will be 40 strips on
each row. From the top the 41th strip is the first five pixels of the
second row.

Your task: Reassemble the artwork and find the name of your sweetest
client.

```
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
.....
.....
.....
.....
....0
00000
00000
0....
.....
.....
.....
.....
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00...
.....
.....
...00
00000
00000
00000
00000
00000
00000
00...
.....
.....
...00
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
0000.
.....
.....
.0000
00000
00000
00000
00000
00000
00000
00000
00000
0000.
.....
.....
.0000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
0....
.....
..000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
000..
.....
....0
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
000..
.....
...00
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00...
.....
..000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
.....
....0
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
0....
.....
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
000..
.....
.0000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
0000.
.....
..000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
0....
....0
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
0....
....0
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
0000.
.....
.0000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
0000.
.....
.0000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00...
....0
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
0....
...00
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
.....
..000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
000..
.....
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
000..
.....
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
.....
..000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00...
...00
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00...
...00
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
.....
..000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
000..
.....
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
0000.
.....
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
.....
.0000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00...
....0
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
0....
...00
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
0....
..000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00...
....0
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
.....
.0000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
0000.
.....
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
0000.
.....
..000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
0000.
.....
.....
....0
00000
00000
00000
00000
00000
.....
.0000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
000..
.....
.....
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
000..
.....
.....
.....
.....
.....
.....
.....
....0
00000
00000
00000
0....
..000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00...
.....
.....
.....
00000
00000
00000
00000
00000
00000
00000
00000
00...
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
00000
00000
00...
...00
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
0....
.....
.....
.....
.....
..000
00000
00000
00000
00000
000..
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
00000
000..
....0
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
0....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
....0
000..
....0
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
0000.
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.0000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
0000.
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.0000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
000..
....0
00000
00000
00000
00000
00...
.....
00000
00000
00000
00000
00000
..000
00000
00000
00000
0000.
.....
.....
..000
00000
00000
00000
0....
....0
00000
0000.
.....
..000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
000..
....0
77777
77777
77777
77700
00000
.....
07777
77777
77777
77777
77770
..077
77777
77777
77777
00000
000..
....0
00007
77777
77777
77770
000..
....0
77777
7770.
.....
..000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
000..
....0
77777
77777
77777
77777
77770
00...
07777
77777
77777
77777
77770
..077
77777
77777
77777
77777
70000
...00
77777
77000
00000
77777
77000
....0
77777
7770.
.....
..000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00...
....0
77777
77700
00000
00777
77777
700..
07777
77770
00000
00000
00000
..077
77777
70000
00000
77777
77770
..007
77777
70000
00000
00777
77770
0...0
77777
7770.
.....
...00
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00...
....0
77777
77700
00000
00007
77777
7700.
07777
77770
00000
00000
0000.
..077
77777
70000
00000
00777
77777
00077
77777
70...
.....
.0777
77777
0...0
77777
7770.
.....
...00
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00...
....0
77777
7770.
.....
...00
77777
7770.
07777
77770
.....
.....
.....
..077
77777
70...
.....
.0777
77777
00777
77777
7000.
.....
.0000
00000
0...0
77777
7770.
.....
...00
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00...
....0
77777
7770.
.....
...00
77777
7770.
07777
77770
00000
00000
00000
..077
77777
70...
.....
.0777
77777
0.077
77777
77000
00000
000..
.....
....0
77777
7770.
.....
...00
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00...
....0
77777
7770.
.....
00007
77777
7700.
07777
77777
77777
77777
77770
..077
77777
70...
...00
00777
77777
0.007
77777
77777
77777
00000
000..
....0
77777
7770.
.....
...00
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00...
....0
77777
77700
00000
00077
77777
700..
07777
77777
77777
77777
77770
..077
77777
70000
00000
77777
77770
0..00
07777
77777
77777
77777
77000
....0
77777
7770.
.....
...00
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00...
....0
77777
77777
77777
77777
77770
00...
07777
77770
00000
00000
00000
..077
77777
77777
77777
77777
77000
.....
00000
00077
77777
77777
77770
00..0
77777
7770.
.....
...00
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00...
....0
77777
77777
77777
77770
00000
0....
07777
77770
00000
00000
0000.
..077
77777
77777
77777
77000
000..
.....
....0
00000
00000
07777
77777
70..0
77777
7770.
.....
...00
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00...
....0
77777
77700
00000
00000
00...
.....
07777
77770
.....
.....
.....
..077
77777
70000
00000
00000
.....
.0000
00000
.....
....0
00077
77777
70..0
77777
7770.
.....
...00
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00...
....0
77777
7770.
.....
.....
.....
.....
07777
77770
.....
.....
.....
..077
77777
70...
.....
.....
.....
.0000
00000
0....
.....
..077
77777
70..0
77777
7770.
.....
...00
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00...
....0
77777
7770.
.....
.....
.....
.....
07777
77770
00000
00000
00000
..077
77777
70...
.....
.....
.....
.0077
77777
000..
.....
00077
77777
00..0
77777
7770.
.....
...00
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
000..
....0
77777
7770.
.....
.....
.....
.....
07777
77777
77777
77777
77770
..077
77777
70...
.....
.....
.....
..007
77777
70000
00000
00777
77700
0...0
77777
7770.
.....
..000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
000..
....0
77777
7770.
.....
.....
.....
.....
07777
77777
77777
77777
77770
..077
77777
70...
.....
.....
.....
...00
00777
77777
77777
77777
00000
....0
77777
7770.
.....
..000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
000..
....0
00000
0000.
.....
.....
.....
.....
00000
00000
00000
00000
00000
..000
00000
00...
.....
.....
.....
.....
00000
00000
00000
00000
00...
....0
00000
0000.
.....
..000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
0000.
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.0000
00000
0....
.....
.....
.....
.....
.....
.0000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
0000.
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.0000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
0....
..000
0....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
....0
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
0....
..000
00000
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
..000
00000
00000
00000
00000
000..
.....
.....
.....
.....
....0
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00...
...00
77700
00000
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
.....
...00
00000
00000
07777
77777
77777
77770
00000
00000
.....
.....
.....
...00
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
000..
....0
07777
77700
00000
0....
.....
.....
.....
.....
.....
.....
.....
..000
00000
00000
07777
77777
77777
77777
77777
77777
77777
77700
00000
.....
.....
..000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
0000.
.....
00777
77777
77700
00000
00000
0....
.....
.....
00000
00000
00000
00000
07777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77700
000..
.....
.0000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
.....
.0077
77777
77777
77777
77000
00000
00000
00000
00000
00777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
770..
.....
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
0....
..000
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
00...
....0
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00...
....0
07777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77770
0....
...00
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
0000.
.....
00077
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77000
.....
.0000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
.....
..007
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
700..
.....
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00...
...00
07777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77770
00...
...00
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
000..
.....
00077
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77000
.....
..000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
.....
..000
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
000..
.....
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00...
....0
00777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77700
0....
...00
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
000..
.....
.0000
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
0000.
.....
.0000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
0....
....0
00777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77700
0....
....0
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
000..
.....
.0000
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
0000.
.....
..000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
.....
....0
00007
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
70000
0....
.....
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
000..
.....
...00
00077
77777
77777
77777
77777
77777
77777
77777
77777
77777
77777
77000
00...
.....
..000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
0....
.....
..000
00777
77777
77777
77777
77777
77777
77777
77777
77777
77700
000..
.....
....0
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
0000.
.....
.....
.0000
00077
77777
77777
77777
77777
77777
77777
77000
0000.
.....
.....
.0000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00...
.....
.....
..000
00000
00077
77777
77777
77000
00000
000..
.....
.....
...00
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
.....
.....
.....
.....
...00
00000
00000
00...
.....
.....
.....
.....
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
00000
```