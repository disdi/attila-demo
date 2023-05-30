:date: 2023-05-30 01:25
:author: disdi
:tags: Nlnet
:slug: milestine-one-update
:title: Milestone 1 Update
:disqus_identifier: /2023/05/milestine-one-update.html


CTUCAN Controller for Linux
===========================

We updated linux-on-litex project to integrate CTUCAN Controller booting over Linux.

The link to the code is available at below link - 
https://github.com/disdi/linux-on-litex-vexriscv/commit/e9f9c6b14bca11cca2195bd61f9c5334ead3221d

When Litex BIOS boots up, it shows all the peripherals needed to boot linux alongwith CTUCAN Controller in the memory region.
The screenshoot below of Litex Console:

|Image|

Next step is to modify linux kernel booting over the litex bitstream with CTUCAN Controller to enumerate a CAN device.


.. |Image| image:: /assets/images/litex-linux.png
   :target: /assets/images/litex-linux.png
