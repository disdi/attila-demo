:date: 2024-04-04 14:21
:author: disdi
:tags: Nlnet
:category: Nlnet
:slug: milestone-four-complete
:title: Milestone 4 Complete
:disqus_identifier: /2024/04/milestone-four-complete.html


Bringing up Ethernet interface on Litex
=======================================

Support for CTUCAN interfaces has been extended from Arty to below FPGA boards :

Genesys2 : https://digilent.com/reference/programmable-logic/genesys-2/
commit : https://github.com/litex-hub/linux-on-litex-vexriscv/pull/378/commits/4e2d1bc537c68c8ab7b63ab31b31a27257dd8a23


Nexys A7 : https://digilent.com/reference/programmable-logic/nexys-a7/
commit : https://github.com/litex-hub/linux-on-litex-vexriscv/pull/378/commits/975064cddb70a86cf43d26888ccb749caaf26be8

All the above boards have "ethernet" available in litex project by default so bitstream need not be modified.

I added support in litex buildroot configuration file to support bringing up network interface via DHCP.

commit : https://github.com/litex-hub/linux-on-litex-vexriscv/pull/378/commits/241ffa8e6a4b3069e7a3f16b9d586160af55d406

As a result in Litex rootfs, buildroot generated /etc/network/interfaces with dhcp enabled for eth0 as shown below :

|Image1|


Bringing up Cannelloni on Litex
===============================

Cannelloni uses UDP, TCP or SCTP to transfer CAN frames between two machines not connected via CAN bus.

Repository: https://github.com/mguentner/cannelloni

Cannelloni on RPI
-----------------

We use Raspberry-Pi(RPI) to test cannelloni packet exchange with Litex as shown below :

|Image2|

The above image shows RPI using a virtual CAN interface and starting cannelloni with Litex IP as remote. 

Cannelloni on Litex
-------------------

Cannelloni is already supported in buildroot.
I added support in litex buildroot configuration file to support cannelloni on Litex.

commit : https://github.com/litex-hub/linux-on-litex-vexriscv/pull/378/commits/6a7676b3ef6d7b3c4a9c905e9fba3d0beddb69e8

As a result in Litex rootfs, cannelloni package is installed as shown below :

|Image3|


The above image shows Litex using CTUCAN interface and starting cannelloni with RPI IP as remote.
We then use can-utils(cansend and candump) to send/receive CAN packets over UDP. 

All commits are part of the Pull request to Linux on Litex Project :
https://github.com/litex-hub/linux-on-litex-vexriscv/pull/378


.. |Image1| image:: /assets/images/eth-fpga.png
   :target: /assets/images/eth-fpga.png

.. |Image2| image:: /assets/images/cannelloni-rpi.png
   :target: /assets/images/cannelloni-rpi.png

.. |Image3| image:: /assets/images/cannelloni-fpga.png
   :target: /assets/images/cannelloni-fpga.png   