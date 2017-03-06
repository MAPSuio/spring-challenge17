# Post-Vegas Woes

![vegas](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Welcome_to_Fabulous_Las_Vegas.jpg/2560px-Welcome_to_Fabulous_Las_Vegas.jpg)

Wow – what a weekend! You're not really sure what happened there, but
you (Pedro) and your three friends (Alex, Amin and Joey) have arrived
home from Vegas and the hour of judgement is upon you: As you forgot
to continuously Vipps each other during the trip, you're stuck with a
horror-inducingly long list of transactions and the burning question:
Who owes whom, and how much?

You quickly realize that you cannot simply go through every transaction
and send the corresponding money: Even though Vipps is free, you're
going to spend an awfully long time typing numbers into the app, when in
reality, only a few large transactions should be needed to settle
the balance.

*Your task is to simplify the list of 10 000 transactions down to twelve
(or fewer) transactions*

## Input Format

The input consists of several lines, where each line represents a transaction.

* The first entry before the `-` shows the name of the person who paid the expense
* The second entry contains a comma-separated list of the ones who benefitted
* The third entry contains the amount

For example, the entry

```txt
Amin-Joey,Alex,Amin,Pedro-5000
```

indicates that Amin paid 5000 for something that benefitted himself,
Joey, Alex and Pedro. A consequence is that Joey, Alex and Pedro owes Amin
one fourth of 5000 each.

## Answer Format

You need to submit 12 space-separated integers. Each integer represent
the amount that X sends to Y, where X and Y are the names in sorted
order:

1. Alex sends to Amin
2. Alex sends to Joey
3. Alex sends to Pedro
4. Amin sends to Alex
5. Amin sends to Joey
6. Amin sends to Pedro
7. Joey sends to Alex
8. Joey sends to Amin
9. Joey sends to Pedro
10. Pedro sends to Alex
11. Pedro sends to Amin
12. Pedro sends to Joey

## Example

```txt
Amin-Pedro,Amin,Alex,Joey-7776
Alex-Joey,Amin,Pedro-4965
Joey-Pedro,Alex-2004
Pedro-Joey-1176
Alex-Pedro,Amin,Joey,Alex-3204
Amin-Alex-1044
Pedro-Joey,Amin,Alex,Pedro-2044
```

Answer: `532 0 0 0 0 0 1454 1944 685 1945 1433 0`

Note that the one who pays is not necessarily benefitting from that which is bought.