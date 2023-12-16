:date: 2023-12-16 14:21
:author: disdi
:tags: Nlnet
:category: Nlnet
:slug: milestone-two-complete
:title: Milestone 2 Complete
:disqus_identifier: /2023/06/milestone-two-complete.html


This is to update on completion of Milestone 2 of the project which involved communication on the CAN network with real CAN devices.

The major work done in this Milestone involved :

1. Bring UP the CTUCAN device enumerated in first Milestone. 
   Update of Litex interfaces was needed to make CAN interface UP and running.

   Refer : https://github.com/disdi/linux-on-litex-vexriscv/commit/b4c7c81e48d285977055b19cb08069af642ff516

2. Use ip utilites of linux which treats CAN as network device and make it up.
   Support was added to buildroot to include needed utilities for CAN and make it part of bootup script.

   Refer : https://github.com/disdi/linux-on-litex-vexriscv/commit/64ecd04d2eefc14753181dbf8a1bc65d09c65991

   Below image shows CAN bus coming up on system restart and can-utils is used for communication over CAN network :

   |Image|

3. Now when CAN IP is up, we needed a CAN transceiver to connect to CAN network. SN65HVD230 CAN Board is used for this purpose.

   |Image6|
   
   Refer : https://www.waveshare.com/sn65hvd230-can-board.htm

   can_tx and canrx are are mapped to ck_io pins exposed on J4 of Arty Board.
   https://github.com/disdi/linux-on-litex-vexriscv/blob/master/soc_linux.py#L34

   They are connected to CAN RX and CAN TX of transceiver with 3.3V to power it. Connection between FPGA board and CAN transceiver is shown below :

   |Image2| 

4. Considerable testing is done over different CAN devices to confirm CTUCAN IP is able to comunicate over CAN network.
   PCAN-USB adapter is used to emulate CAN device over development computer.

   Refer : https://www.peak-system.com/PCAN-USB.199.0.html?&L=1

   Connection between PCAN-USB adapter with DB9 connector and CAN transceiver is shown below :

   |Image3|

   CANH and CANL of transceiver is attached to (pin2 and pin7) DB9 connector. For DB9 Connector pinout for CAN, refer : https://documentation.help/NI-CAN/High-Speed_CAN_Pinout_Cable.html

5. PCAN-View software run on development computer is to analyze the CAN network to check for the protocal conformity and errors.

   Refer : https://www.peak-system.com/PCAN-View.242.0.html?&L=1

   |Image4|

   
TestBench Setup
===============

   |Image5|


The testbench results can be seen by referencing Section 2 where 01010101 sent from Litex Console is recieved in PCAN-View In Section 5.


.. |Image| image:: /assets/images/litex-can.png
   :target: /assets/images/litex-can.png

.. |Image2| image:: /assets/images/fpga-traceiver.jpeg
   :target: /assets/images/fpga-traceiver.jpeg   

.. |Image3| image:: /assets/images/tranciever-Pcanusb.jpeg
   :target: /assets/images/tranciever-Pcanusb.jpeg   

.. |Image4| image:: /assets/images/pcan-trace.jpeg
   :target: /assets/images/pcan-trace.jpeg

.. |Image5| image:: /assets/images/can_testbench.png
   :target: /assets/images/can_testbench.png

.. |Image6| image:: /assets/images/SN65HVD230-CAN-Board-2.jpg
   :target: /assets/images/SN65HVD230-CAN-Board-2.jpg