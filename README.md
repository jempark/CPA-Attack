# Correlation Power Analysis Attack 
## Overview
Implemented a correlation power analysis (CPA) attack and recovered a full round key used in an AES encryption process. We are provided with a set of power traces of the 128-bit AES core running on an FPGA board already acquired in the NUEESS lab (http://tescase.coe.neu.edu/) of Northeastern
University. We will need to utilize a leakage point to perform a correlation power analysis and recover the full round key.

## Data Set
We have a set of 7000 power traces of an unmasked AES running on an FPGA board (SAKURA-GII). As we are attacking the last round, we will need to use cipher 7000.txt and trace 7000.txt files for this. Each row of both files is for one encryption, which consists of one 16-byte ciphertext and one 3125-point power trace, respectively. We will first generate a plot of one power trace in the data set. 

## Correlation Power Analysis with Hamming Distance Power Model

We will need to use the Hamming Distance (HD) power model to recover all 16 AES key bytes. With the correct key byte value, the HD model yields the strongest correlation with power values at time point 2663 (the HD Leakage Point).

*Organization of AES State*: The 128-bit AES, has ten rounds and eleven states, where each state is 16-byte. Its index is increasing vertically within columns.

*Hamming distance power model*: We attack the last round of AES and use the Hamming distance power model for each byte. Assume the input state for the last round is S and the output state is the ciphertext
C, and the relationship between them is cj = sbox[si] ⊕ kj due to the ShiftRow operation, i.e., si = inv sbox[cj ⊕ kj ] , with the mapping between the input state index i and output state index j.

So the HD power model for each byte will be HD(si, ci) = HD(inv sbox[cj ⊕ kj ], ci). With each key byte guess value, using this HD model to correlate with power values at the leakage point. The correct key
byte value should be the one with the strongest correlation.