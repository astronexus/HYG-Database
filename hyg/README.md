## Welcome to the HYG star database archive.  The most current version of the database will always be found here.

### License and Versions:

This data set is licensed by a Creative Commons Attribution-ShareAlike license. For more details, read the Creative Commons page (https://creativecommons.org/licenses/by-sa/2.5/).
 
For additional background details, and older versions of the database, visit  http://www.astronexus.com/hyg.

For the most current version of the applications using this database, visit http://www.astronexus.com/endeavour. 

#### v3/hyg_v38.csv:  This is the current version (3.8) of the HYG stellar database.  It is very similar to previous v3.x files, but with minor fixes or updates. The older v2 files are now deprecated.

##### Recent changes

There are now multiple sub-versions of v3. The latest version (as of Dec. 5, 2023) is v3.8.

###### v3.8: Update proper names to include more official (IAU) names since previous update

Pull request 16 (https://github.com/astronexus/HYG-Database/pull/16), from June 14, 2019, incorporated a large number of 
IAU offical star names to the `proper` field in HYG 3.1 and later versions. Since then, there have been a number of updates, with the official IAU site on "naming stars" (https://www.iau.org/public/themes/naming_stars/) showing the current list of IAU-official names as of January 1, 2021, reflecting about a year and a half of updates since the original PR containing a large set of IAU names to add.

Of these new names, there were 78 that were not in previous versions of HYG and which corresponded to a star in HYG. These are outlined in the file "v38_name_updates.md", which gives the catalog IDs of the stars in HYG that were updated for version 3.8. Note that most of these are not readily naked-eye visible even from a dark site (M brighter than about +7), and so often reflect recent names from sources like NameExoWorlds (https://www.nameexoworlds.iau.org/) rather than older historical names.

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

1. `id`: The database primary key.
2. `hip`: The star's ID in the Hipparcos catalog, if known.
3. `hd`: The star's ID in the Henry Draper catalog, if known.
4. `hr`: The star's ID in the Harvard Revised catalog, which is the same as its number in the Yale Bright Star Catalog.
5. `gl`: The star's ID in the third edition of the Gliese Catalog of Nearby Stars.
6. `bf`: The Bayer / Flamsteed designation, primarily from the Fifth Edition of the Yale Bright Star Catalog. This is a combination of the two designations. The Flamsteed number, if present, is given first; then a three-letter abbreviation for the Bayer Greek letter; the Bayer superscript number, if present; and finally, the three-letter constellation abbreviation. Thus Alpha Andromedae has the field value "21Alp And", and Kappa1 Sculptoris (no Flamsteed number) has "Kap1Scl".
7. `ra`, `dec`: The star's right ascension and declination, for epoch and equinox 2000.0.
8. `proper`: A common name for the star, such as "Barnard's Star" or "Sirius". These are taken from the International Astronomical Union (https://www.iau.org/public/themes/naming_stars/, specifically, I'm using a formatted version from https://github.com/mirandadam/iau-starnames)
9. `dist`: The star's distance in parsecs, the most common unit in astrometry. To convert parsecs to light years, multiply by 3.262. A value >= 100000 indicates missing or dubious (e.g., negative) parallax data in Hipparcos.
10. `pmra`, `pmdec`:  The star's proper motion in right ascension and declination, in milliarcseconds per year.  
11. `rv:`  The star's radial velocity in km/sec, where known.
12. `mag`: The star's apparent visual magnitude.
13. `absmag`: The star's absolute visual magnitude (its apparent magnitude from a distance of 10 parsecs).
14. `spect`: The star's spectral type, if known.
15. `ci`: The star's color index (blue magnitude - visual magnitude), where known.
16. `x`,`y`,`z`: The Cartesian coordinates of the star, in a system based on the equatorial coordinates as seen from Earth. +X is in the direction of the vernal equinox (at epoch 2000), +Z towards the north celestial pole, and +Y in the direction of R.A. 6 hours, declination 0 degrees.
17. `vx`,`vy`,`vz`: The Cartesian velocity components of the star, in the same coordinate system described immediately above. They are determined from the proper motion and the radial velocity (when known). The velocity unit is parsecs per year; these are small values (around 1 millionth of a parsec per year), but they enormously simplify calculations using parsecs as base units for celestial mapping.
18. `rarad`, `decrad`, `pmrarad`, `pmdecrad`:  The positions in radians, and proper motions in radians per year.
19. `bayer`:  The Bayer designation as a distinct value
20. `flam`:  The Flamsteed number as a distinct value
21. `con`:  The standard constellation abbreviation
22. `comp`, `comp_primary`, `base`:  Identifies a star in a multiple star system.  `comp` = ID of companion star, `comp_primary` = ID of primary star for this component, and `base` = catalog ID or name for this multi-star system.  Currently only used for Gliese stars.
23. `lum`:  Star's luminosity as a multiple of Solar luminosity.
24. `var`:  Star's standard variable star designation, when known.
25. `var_min,` `var_max`:  Star's approximate magnitude range, for variables.  This value is based on the Hp magnitudes for the range in the original Hipparcos catalog, adjusted to the V magnitude scale to match the "mag" field.

