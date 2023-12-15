
# Stress Calculation Codes

This folder consists of Python files. If you want to add any other Language (MATLAB etc.), create another folder.

## Folder Outline

Make sure all the files are in the same folder in your locale.

### *main_gear.py*

* Program will run to calculate factor of safety values when you execute this file. You should only change the numerical values in this file. **DO NOT CHANGE** other files. Check Hypocycloid.py file to learn how to initialize Hypocycloidal Gear objects.

### *main_part.py*

* Program will run to calculate maximum normal and shear stresses in a part. Part properties should be given as an external .txt file. This .txt  file has a template given as *part_template.txt* file. Get necessary values from Siemens NX.
* Change necessary parameters in main_part.py to define another part or change the part.
* Please define all all parts as .txt file for further investigation.
* Edit force and torque values inside the main_part.py as you wish.
* There is a possible **error** in **bending stress calculation**, please **CHECK IT.**

### More Questions?

* Contact Can:)
