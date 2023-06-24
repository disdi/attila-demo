:date: 2023-06-08 14:21
:author: disdi
:tags: Nlnet
:slug: milestone-one-complete
:title: Milestone 1 Complete
:disqus_identifier: /2023/06/milestone-one-complete.html


CTUCAN Controller for Linux
===========================

We updated linux-on-litex kernel config to enable CTUCAN linux driver.

The screenshoot below shows the menuconfig to enable CTUCAN driver:

|Image|

Next we had to update the device tree manually to add a section for CTUCAN driver:

CTU_CAN_FD_0: CTU_CAN_FD@80010000 {
    compatible = "ctu,ctucanfd";
    reg = <0x80010000 0x10000>;
    interrupt-parent = <&intc0>;
    interrupts = <0 30 4>;
    clocks = <&sys_clk>;
    status = "okay";
    };

The link to the complete modified device-tree is available at below link - 
https://github.com/disdi/linux-on-litex-vexriscv/commit/64970aea0ce4dfb10d16ffeece8837b032a702d4

When Linux  boots up, it shows the CTUCAN linux driver getting initialized.

|Image2|

In the buildroot Image booting up we can clearly see the CTUCAN driver module is associated with a device:

|Image3|

Further, it gets enumerated as a network device:

|Image4|

Next step is to connect Digilent Arty Board running CTUCAN IP core with an external MCP2551 CAN transceiver Board and attempt
CAN transmission to another device on this CAN Bus.

.. |Image| image:: /assets/images/ctucan-config.png
   :target: /assets/images/ctucan-config.png

.. |Image2| image:: /assets/images/ctucan-linux-boot.png
   :target: /assets/images/ctucan-linux-boot.png   

.. |Image3| image:: /assets/images/ctucan-buildroot.png
   :target: /assets/images/ctucan-buildroot.png   

.. |Image4| image:: /assets/images/ctucan-net.png
   :target: /assets/images/ctucan-net.png