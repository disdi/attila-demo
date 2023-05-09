---
layout: post
title: Milestone 1
author: Saket Sinha
date: 2023-05-09 21:43:12.000000000 +02:00
category: Update
tags: Nlnet
context: post
---
This is to update on the first milestone that is archeived in Libre Car Control project.


- FPGA board boots up Linux using linux-on-litex-vexriscv.

    - Replacing ECP5 with Artix7

We switched from Lattice ECP5 to Xillinx Artix7 FPGA since we found that yosys toolchain was not able to synthesize
vhdl code. The project is now being develop on Digilent Artix7 board.
We are able to boot Linux on Artix7 from the official Litex repository since this board is officially supported.


- CTUCAN Controller IP in integrated in Litex.

    - CTUCAN controller Litex Integration

We generated VHDL code for CTUCAN controller and used the CTUCAN wrapper to integrate it in Litex ecosystem. It became
available as python egg in the development environment.

    - Litex SOC with CTUCAN Controller

We created a new Litex Core with CTUCAN controller and mapped it to the processor. When Litex BIOS boots up, CTUCAN
controller can be seen in the memory region.