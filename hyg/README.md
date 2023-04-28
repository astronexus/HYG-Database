## Welcome to the HYG star database archive.  The most current version of the database will always be found here.

### License and Versions:

This data set is licensed by a Creative Commons Attribution-ShareAlike license. For more details, read the Creative Commons page (https://creativecommons.org/licenses/by-sa/2.5/).
 
For additional background details, and older versions of the database, visit  http://www.astronexus.com/hyg.

For the most current version of the applications using this database, visit http://www.astronexus.com/endeavour. **

### Database field descriptions:


#### v3/hyg_v32.csv:  This is the current version (3.2) of the HYG stellar database.  It is similar to the main version 2 (hygxyz.csv) file, but has a few updates.  The older v2 files are now deprecated.

##### Recent changes

There are now three subversions of v3. The latest version (as of April 27, 2023) is v3.2.

v3.0: The original version, released in 2014.

v3.1: An update from early 2023. No stars have been added or deleted, so there are no changes to the primary "id" field or to the large majority of primary catalog IDs (HIP, HD, and HR). However, there have been several significant changes in early 2023 to some of the proper names and secondary catalog IDs.

* March 21, 2023: Merged a PR to add all the IAU Working Group For Star Names standard/official names to the proper name field.
* April 10, 2023: Added a few proper names to nearby stars that lacked one, e.g. "Ross 128"
* April 11, 2023: Moved the proper name 'Guniibuu' for 36 Oph from the B component to the A component of the multiple star.
* April 24, 2023: Changed some deprecated Gliese catalog abbreviations ("NN" and "Wo") to the preferred "GJ". See https://cds.unistra.fr/cgi-bin/Dic-Simbad?GJ for comments on the labels. The original catalog numbers from the first catalog (in the range 1 - 999) still retain the "Gl" abbreviation.

v3.2: During processing of the AT-HYG catalog, I found 2 stars in HYG that are currently listed as "nonexistent" in the literature (https://simbad.cds.unistra.fr/simbad/sim-id?Ident=HIP+114110&NbIdent=1&Radius=2&Radius.unit=arcmin&submit=submit+id)

* HIP 114110 (primary "id" = 113739)
* HIP 114176 (primary "id" = 113815) 

These two rows were simply deleted, so to maintain continuity with other HYG primary IDs in version 3.x, there are now gaps in the sequence for the missing primary IDs 113739 and 113815.
##### General content notes

1. All stars now have both an epoch and equinox of 2000.0.  In v2 of the catalog, all three primary source catalogs either had or were adjusted to equinox 2000, but all 3 had different epochs, leading to small position errors at high magnifications.
2. The Flamsteed numbers now include many that were not in the _Yale Bright Star Catalog_, the
primary reference for these numbers in the original catalog.  In particular, it now contains all valid numbers listed in "Flamsteed's Missing Stars", M. Wagman, JHA xviii (1987), p 210-223.
3. Some errors in proper motions have been corrected.
4. A few additional proper names have been added.
5. For stars in Hipparcos that are known to be variable, the variable star designations have been added.  In general,
stars that were merely suspected of variability ("NSV") were excluded.

Fields in the database:

1. id: The database primary key.
2. hip: The star's ID in the Hipparcos catalog, if known.
3. hd: The star's ID in the Henry Draper catalog, if known.
4. hr: The star's ID in the Harvard Revised catalog, which is the same as its number in the Yale Bright Star Catalog.
5. gl: The star's ID in the third edition of the Gliese Catalog of Nearby Stars.
6. bf: The Bayer / Flamsteed designation, primarily from the Fifth Edition of the Yale Bright Star Catalog. This is a combination of the two designations. The Flamsteed number, if present, is given first; then a three-letter abbreviation for the Bayer Greek letter; the Bayer superscript number, if present; and finally, the three-letter constellation abbreviation. Thus Alpha Andromedae has the field value "21Alp And", and Kappa1 Sculptoris (no Flamsteed number) has "Kap1Scl".
7. ra, dec: The star's right ascension and declination, for epoch and equinox 2000.0.
8. proper: A common name for the star, such as "Barnard's Star" or "Sirius". These are taken from the International Astronomical Union (https://www.iau.org/public/themes/naming_stars/, specifically, I'm using a formatted version from https://github.com/mirandadam/iau-starnames)
9. dist: The star's distance in parsecs, the most common unit in astrometry. To convert parsecs to light years, multiply by 3.262. A value >= 100000 indicates missing or dubious (e.g., negative) parallax data in Hipparcos.
10. pmra, pmdec:  The star's proper motion in right ascension and declination, in milliarcseconds per year.  
11. rv:  The star's radial velocity in km/sec, where known.
12. mag: The star's apparent visual magnitude.
13. absmag: The star's absolute visual magnitude (its apparent magnitude from a distance of 10 parsecs).
14. spect: The star's spectral type, if known.
15. ci: The star's color index (blue magnitude - visual magnitude), where known.
16. x,y,z: The Cartesian coordinates of the star, in a system based on the equatorial coordinates as seen from Earth. +X is in the direction of the vernal equinox (at epoch 2000), +Z towards the north celestial pole, and +Y in the direction of R.A. 6 hours, declination 0 degrees.
17. vx,vy,vz: The Cartesian velocity components of the star, in the same coordinate system described immediately above. They are determined from the proper motion and the radial velocity (when known). The velocity unit is parsecs per year; these are small values (around 1 millionth of a parsec per year), but they enormously simplify calculations using parsecs as base units for celestial mapping.
18. rarad, decrad, pmrarad, pmdecrad:  The positions in radians, and proper motions in radians per year.
19. bayer:  The Bayer designation as a distinct value
20. flam:  The Flamsteed number as a distinct value
21. con:  The standard constellation abbreviation
22. comp, comp\_primary, base:  Identifies a star in a multiple star system.  comp = ID of companion star, comp\_primary = ID of primary star for this component, and base = catalog ID or name for this multi-star system.  Currently only used for Gliese stars.
23. lum:  Star's luminosity as a multiple of Solar luminosity.
24. var:  Star's standard variable star designation, when known.
25. var\_min, var\_max:  Star's approximate magnitude range, for variables.  This value is based on the Hp magnitudes for the range in the original Hipparcos catalog, adjusted to the V magnitude scale to match the "mag" field.

### Older databases (version 2): v2/hygfull.csv, v2/hygxyz.csv

These are still available, but are no longer current or being actively updated, and should be considered deprecated for higher-precision applications.

#### hygfull.csv:

1. StarID: The database primary key from a larger "master database" of stars.
2. HD: The star's ID in the Henry Draper catalog, if known.
3. HR: The star's ID in the Harvard Revised catalog, which is the same as its number in the Yale Bright Star Catalog.
4. Gliese: The star's ID in the third edition of the Gliese Catalog of Nearby Stars.
5. BayerFlamsteed: The Bayer / Flamsteed designation, from the Fifth Edition of the Yale Bright Star Catalog. This is a combination of the two designations. The Flamsteed number, if present, is given first; then a three-letter abbreviation for the Bayer Greek letter; the Bayer superscript number, if present; and finally, the three-letter constellation abbreviation. Thus Alpha Andromedae has the field value "21Alp And", and Kappa1 Sculptoris (no Flamsteed number) has "Kap1Scl".
6. RA, Dec: The star's right ascension and declination, for epoch 2000.0. Stars present only in the Gliese Catalog, which uses 1950.0 coordinates, have had these coordinates precessed to 2000.
7. ProperName: A common name for the star, such as "Barnard's Star" or "Sirius". I have taken these names primarily from the Hipparcos project's web site, which lists representative names for the 150 brightest stars and many of the 150 closest stars. I have added a few names to this list. Most of the additions are designations from catalogs mostly now forgotten (e.g., Lalande, Groombridge, and Gould ["G."]) except for certain nearby stars which are still best known by these designations.
8. Distance: The star's distance in parsecs, the most common unit in astrometry. To convert parsecs to light years, multiply by 3.262. A value of 10000000 indicates missing or dubious (e.g., negative) parallax data in Hipparcos.
9. Mag: The star's apparent visual magnitude.
10. AbsMag: The star's absolute visual magnitude (its apparent magnitude from a distance of 10 parsecs).
11. Spectrum: The star's spectral type, if known.
12. ColorIndex: The star's color index (blue magnitude - visual magnitude), where known.
                                                       
#### hygxyz.csv: the fields in hygfull, plus some additional fields useful for mapping tools:

13. X,Y,Z: The Cartesian coordinates of the star, in a system based on the equatorial coordinates as seen from Earth. +X is in the direction of the vernal equinox (at epoch 2000), +Z towards the north celestial pole, and +Y in the direction of R.A. 6 hours, declination 0 degrees.
14. VX,VY,VZ: The Cartesian velocity components of the star, in the same coordinate system described immediately above. They are determined from the proper motion and the radial velocity (when known). The velocity unit is parsecs per year; these are small values (around 10-5 to 10-6), but they enormously simplify calculations using parsecs as base units for celestial mapping.
