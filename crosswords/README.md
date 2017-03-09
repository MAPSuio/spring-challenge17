#Crossword helper

<img src="http://i4.irishmirror.ie/incoming/article2813250.ece/ALTERNATES/s615/cryptic-crossword-img.jpg" align="right" style="width: 250px; margin: 10px;">

Sean loves solving crosswords, but he wants to boost his crossword-solving speed.
He wants to create a dictionary of common words which can help him when solving
crosswords. However, a normal dictionary is not good enough for Sean, as he wants
to be able to look up words by length first. More specifically, a word `s` should
come before another word `t` in Sean's dictionary if either the length of `s` is less than the length of `t` or the length of `s` is the same as the length of `t`, but `s` would come before `t` in a normal dictionary. Can you help Sean with creating this dictionary?

####Your task
Given a [file](https://gist.githubusercontent.com/arnet95/e4526120a65f952a5865cfb92549af4d/raw/f064bb2c4a0fa0699c20d7614149e789d0186d18/crosswords_data.txt) consisting of common dictionary words, sort them
in increasing order (where the order here is the order defined above). Give your answer as a string `s`, where `s` is the 10000th word in the sorted list.
(For clarification, the first word is the 1st word, not the 0th word)

####Example
If the file consists of
```
aardvark
beehive
natural
computer
```
the sorted list should be
```
beehive
natural
aardvark
computer
```
and the 4th number in this list would be `computer`.
