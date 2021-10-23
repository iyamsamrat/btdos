<h1 align="center">Bluetooth Denial of service</h1>
<p align="center">
  <a href="https://python.org">
  </a>
</p>
<p align="center">Script made for attacking Bluetooth Devices By Samrat Katwal. </p>



## Warning
<p align="center">This project was created only for fun purposes and personal use.</p>
Mr. Bastard 
Samrat Katwal

Facebook
   https://www.facebook.com/samrat.katwal.5

## To execute


```
$ sudo apt update
$ sudo apt install python3
$ cd btdos/
$ python3 Bluetooth.py
```
### NOte
<p>The script works only with Linux systems.</p>
<p>You must have "l2ping" util on your linux machine (it installed as default on Kali Linux).</p>
<p>YOU MUST SCAN AND ATTACK BEFORE SOMEONE CONNECTS TO THE TARGET!!!</p>

## How's it's tested
Kali Linux as attacker, and JY-25 Bluetooth Speaker as target.

## HOw to use
<p>First of all, you must scan network for Bluetooth devises. For example, you can use "hcitool", scan and copy Mac address you may need to execute 'service bluetooth start'.</p>

```
$ sudo apt update
$ apt install hcitool
$ sudo service bluetooth start
$ hcitool scan
```
<p>Output will be like:</p>

```
C1:E4:A4:D3:45      Jy-25
B3:C2:E3:D4:F5      POCO C3
D5:B2:F3:E4:A6      Some Bluetooth device
```
<p>Then copy target addres (for example "C1:E4:A4:D3:45") and paste it where Mac address is asked.</p>

## Tutorial

1. "Target addr" - addres of your target (Check info above).
2. "Packages size" - size of the packages, that will be sent to the target. 600 is optimal.
3. "Threads count" - number of threads, that will send packages to the target at the same time. I used 500 threads, and that was enough. Check the table below, to find optimal value.

|  Packages size | Threads count| Ping, ms  | Distance, meters | Time waited, sec  | Device |
|:--------------:|:-----: |:------------:|:--------------------:|:----------------:|:------:|
|  600           | 1       | 9           |0,3                   |           5      |JY-25   |
|  600           | 10      | 38          |0,3                   |           5      |JY-25   |
|  600           | 20      | 78          |0,3                   |           5      |JY-25   |
|  600           | 50      | 229         |0,3                   |           5      |JY-25   |
|  600           | 100     | 413         |0,3                   |           5      |JY-25   |
|  600           | 200     | 806         |0,3                   |           5      |JY-25   |
|  600           | 500     | 1961        |0,3                   |           5      |JY-25   |
|  600           | 1000    | 6621        |0,3                   |           5      |JY-25   |
|  600           | 1000+   | ...         |0,3                   |           5      |JY-25   |

## What happened to the target

<p>I haven't tested on all devices, but the device i used worked perfecly.</p>
