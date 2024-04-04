:date: 2024-03-17 14:21
:author: disdi
:tags: Nlnet
:category: Nlnet
:slug: milestone-three-complete
:title: Milestone 3 Complete
:disqus_identifier: /2024/03/milestone-three-complete.html

Controlling BLDC Motor for Vehicle with CTUCAN
==============================================

This is to update on completion of Milestone 3 of the project which involved controlling a motor on the CAN network with CTUCAN device.
We would need to have a motor contoller to interface with our CAN bus and control the motor.

The ODrive is a motor control board based on the STM32 microcontroller. 
It can  be used with BLDC motors (brushless DC motors), over a CAN bus to set acceleration, braking, and other parameters
for motor control systems.  

Hardware for ODrive is available for sale on online shop:
https://odriverobotics.com/shop

The entire firware and GUI software to interface with Odrive is available on GitHub:
https://github.com/odriverobotics/ODrive/


|Image8|



Hardware Requirements
---------------------


1. A brushless motor.

2. Odrive S1

3. FPGA device with CAN controller/transceiver

4. A >12V power supply or battery.


Hardware Connections
--------------------

- Connect screw terminals representing the motor phases to A/B/C of Odrive S1 Power Pads.

- Connect the power supply cables to Odrive S1 solder pads that are labelled +/- and Arty A7 board 

Since CAN bus is not isolated, use power supply to power both. To run Arty A7 board with same DC source, below accesories can be used :

- DC-DC convertor : https://amzn.eu/d/iUmVObb

|Image|

- DC Hollow Connector :  https://amzn.eu/d/gej5q8E 

|Image1|


- Connect Odrive S1 with FPGA board over CAN bus.

- Connect motor to Odrive S1 via 3 phase wire.

Complete setup can be illustrated in below daigram

|Image6|


In reality, it resemebles like seen in below image:

|Image2|


Controlling Motor Controller with CAN bus
-----------------------------------------

- Power up Arty board with CTUCAN driver enabled

|Image4|


- Use GUI Wizard of Odrive to calibrate the motor.

|Image3|


- Check if any data is recevied on CAN bus with `candump`

|Image7|

To make sense of this data we would use CAN Simple protocol provided by Odrive.

https://github.com/odriverobotics/ODriveResources/blob/master/examples/can_simple.py

Motor should start rotating with torque of 1 turns per second.

|Image5|


.. |Image| image:: /assets/images/dc-dc.png
   :target: /assets/images/dc-dc.png

.. |Image1| image:: /assets/images/dc-connector.jpg
   :target: /assets/images/dc-connector.jpg

.. |Image2| image:: /assets/images/whole-setup.jpeg
   :target: /assets/images/whole-setup.jpeg

.. |Image3| image:: /assets/images/calibrate.png
   :target: /assets/images/calibrate.png   

.. |Image4| image:: /assets/images/ctucan-net.png
   :target: /assets/images/ctucan-net.png  

.. |Image5| image:: /assets/images/can-simple.png
   :target: /assets/images/can-simple.png   

.. |Image6| image:: /assets/images/setup.png
   :target: /assets/images/setup.png   

.. |Image7| image:: /assets/images/candump.png
   :target: /assets/images/candump.png      

.. |Image8| image:: /assets/images/s1.jpg
   :target: /assets/images/s1.jpg      