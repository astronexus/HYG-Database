## Welcome to the HYG star database archive.  The most current version of the database will always be found here.

### License and Versions:

This data set is licensed by a Creative Commons Attribution-ShareAlike license. For more details, read the Creative Commons page (https://creativecommons.org/licenses/by-sa/2.5/).
 
For additional background details, and older versions of the database, visit  http://www.astronexus.com/hyg.

For the most current version of the applications using this database, visit http://www.astronexus.com/endeavour. **

#### v3/hyg_v37.csv:  This is the current version (3.7) of the HYG stellar database.  It is very similar to previous v3.x files, but with minor fixes or updates. The older v2 files are now deprecated.

##### Recent changes

There are now multiple sub-versions of v3. The latest version (as of Sept. 25, 2023) is v3.7.

###### v3.7: Assign missing HR (Yale Bright Star Catalog) stars

Issue 22 (https://github.com/astronexus/HYG-Database/issues/22) described a set of 98 HR (YBSC) IDs that were not found in HYG. Of these, 82 could be ascribed to HR IDs for multiple star components that are not in HIP, or to objects in YBSC that are not stellar (or otherwise unsuitable for HYG).

Of the remaining 16 stars, 4 IDs were simply missing and were added directly. In two cases, the missing ID resulted from a bad HIP->HD cross-reference in the original HYG data, so the HD numbers were updated as well:

* HR 1 = HIP 424 (HD unchanged)
* HR 4401 = HIP 55597 (HD unchanged)
* HR 6758 = HIP 88627, HD 165475 (HD changed, HR is associated with this HD)
* HR 8793 = HIP 114167, HD 218269 (HD changed, HR is associated with this HD)

The remaining 12 stars were missing entirely from HIP. They all have Henry Draper numbers, and have had their YBSC data added unchanged, with a couple minor exceptions (noted below):

* HR 1704 = HD 33948
* HR 2322 = HD 45291
* HR 2341 = HD 45509
* HR 2366 = HD 45951
* HR 2950 = HD 61563
* HR 3328 = HD 71488
* HR 4210 = HD 93308, eta Carinae
* HR 5343 = variable CN Boo
* HR 6263 = HD 152249
* HR 6660 = HD 162678
* HR 6848 = HD 168021
* HR 9090 = variable W Cet

These 12 stars were added to the end of the catalog, in order of increasing R.A., and given new sequential HYG IDs (119619-119630). I did this to avoid having to renumber existing stars and breaking continuity with earlier versions.

I made a few small changes to the raw YBSC data when adding these new entries:

* The parallax for HR 6848 of 20 mas (distance: 50 pc) is impossibly large for a V ~ 7 star with spectral type B0 Ib (i.e., blue supergiant). A quick check in SIMBAD confirmed this suspicion. I treated it as invalid (0 mas, placeholder distance value).
* The stars CN Boo and W Cet have variable magnitude ranges from the General Catalog of Variable Stars (5th ed.). The values for W Cet are unchanged. The values for CN Boo are adjusted to the YBSC visual magnitude, which is slightly different from the one given in the GCVS.
* I did not calculate true space velocities (vx,vy,vz) for these 12 stars. 9 of the 12 (10 if including the change I made for HR 6848) have no valid parallax in YBSC. The other two are not known to high enough accuracy to justify the effort to calculate them. I intend for AT-HYG to recalculate all of these values to much higher accuracy in the relatively near future, anyway.

###### Earlier versions

For details about previous versions and the changes they made, see version-info.md.

###### General content notes

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

