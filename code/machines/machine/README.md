Machine Features and Dependencies
---

# scripts


```
sh python-libs.sh
```


```
sh machine-features.sh
```





# terminal output

## python-libs

```
$ sudo pip install Pillow #[1][2][3]
The directory '/home/map479/.cache/pip/http' or its parent directory is not owned by the current user and the cache has been disabled. Please check the permissions and owner of that directory. If executing pip with sudo, you may want sudo's -H flag.
The directory '/home/map479/.cache/pip' or its parent directory is not owned by the current user and caching wheels has been disabled. check the permissions and owner of that directory. If executing pip with sudo, you may want sudo's -H flag.
Collecting Pillow
  Downloading https://files.pythonhosted.org/packages/2a/9b/96c45009d405cc11c7bc0c73e6bcef8cc4e9c995568773753527be41ed13/Pillow-5.3.0-cp27-cp27m-manylinux1_x86_64.whl (2.0MB)
    100% |████████████████████████████████| 2.0MB 8.4MB/s 
Installing collected packages: Pillow
Successfully installed Pillow-5.3.0
```


## machine-features

```
#################################################################
## Ubuntu Version: $lsb_release -a
No LSB modules are available.
Distributor ID:	Ubuntu
Description:	Ubuntu 16.04.2 LTS
Release:	16.04
Codename:	xenial

#################################################################
## Machine Arquitecture: $uname -a
##
Linux map479-W2600CR 4.4.0-138-generic #164-Ubuntu SMP Tue Oct 2 17:16:02 UTC 2018 x86_64 x86_64 x86_64 GNU/Linux

#################################################################
## CPU INFO: $grep -E: (^model name|^vendor_id|^flags) /proc/cpuinfo | sort | uniq
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc aperfmperf pni pclmulqdq dtes64 monitor ds_cpl vmx smx est tm2 ssse3 cx16 xtpr pdcm pcid dca sse4_1 sse4_2 x2apic popcnt tsc_deadline_timer aes xsave avx lahf_lm epb ssbd ibrs ibpb stibp kaiser tpr_shadow vnmi flexpriority ept vpid xsaveopt dtherm arat pln pts flush_l1d
model name	: Intel(R) Xeon(R) CPU E5-2609 0 @ 2.40GHz
vendor_id	: GenuineIntel

#################################################################
#GRAPHIC CARD INFO:  $lspci -vnn | grep VGA -A 12
03:00.0 VGA compatible controller [0300]: NVIDIA Corporation GK104 [GeForce GTX 680] [10de:1180] (rev a1) (prog-if 00 [VGA controller])
	Subsystem: Device [196e:0969]
	Physical Slot: 1
	Flags: bus master, fast devsel, latency 0, IRQ 69
	Memory at d0000000 (32-bit, non-prefetchable) [size=16M]
	Memory at d8000000 (64-bit, prefetchable) [size=128M]
	Memory at e0000000 (64-bit, prefetchable) [size=32M]
	I/O ports at 3000 [size=128]
	Expansion ROM at d1000000 [disabled] [size=512K]
	Capabilities: <access denied>
	Kernel driver in use: nouveau
	Kernel modules: nvidiafb, nouveau


#################################################################
## gcc version: $gcc --version -O3 -std=c99
gcc (Ubuntu 5.4.0-6ubuntu1~16.04.10) 5.4.0 20160609
Copyright (C) 2015 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.


#################################################################
##  version of your python and pip:  version of your python and pip
Python 2.7.13
pip 18.0 from /usr/local/lib/python2.7/site-packages/pip (python 2.7)

```
