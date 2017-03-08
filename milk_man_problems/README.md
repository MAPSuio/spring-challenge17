# Milk man problems

<img align="right" src="http://folk.uio.no/torenord/milk.png" width="500px">

All milkmen are familiar with this classic problem from the Middle Ages:

You are on your daily milk delivery route. But when you get to the last
two people, you discover a major problem! Both of them require 6
liters, but you only have 12, 8 and 5 liter jugs. The 12 liter jug is
full of milk however, so if you could figure out a way of pouring from
jug to jug until you have 6 liters in two of the jugs, you'd be all
set.

The difficulty is that there are no markings on the jugs, you only
know their maximum volume. When you pour, you pour the most possible.
That is: You pour until either the jug you're pouring from is empty,
or the one you're pouring to is full.

Since you'll run into this problem everyday on your route, you have
taken the time to figure out a way to do this. You call the 12, 8 and
5 jugs A, B and C, respectively. Also, you assume A is full of milk,
and B, C are empty. Here are the steps you use:

1. Pour 8 liters from A to B.
2. Pour 5 liters from B to C.
3. Pour 5 liters from C to A.
4. Pour 3 liters from B to C.
5. Pour 8 liters from A to B.
6. Pour 2 liters from B to C.
7. Pour 5 liters from C to A.

Now you have 6 liters in A, 6 liters in B and 0 liters in C. You have
divided the milk equally and it only took 7 steps! It turns out that
it is not possible to do it with fewer steps in this case.

After solving this problem successfully, you want to help milkmen
everywhere! You have done the natural thing: You have written a
computer program.

Now you want to test it on another instance where the volumes of the
jugs are A = 500, B = 333, C = 100. A is full of milk, B, C are empty.
Your goal is to have 250 milk in A, 250 in B and 0 in C. What is the
smallest number of steps needed to accomplish this?
