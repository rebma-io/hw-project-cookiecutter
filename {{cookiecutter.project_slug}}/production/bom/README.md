# Bill of Materials (BOM)

Store the Bill of Materials (BoM) for {{cookiecutter.project_name}} in this
section. There are two types of BOMs that you might need to maintain. The
first is a complete BOM that has _every_ part that your project will need.
The other is a BOM for the assembly of a PCB. This is, quite clearly, a
subset of the greater complete BOM. You should store both of these as a CSV
with the following columns:

| Column       | Description                                                                        |
|--------------|------------------------------------------------------------------------------------|
| Reference    | The reference designator. N/A if it isn't a PCB component                          |
| Qty          | The quantity of the item. Should map to the _reference_ designator                 |
| Manufacturer | The preferred manufacturer for the part, or "ANY" if no preference.                |
| Mfg Part #   | The part number the manufacturer uses, if manufacturer specified.                  |
| Distributor  | Where the part should be procured from. "ANY" if no preference.                    |
| Dist Part #  | The part number the distributor uses. "N/A" if no preferred distributor.           |                                             
| Description  | Information about the part, it's value, tolerance, etc.                            |
| Package      | The standardized package nomenclature. This should match the footprint on the PCB. |
| Type         | SMT or Through Hole                                                                |

For _Description_, you want to include all the appropriate specifications.

* For resistors, at a minimum the tolerance and wattage should be specified. 
  A 1k, 1% 1/4W carbon resistor is very different beast from a 1k, 5% 1W w
  wirewound resistor!
* For capacitors, at a minimum the tolerance, voltage rating, and dielectric 
  type should be specified. For special applications, certain parameters such 
  as ESR or ripple current tolerance also need to be specified. A 10uF, 
  electrolytic, 10% 50V capacitor has vastly different performance at high 
  frequencies compared to a 10uF, X7R (ceramic), 20% 16V capacitor.