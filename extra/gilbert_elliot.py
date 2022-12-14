import math
import random
import matplotlib.pyplot as plt
import numpy as np

# Set environment
E = "e3"

# Initialize model parameters for E1
if E == "e1":
    p_G = 0.1 * (10 ** (-35))        # Probability of good state
    p_B = 0.000197264442772      # Probability of bad state
    p_p = 0.0000132518942   # Probability of state transition from good to bad
    p_r = 0.00000921436463  # Probability of state transition from bad to good

# Initialize model parameters for E2
elif E == "e2":
    p_G = 5.0 * (10 ** (-4))        # Probability of good state
    p_B = 1.0 * (10 ** (-2))      # Probability of bad state
    p_p = 4.0 * (10 ** (-3))   # Probability of state transition from good to bad
    p_r = 6.0 * (10 ** (-3))  # Probability of state transition from bad to good

# Initialize model parameters for E3
elif E == "e3":
    p_G = 1.0 * (10 ** (-3))        # Probability of good state
    p_B = 1.0 * (10 ** (-1))      # Probability of bad state
    p_p = 1.0 * (10 ** (-2))   # Probability of state transition from good to bad
    p_r = 1.0 * (10 ** (-3))  # Probability of state transition from bad to good

# Initialize state
# Good state : "g"
# Bad state  : "b"
state = "G"

# Initialize packet size and counts
bit_count = 0
packet_size = 265
packet_count = 0
packet_errors = 0
packet_retransmissions = 0
packet_list = []

# Initialize number of steps to simulate
steps = 0
bits = 500000

# Initialize number of errors to 0
errors = 0

# Simulate transmissions
while steps < bits:

    # If state is good, determine if it transitions to bad
    if state == "G":
        if random.random() < p_p:
            state = "B"
    # If state is bad, determine if it transitions to good
    elif state == "B":
        if random.random() < p_r:
            state = "G"

    # Error
    if state == "B":
        if random.random() < p_B:
            errors += 1
            packet_errors += 1
    elif state == "G":
        if random.random() < p_G:
            errors += 1
            packet_errors += 1

    # Count packets
    if bit_count == packet_size:

        # Re-transmit if there's more than 2 bit errors in packet
        if packet_errors >= 2:
            packet_retransmissions += 1
            steps -= packet_size

        # Add packet errors to packet list
        packet_list.append(packet_errors)
        packet_count += 1

        # Reset counts
        packet_errors = 0
        bit_count = 0

    bit_count += 1
    steps += 1

# Print packets
print(f"Packets transmitted: {packet_count}")
# Print packets retransmitted:
print(f"Packets re-transmitted: {packet_retransmissions}")
# Print packets retransmitted:
print(f"Transmission success rate: {packet_count/packet_retransmissions}")

# Print packets
print(f"Packets with errors = 0: {packet_list.count(0)}")
print(f"Packets with errors = 1: {packet_list.count(1)}")
print(f"Packets with errors >= 2: {len([x for x in packet_list if x >= 2])}")

# Print bits transmitted
print(f"Bits transmitted: {bits-errors}/{bits}")
# Print total errors and transmissions
print(f"Errors/packets: {errors}/{bits}")
# Print the error rate
print(f"Error rate: {errors / bits:.6f}")