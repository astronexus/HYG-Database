## Welcome to the HYG star database archive.  The most current version of the database will always be found here.

## IMPORTANT NOTE:

The AT-HYG database has been moved into its own repository: "ATHYG-Database". This is currently also hosted on Github at https://github.com/astronexus/ATHYG-Database. This repo is live and will have all future updates to AT-HYG. No updates to the new AT-HYG files will be posted here.

### Versions and Licensing:

#### Current version: HYG v4.1 (directory: hyg/CURRENT/hyg_v41.csv)

HYG 4.1 contains 1 update:

1. The following stars have a primary with a proper name, but an unnamed secondary. For consistency in labeling, in HYG 4.1, these secondaries have a name of "[primary name] B". 

These names are unofficial. They are intended to make these double stars (which, in most cases, are relatively wide) show more consistent labels or names on charts that resolve the double, or lists that show both stars. Without the "B" names, labels on charts or names in lists would often look something like "Revati" and "ζ Psc", and it wouldn't always be clear that the two stars are strongly historically associated.

|HIP ID|HR/Yale ID|Bayer/Flamsteed|HYG 4.1 Name| 
|------|----------|---------------|------------|
5743|362|ζ Psc|Revati B
63121|4914|α¹ Cvn|Cor Caroli B
75415|5734|μ² Boo|Alkalurops B
78821|5985|β² Sco|Acrab B
79045|6009|κ Her|Marsic B
866230|6637|ψ¹ Dra|Dziban B
92951|7142|θ² Ser|Alya B
95951|7418|β² Cyg|Albireo B
||2890|α Gem|Castor B
||4374|ξ UMa|Alula Australis B
||6402|36 Oph|Guniibuu B

Note that α¹ CVn really is the dimmer component -- α² is the one officially designated "Cor Caroli" -- and the stars Revati, Marsic, Dziban, Castor, Alula Australis, and Gunibuu have the same Bayer or Flamsteed ID for both components, so these in particular are difficult to disambiguate without having an additional proper name on the "B" component.

### License:

This work is licensed under a
[Creative Commons Attribution-ShareAlike 4.0 International License][cc-by-sa].

[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/

---

### HYG (Hipparcos-Yale-Gliese)
#### Directory /hyg - Currently 119,614 stars

This is the original focus of this data collection. HYG combines every identifiable star in the HIPPARCOS, Yale Bright Star, and Gliese (nearby star) catalogs into a combined dataset of the stars' currently best-known positions, brightnesses, spectral types, and various additional catalog IDs such as traditional names and Bayer designations.

The current HYG catalog is v4.1. v3.0 was originally compiled in 2014. There have been a few small changes since then, mostly to add additional ID/label information and to correct a few errors. The most significant was a change in March 2023, to merge a PR that added the official star names from the IAU Working Group on Star Names in 2018, as well as to add a few additional old catalog designations for some nearby stars (e.g., "Ross 128") that may as well be proper names at this point. The final version of v3, v3.8, has only very minor differences from v4.1 in data content; the major version update was done largely to make updated licensing easier.

See hyg/README.md for details about the HYG catalog.

### AT-HYG (Tycho-2/Gaia based) HYGLike Subset
#### Directory /athyg_v3 - Currently 118,971 stars

This is a subset of the larger AT-HYG database (https://github.com/astronexus/ATHYG-Database) that mimics the original HYG database as closely as possible. The HYGLike subset contains all the data updates (such as Gaia DR3 distances and velocities) the AT-HYG build was able to collect for HYG stars.

See hyg/athyg_v3/README.md for more details.

### Miscellany
#### Directory /misc

The catalog misc/dso.csv contains a list of approximately 220K deep-sky objects, mostly galaxies, used in applications on https://www.astronexus.com. 

See misc/README.md for details about this catalog.