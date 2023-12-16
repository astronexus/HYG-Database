## Welcome to the HYG star database archive.  The most current version of the database will always be found here.

## IMPORTANT NOTE:

The AT-HYG database has been moved into its own repository: "ATHYG-Database". This is currently also hosted on Github at https://github.com/astronexus/ATHYG-Database. This repo is live and will have all future updates to AT-HYG. No updates to the new AT-HYG files will be posted here.

### Versions and Licensing:

#### Current version: HYG v4.0 (directory: hyg/CURRENT/hyg_v40.csv)

HYG 4.0 contains 2 updates:

1. 10 more stars have had proper names added. These come from the 2022 update to names from NameExoWorlds (https://www.nameexoworlds.iau.org/2022approved-names). A list of the updated names is in CURRENT/v40_name_updates.md.
2. The licensing for HYG v4.0 is Creative Commons CC BY-SA 4.0, unlike previous versions of the HYG catalog.

---

Shield: [![CC BY-SA 4.0][cc-by-sa-shield]][cc-by-sa]

This work is licensed under a
[Creative Commons Attribution-ShareAlike 4.0 International License][cc-by-sa].

[![CC BY-SA 4.0][cc-by-sa-image]][cc-by-sa]

[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg

---

### HYG (Hipparcos-Yale-Gliese)
#### Directory /hyg - Currently 119,614 stars

This is the original focus of this data collection. HYG combines every identifiable star in the HIPPARCOS, Yale Bright Star, and Gliese (nearby star) catalogs into a combined dataset of the stars' currently best-known positions, brightnesses, spectral types, and various additional catalog IDs such as traditional names and Bayer designations.

The current HYG catalog is v34.0. v3.0 was originally compiled in 2014. There have been a few small changes since then, mostly to add additional ID/label information and to correct a few errors. The most significant was a change in March 2023, to merge a PR that added the official star names from the IAU Working Group on Star Names in 2018, as well as to add a few additional old catalog designations for some nearby stars (e.g., "Ross 128") that may as well be proper names at this point. The final version of v3, v3.8, has only very minor differences from v4.0 in data content; the major version update was done largely to make updated licensing easier.

See hyg/README.md for details about the HYG catalog.

### AT-HYG (Tycho-2/Gaia based) HYGLike Subset
#### Directory /athyg_v2 - Currently 118,971 stars

This is a subset of the larger AT-HYG database (https://github.com/astronexus/ATHYG-Database) that mimics the original HYG database as closely as possible. The HYGLike subset contains all the data updates (such as Gaia DR3 distances and velocities) the AT-HYG build was able to collect for HYG stars.

See hyg/athyg_v2/README.md for more details.

### Miscellany
#### Directory /misc

The catalog misc/dso.csv contains a list of approximately 220K deep-sky objects, mostly galaxies, used in applications on https://www.astronexus.com. 

See misc/README.md for details about this catalog.