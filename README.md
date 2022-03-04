# Diffie-Hellman-Merkle
Diffie–Hellman key exchange is a method of securely exchanging cryptographic keys over a public channel and was one of the first public-key protocols as conceived by Ralph Merkle and named after Whitfield Diffie and Martin Hellman.[[1]](https://dl.acm.org/doi/10.1145/359460.359473)[[2]](https://ee.stanford.edu/~hellman/publications/24.pdf)

The simplest and most original implementation of the protocol uses the [multiplicative group of integers modulo p](https://en.wikipedia.org/wiki/Multiplicative_group_of_integers_modulo_n), where p is [prime](https://en.wikipedia.org/wiki/Prime_number) and g is a [primitive root modulo p](https://en.wikipedia.org/wiki/Primitive_root_modulo_n). These two values are chosen this way to ensure that the resulting shared secret can take on any value from 1 to p–1.

In the most basic form of Diffie-Hellman key exchange, Alice and Bob start by mutually deciding two numbers to start with. These are the modulus (p) and the base (g).

In practice, the modulus (p) is a very large prime number, with at least 2048 bits, while the base (g) is relatively small to simplify calculations.

To make the process easier, let's use much smaller numbers. Here is an example of the protocol, with non-secret values in blue, and secret values in red.

<p align="center">
  <img src="https://user-images.githubusercontent.com/94197281/156836374-cc06a5f9-25b0-49de-a606-af1a257fd19a.png">
</p>

#### Security
The protocol is considered secure against eavesdroppers if G and g are chosen properly. In particular, the order of the group G must be large, particularly if the same group is used for large amounts of traffic. The eavesdropper has to solve the Diffie–Hellman problem to obtain gab. This is currently considered difficult for groups whose order is large enough. An efficient algorithm to solve the discrete logarithm problem would make it easy to compute a or b and solve the Diffie–Hellman problem, making this and many other public key cryptosystems insecure. Fields of small characteristic may be less secure.[[3]](https://hal.inria.fr/file/index/docid/909087/filename/article.pdf)

#### Name
In 2002, Hellman suggested the algorithm be called Diffie–Hellman–Merkle key exchange in recognition of Ralph Merkle's contribution to the invention of public-key cryptography (Hellman, 2002), writing:

"The system...has since become known as Diffie–Hellman key exchange. While that system was first described in a paper by Diffie and me, it is a public key distribution system, a concept developed by Merkle, and hence should be called 'Diffie–Hellman–Merkle key exchange' if names are to be associated with it. I hope this small pulpit might help in that endeavor to recognize Merkle's equal contribution to the invention of public key cryptography."[[4]](https://ee.stanford.edu/~hellman/publications/31.pdf)

# 
### References
1. [Merkle, Ralph C. (April 1978). "Secure Communications Over Insecure Channels". Communications of the ACM. 21 (4): 294–299](https://dl.acm.org/doi/10.1145/359460.359473)
2. [Diffie, Whitfield; Hellman, Martin E. (November 1976). "New Directions in Cryptography"](https://ee.stanford.edu/~hellman/publications/24.pdf)
3. [Barbulescu, Razvan; Gaudry, Pierrick; Joux, Antoine; Thomé, Emmanuel (2014). "A Heuristic Quasi-Polynomial Algorithm for Discrete Logarithm in Finite Fields of Small Characteristic". Advances in Cryptology – EUROCRYPT 2014.](https://hal.inria.fr/file/index/docid/909087/filename/article.pdf)
4. [Hellman, Martin E. (May 2002), "An overview of public key cryptography"](https://ee.stanford.edu/~hellman/publications/31.pdf)
