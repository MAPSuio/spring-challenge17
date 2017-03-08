# Post-Vegas Woes

![vegas](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Welcome_to_Fabulous_Las_Vegas.jpg/2560px-Welcome_to_Fabulous_Las_Vegas.jpg)

Wow – what a weekend! You're not really sure what happened there, but
you (Amina) and your two friends (Pedro and Joey) have arrived
home from Vegas and the hour of judgement is upon you: As you forgot
to continuously Vipps each other during the trip, you're stuck with a
horror-inducingly long list of transactions and the burning question:
Who owes whom, and how much?

You quickly realize that you cannot simply go through every transaction
and send the corresponding money: Even though Vipps is free, you're
going to spend an awfully long time typing numbers into the app, when in
reality, only a few large transactions should be needed to settle
the balance.

It turns out that the balance can be settled with only *two* transactions.
Your job is to find the two smallest transactions that settles the balance.

## Input Format

The input consists of several lines, where each line represents a transaction.

* The first entry before the `-` shows the name of the person who paid the expense
* The second entry contains a comma-separated list of the ones who benefitted
* The third entry contains the amount

For example, the entry

```txt
Amina-Joey,Pedro,Amina,-6000
```

indicates that Amina paid 6000 for something that benefitted himself,
Joey and Pedro. A consequence is that Joey and Pedro owe Amina
one third of 6000 each.

## Answer format

Print the amounts that were sent in the two transactions in sorted
order, small to large, separated by a space, i.e. `43 55`.

## Example

```txt
Amina-Pedro,Joey-2522
Joey-Joey,Amina,Pedro-2610
Joey-Pedro-300
Pedro-Joey-1038
Joey-Pedro,Joey,Amina-2652
Joey-Joey,Amina-3784
Pedro-Pedro,Amina-1820
```
Solution: `1367 2034`
