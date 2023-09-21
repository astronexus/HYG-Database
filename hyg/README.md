## Welcome to the HYG star database archive.  The most current version of the database will always be found here.

### License and Versions:

This data set is licensed by a Creative Commons Attribution-ShareAlike license. For more details, read the Creative Commons page (https://creativecommons.org/licenses/by-sa/2.5/).
 
For additional background details, and older versions of the database, visit  http://www.astronexus.com/hyg.

For the most current version of the applications using this database, visit http://www.astronexus.com/endeavour. **

### Database field descriptions:


#### v3/hyg_v36.csv:  This is the current version (3.6) of the HYG stellar database.  It is very similar to previous v3.x files, but with minor fixes or updates. The older v2 files are now deprecated.

##### Recent changes

There are now multiple sub-versions of v3. The latest version (as of Sept. 20, 2023) is v3.6.

###### v3.6: A more comprehensive update to fix a larger set of constellation field errors (see https://github.com/astronexus/HYG-Database/issues/21 for discussion)

This update used a higher-precision version of constellation label determination to look for incorrectly labeled stars. It is worth pointing out that in this case, "incorrectly" often
means "off by only a few arcseconds". The vast majority of previously existing labels were correct.

A brief summary for the more technically-minded:

The official constellation boundaries were defined in 1930 and followed exact lines of right ascension and declination at the start of the year 1875. Over time, precession (a gradual shift in the position
of the Earth's axis) causes the boundaries to become skewed compared to the current lines of R.A. and declination. The easiest way to find out which constellation a star is in is to mathematically "unwind" this motion 
(there are calculation methods for doing this) and comparing the star's 1875 position to the exact boundary lines at the time.

The specific updates I did were:

* replacing the previous version of precession calculation, which was accurate to about 20" over 1.25 centuries, with a much higher-precision conversion available through the astropy module for
Python (https://docs.astropy.org/en/stable/index.html). The astropy module has the added benefit of being able to do multiple coordinate system changes (including precession) in parallel very quickly, much faster
than iterating through a list of stars and doing the conversions one by one.
* adding a custom calculation for nutation, a small but significant periodic variation in the Earth's axial position on top of precession itself, to an accuracy of ~0.25".  This was missing in my original
calculation and is not done automatically by the astropy module. The correction used the 4 largest terms in the conventional breakdown of the components. The smallest term had a maximum value of ~0.2", with all smaller terms 
(neglected here) of 0.1" or less.

At this point, I was able to resolve most differences reported in the discssion on Github. Specifically:

* 22 stars had their "con" (constellation) labels changed, because the higher-precision calculations put them on the other side of a constellation boundary in 1875
* 1629 stars were completely missing values for the "con" (constellation) label entirely, and were assigned whatever constellation the new calculations produced. 
* all stars mentioned in the Github issue discussion but one were converted here or in the previous version (3.5.1), which fixed some more serious errors.
* the one unconverted star (HYG ID 78313) has an 1875 position that is at most 0.5" away from the boundary, and it is currently unclear whose calculations are correct.

The stars that had their constellation labels changed are:

* HYG ID 3865: old label And, new label Psc
* HYG ID 7751: old label Phe, new label Eri
* HYG ID 19173: old label Hyi, new label Ret
* HYG ID 27992: old label Ori, new label Mon
* HYG ID 30112: old label Ori, new label Mon
* HYG ID 52886: old label Hya, new label Crt
* HYG ID 58221: old label Leo, new label Com
* HYG ID 59234: old label UMa, new label CVn
* HYG ID 67599: old label Aps, new label Cha
* HYG ID 72017: old label Vir, new label Lib
* HYG ID 74021: old label Boo, new label Ser
* HYG ID 85957: old label Ara, new label Aps
* HYG ID 87694: old label Sco, new label Sgr
* HYG ID 89105: old label Aps, new label Pav
* HYG ID 91382: old label Ser, new label Aql
* HYG ID 92907: old label Sct, new label Sgr
* HYG ID 93308: old label Vul, new label Sge
* HYG ID 95468: old label Dra, new label Cyg
* HYG ID 100777: old label Tel, new label Ind
* HYG ID 101541: old label Cyg, new label Cep
* HYG ID 105623: old label Mic, new label PsA
* HYG ID 117789: old label And, new label Peg

In all these cases, the star was within a few arcseconds of a boundary line, so even the older, "wrong" positions are scarcely noticeable in practice.

###### v3.5.1: A minor update to fix a few small errors in the "constellation" field.

The following four stars had Flamsteed IDs that were either invalid from the start, or were historically valid but no longer so because the star is in a different modern constellation.

These four stars are:

* HYG ID 10342: Old Flamsteed ID was 6 Per; is now in And
* HYG ID 22400: Old Flamsteed ID was 1 Aur; is now in Per
* HYG ID 29366: A far southern star (in Dor) that had a very wrong Flamsteed ID of "9 Lyn".
* HYG ID 84413: Old Flamsteed ID was 66 Her; is now in Oph

This update corrects these stars (the constellations are updated and the Flamsteed numbers removed). HYG v3.6 will correct a few other stars that were assigned a wrong constellation as well as ones that are completely missing a constellation designation right now.

###### v3.5: A number of errors in the HIP->HD mapping used to create HYG were found during processing of the AT-HYG catalog.

According to SIMBAD, the following HIP IDs do not have a corresponding HD ID, and the originally-assigned HD IDs have been removed:

* HIP 27111
* HIP 29395
* HIP 30997
* HIP 70790
* HIP 73094
* HIP 86405
* HIP 86542
* HIP 97991
* HIP 100111
* HIP 107156

Also according to SIMBAD, the following HIP IDs were assigned an incorrect HD ID, and have been updated:

* HIP 16747: correct ID is HD 22159
* HIP 18443: correct ID is HD 286368
* HIP 18759: correct ID is HD 281458
* HIP 20065: correct ID is HD 283549
* HIP 20272: correct ID is HD 27369
* HIP 21983: correct ID is HD 286996
* HIP 23728: correct ID is HD 32839
* HIP 24368: correct ID is HD 241842
* HIP 26280: correct ID is HD 288089
* HIP 29889: correct ID is HD 291456
* HIP 46395: correct ID is HD 302225
* HIP 48835: correct ID is HD 86523
* HIP 54355: correct ID is HD 96600
* HIP 77945: correct ID is HD 327627
* HIP 88762: correct ID is HD 312644
* HIP 90265: correct ID is HD 336196
* HIP 94106: correct ID is HD 234817
* HIP 96490: correct ID is HD 350185
* HIP 98255: correct ID is HD 350851
* HIP 100848: correct ID is HD 346569

For better handling in AT-HYG, the HIP ID 7751 assigned to Gl 66A was deleted. Both components keep a proper name of "p Eridani".

Finally, the HIP ID of 55203 assigned to Xi UMa is not associated with a valid set of data and has been deleted. The two components of Xi UMa currently have valid HD, HR, and Gliese IDs.

###### v3.4: A few more updates made during processing of the AT-HYG catalog.

A few errors were found with Gliese IDs and fixed. Specifically:

* The HIP stars HIP 10789, 14101, and 73531 do not correspond to stars in Gliese, and were mistakenly assigned Gliese IDs at some point during the original compilation of HYG v2 or v3. The Gliese IDs previously associated with them have been removed. 
* The three Gliese stars disassociated from these three HIP stars (GJ 3192, GJ 3885, and Gl 94) were added as standalone Gliese stars at the end of the HYG catalog, with new sequential primary IDs. Data for these 3 stars was taken directly from the Gliese catalog, but the RA and Dec values have been converted to epoch+equinox 2000.0 via SIMBAD.
* The HIP star 21765 originally had a Gliese ID of GJ 9163A. This has been changed to GJ 9163 (no "A") to correspond better to other catalogs' cross-references, including HIP. (This star is indeed a double, with A and B components, but very few catalogs besides Gliese reference the individual components as such.)
* The HIP stars 36626 and 36627 were assigned Gliese IDs Gl 277B and Gl 277A respectively; those two IDs were incorrectly swapped. The IDs have been swapped back to the correct association of HIP 36626 = Gl 277A, HIP 36627 = Gl 277B.
* The Gliese IDs Gl 333.2A and Gl 333.2B were originally assigned to HIP 44263 and a non-HIP star respectively. These Gliese IDs were also swapped. In addition to swapping the IDs back to the correct stars, their catalog IDs of "Ross 686" and "Ross 687" have also been added, as an extra disambiguation for AT-HYG purposes.

###### v3.3: Some more updates made during processing of the AT-HYG catalog.

* HIP 57438 has been deleted as a known bad entry (see https://cdsarc.u-strasbg.fr/viz-bin/getCatFile_Redirect/?-plus=-%2b&I/239/errata.htx). As before, primary "id"s in the remaining rows are left unchanged.
* In general, HYG v3.x used the 2007 data reduction for HIP, but the parallax and Cartesian coordinates for HIP 57146 have been reverted to the 1997 data reduction, based on its likely association with the star HIP 57148 (which has a much smaller parallax) and the better consistency of the 1997 data reduction with the parallax in Gliese.  

* The stars HIP 72509 and 72511 have had their parallaxes and Cartesian coordinates updated according to the notes in https://vizier.cds.unistra.fr/viz-bin/VizieR?-6N&-out.form=H0&//*&-source%3D1239/*notes&HIP%3D72509 : 
    - "Investigations carried out after the main catalogue was finalised led to a more likely solution for this entry (standard errors in parentheses): RA = 222.38436571 (5.01), Dec = -26.10858075 (3.59), Par = 45.59 (5.53), PM_RA = -1202.63 (6.32), PM_Dec = -182.10 (4.58),with F1 = 0 and F2 = -0.92, and processed as single star."
* The star HIP 63721 had a similar reprocessing of its parallax and Cartesian coordinates, as in its notes at https://vizier.cds.unistra.fr/viz-bin/VizieR?-6N&-out.form=H0&//*&-source%3D1239/*notes&HIP%3D63721 :
    - "Investigations carried out after the main catalogue was finalised led to a more likely solution for this entry (standard errors in parentheses):RA = 195.87120242 (1.16), Dec = 25.79668135 (1.02), Par = 3.21 (1.50), PM_RA = -36.26 (1.30), PM_Dec = -21.75 (0.98), with F1 = 0 and F2 = -1.09, and processed as single star."
* The previous three steps affected several stars that could not be reconciled with other lists of nearby (D < 20 ly) stars with well-verified data.
* HIP 84140 (Gliese 661) has been given a proper name value ("EZ Aqr") for consistency with other dim, very nearby (D < 4 pc) stars. This also simplifies some data handling for AT-HYG.


###### v3.2: During processing of the AT-HYG catalog, I found 2 stars in HYG that are currently listed as "nonexistent" in the literature (https://simbad.cds.unistra.fr/simbad/sim-id?Ident=HIP+114110&NbIdent=1&Radius=2&Radius.unit=arcmin&submit=submit+id)

* HIP 114110 (primary "id" = 113739)
* HIP 114176 (primary "id" = 113815) 

These two rows were simply deleted, so to maintain continuity with other HYG primary IDs in version 3.x, there are now gaps in the sequence for the missing primary IDs 113739 and 113815.

###### v3.1: An update from early 2023. No stars have been added or deleted, so there are no changes to the primary "id" field or to the large majority of primary catalog IDs (HIP, HD, and HR). However, there have been several significant changes in early 2023 to some of the proper names and secondary catalog IDs.

* March 21, 2023: Merged a PR to add all the IAU Working Group For Star Names standard/official names to the proper name field.
* April 10, 2023: Added a few proper names to nearby stars that lacked one, e.g. "Ross 128"
* April 11, 2023: Moved the proper name 'Guniibuu' for 36 Oph from the B component to the A component of the multiple star.
* April 24, 2023: Changed some deprecated Gliese catalog abbreviations ("NN" and "Wo") to the preferred "GJ". See https://cds.unistra.fr/cgi-bin/Dic-Simbad?GJ for comments on the labels. The original catalog numbers from the first edition of the catalog (in the range 1 - 999) still retain the "Gl" abbreviation.


###### v3.0: The original version, released in 2014.

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
