#!/bin/bash

# Get the default gateway IP address
DEFAULT_GATEWAY=$(sudo ip route | grep default | awk '{print $3}')

echo "Default Gateway IP: $DEFAULT_GATEWAY"
