## Welcome to the HYG and AT-HYG star database archive.  The most current version of the database will always be found here.

### License and Versions:

This data set is licensed by a Creative Commons Attribution-ShareAlike license. For more details, read the Creative Commons page (https://creativecommons.org/licenses/by-sa/2.5/).
 
For additional background details, and older versions of the database, visit  http://www.astronexus.com/hyg.

For the most current version of the applications using this database, visit http://www.astronexus.com/endeavour. 

### Database Collections

There is now a major new update to this collection: Augmented Tycho-HYG or AT-HYG for short. This is the Tycho-2 catalog with added Gaia distance data (Augmented Tycho) combined with HYG. 

#### Augmented Tycho - HYG (AT-HYG)
##### Directory /athyg - Currently 2,552,166 stars

This is a new (first released May, 2023) database set that includes all the stars in the Tycho-2 catalog (minus a very small number of stars that do not have valid position or brightness data), augmented with distance data from Gaia Data Release 3 (2020-2022). The Tycho + Gaia data have then been combined with HYG to add useful name and catalog ID data for the brighter stars in the data set. 

AT-HYG came out of a desire to have a larger data set than is available in HYG, especially one with the new data from Gaia. AT-HYG is intended to replace HYG for applications that can use the larger catalog size conveniently.

See athyg/README.md for details about the AT-HYG catalog.
#### HYG (Hipparcos-Yale-Gliese)
##### Directory /hyg - Currently 119,614 stars

This is the original focus of this data collection. HYG combines every identifiable star in the HIPPARCOS, Yale Bright Star, and Gliese (nearby star) catalogs into a combined dataset of the stars' currently best-known positions, brightnesses, spectral types, and various additional catalog IDs such as traditional names and Bayer designations.

The current HYG catalog is v3.5. v3.0 was originally compiled in 2014. There have been a few small changes since then, mostly to add additional ID/label information and to correct a few errors. The most significant was a change in March 2023, to merge a PR that added the official star names from the IAU Working Group on Star Names in 2018, as well as to add a few additional old catalog designations for some nearby stars (e.g., "Ross 128") that may as well be proper names at this point.

See hyg/README.md for details about the HYG catalog.

#### Miscellany
##### Directory /misc

The catalog misc/dso.csv contains a list of approximately 220K deep-sky objects, mostly galaxies, used in applications on https://www.astronexus.com. 

See misc/README.md for details about this catalog.