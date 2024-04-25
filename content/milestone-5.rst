:date: 2024-04-24 01:25
:author: disdi
:tags: Nlnet
:category: Nlnet
:slug: milestine-five
:title: Milestone 5
:disqus_identifier: /2024/04/milestine-five.html


Automotive Protcols on Litex
============================

Unified Diagnostic Services
---------------------------

Unified Diagnostic Services (UDS) is a communication protocol used in automotive Electronic Control Units (ECUs) to 
enable diagnostics, firmware updates, routine testing and more.

UDS communication is performed in a client-server relationship - 

- client being a tester-tool 
- server being a vehicle ECU

The UDS protocol (ISO 14229) is supported on both  CAN and Ethernet.It describes the application layer requirements for 
UDS (independent of what lower layer protocol is used).
Opensource implementation on CAN is available at:

https://pypi.org/project/udsoncan/


The standard which specifies a transport protocol and network layer services for use in CAN based vehicle networks is 
CAN ISO-TP - Transport Protocol (ISO 15765).
Opensource implementation is available at:

https://pypi.org/project/can-isotp/


DoIP(Diagnostics over Internet Protocol) is a standardized diagnostic transport protocol according to ISO 13400. 
It encapsulates diagnostics messages of protocol standards like Unified Diagnostic Services (UDS) over Ethernet.
Opensource implementation is available at:

https://pypi.org/project/doipclient/


As part of this milestone, integration of the above Opensource projects to buildroot is compelted so that it is available on Linux on Litex.
The link to the integration effort in buildroot project is available at below link - 

https://gitlab.com/saket.sinha89/buildroot

Once these python packages are added to buildroot project, the buildroot configuration can be updated with below options:

|Image1|

The screenshoot below shows these packages working on buildroot rootfs of Litex Console:

|Image|




.. |Image| image:: /assets/images/uds-buildroot.png
   :target: /assets/images/uds-buildroot.
   
.. |Image1| image:: /assets/images/uds-config.png
   :target: /assets/images/uds-config.png
