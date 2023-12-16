:date: 2023-12-16 14:21
:author: disdi
:tags: Nlnet
:category: Nlnet
:slug: milestone-two-complete
:title: Milestone 2 Complete
:disqus_identifier: /2023/06/milestone-two-complete.html


This is to update on completion of Milestone 2 of the project which involved communication on the CAn bus with real CAN devices. 

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
   
   Refer : https://www.waveshare.com/sn65hvd230-can-board.htm

   can_tx and canrx are connected together with 3.3V to power the transceiver.
   Connection between FPGA board and CAN transceiver is shown below :

   |Image2| 

4. Considerable testing is done over different CAN devices to confirm CTUCAN IP is able to comunicate over CAN network.
   PCAN-USB adapter is used to emulate CAN device over development computer.

   Refer : https://www.peak-system.com/PCAN-USB.199.0.html?&L=1

   Connection between PCAN-USB adapter with DB9 connector and CAN transceiver is shown below :

   |Image3|

   For DB9 Connector pinout for CAN, refer : https://documentation.help/NI-CAN/High-Speed_CAN_Pinout_Cable.html 

5. PCAN-View is to analyze the CAN network to check for the protocal conformity and errors.

   Refer : https://www.peak-system.com/PCAN-View.242.0.html?&L=1

   |Image4|

   
The images show 01010101 sent from Litex Console is recieved in PCAN-View.
==========================================================================

.. |Image| image:: /assets/images/litex-can.png
   :target: /assets/images/litex-can.png

.. |Image2| image:: /assets/images/fpga-traceiver.jpeg
   :target: /assets/images/fpga-traceiver.jpeg   

.. |Image3| image:: /assets/images/tranciever-Pcanusb.jpeg
   :target: /assets/images/tranciever-Pcanusb.jpeg   

.. |Image4| image:: /assets/images/pcan-trace.jpeg
   :target: /assets/images/pcan-trace.jpeg