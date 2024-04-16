# Wiring

Many projects have some wiring associated with them. This could be power,
signal, or both. It's important to document what's going on with that.

TODO: Integrate the WireViz work into this area.

```wireviz
connectors:
  X1:
    type: D-Sub
    subtype: female
    pinlabels: [ DCD, RX, TX, DTR, GND, DSR, RTS, CTS, RI ]
  X2:
    type: Molex KK 254
    subtype: female
    pinlabels: [ GND, RX, TX ]

cables:
  W1:
    gauge: 0.25 mm2
    length: 0.2
    color_code: DIN
    wirecount: 3
    shield: true

connections:
  - - X1: [ 5,2,3 ]
    - W1: [ 1,2,3 ]
    - X2: [ 1,3,2 ]
  - - X1: 5
    - W1: s
```