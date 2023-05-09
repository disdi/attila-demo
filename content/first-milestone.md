--
layout: post
title: First Milestone
author: Saket Sinha
date: 2023-05-09 08:43:12.000000000 +02:00
category: Update
tags: Nlnet
context: post
---
This is to update on the first milestone that is archeived in Libre Car Control project.


1. ECP5 based FPGA board boots up Linux using linux-on-litex-vexriscv.
2. CTUCAN Controller IP in integrated in Litex. (€ 1500)
+  CTUCAN controller compiles with Litex build environment.
+  CTUCAN controller is mapped to vexriscv core.
+  Litex BIOS booting up on ECP5 based FPGA board shows CTUCAN IP memory
regions/CSRs at bootup.
3. CTUCAN Controller Device Driver Bringup (€ 1500)
+  ECP5 based FPGA board boots up a custom SOC with Linux on Litex vexriscv with
CTUCAN controller IP.
+  With insmod command opensource ctucan driver is inserted in Linux kernel, CAN
Device in enumerated.