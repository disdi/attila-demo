:date: 2024-04-25 01:25
:author: disdi
:tags: Nlnet
:category: Nlnet
:slug: milestine-five-update
:title: Milestone 5 Update
:disqus_identifier: /2024/04/milestine-five-update.html

Automotive Protcols on Litex
============================

Universal Measurement and Calibration Protocol 
----------------------------------------------

The CAN Calibration Protocol (CCP) is an interface that enables read/write access to an Electronic Control Unit (ECU).
It enables calibration, data measurement, flashing and more.

The Universal Measurement and Calibration Protocol (XCP) is the successor to CCP with various improvements including 
support for more transport layers such as Ethernet, FlexRay and SxL.

XCP provides direct access to the inner workings of an ECU. This lets you request high-frequency parameter data that may
otherwise only be known to the ECU. Further, it also lets you modify the ECU algorithms and variables, making it easy to
test and calibrate ECUs.

The CCP/XCP protocol is based on a single-master/multi-slave concept. An external measurement & calibration tool
(e.g. a PC/device/data logger) serves as the master and is able to read/write from one or more ECUs aka slaves.

Opensource implementation of XCP is available at :
https://github.com/vectorgrp/XCPlite

To enable basic XCP on Litex, a small demo implementation is mirrored at :
https://github.com/disdi/XCPlite


As part of this milestone this is now integrated in buildroot :
https://gitlab.com/saket.sinha89/buildroot/-/commit/e75a1e270292d99e62bd656b3f162dc79caadac8


The below image shows the demo working with creating a dummy XCP Server which talks to XCP slave on Litex over localhost 
via UDP to measure variables at fixed memory address.

|Image|


.. |Image| image:: /assets/images/xcplite-demo.png
   :target: /assets/images/xcplite-demo.png