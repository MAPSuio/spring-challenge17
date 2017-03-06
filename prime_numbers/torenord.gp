/* Usage: gp torenord.gp */

S = 0;
n = 10^16;
for (i = 1, 10^6, n = nextprime(n + 1); S += n);

printf("%d\n", S);
