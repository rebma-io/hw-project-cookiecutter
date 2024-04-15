# Pick and Place (PnP)

Include the PnP files for in this directory. These files provide the necessary
component placement information for PCB assembly.

## Required Files

Ensure that you provide the following files in the required format for the 
manufacturer:

- Gerber Files: Ensure the Gerber files include accurate component outlines 
  and reference designators. These should match the ones in your PCB 
  production files.
- Pick and Place CSV: Create a CSV file containing the positions and 
  rotations of the components on the PCB in the manufacturer's specified 
  format for the file. These are sometimes called centroid files. 
  ([JLCPCB](https://jlcpcb.com/help/article/46-pick-place-file-for-pcb-assembly), 
  [PCBWay](https://www.pcbway.com/helpcenter/technical_support/Generate_Position_File_in_Kicad.html))

This file is crucial for accurate component placement during PCB assembly.
