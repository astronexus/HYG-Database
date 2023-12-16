### Version changes

The latest version (as of Dec. 15, 2023) is v4.0. 

##### Previous Versions:

###### v3.8: Update proper names to include more official (IAU) names since previous update

Pull request 16 (https://github.com/astronexus/HYG-Database/pull/16), from June 14, 2019, incorporated a large number of 
IAU offical star names to the `proper` field in HYG 3.1 and later versions. Since then, there have been a number of updates, with the official IAU site on "naming stars" (https://www.iau.org/public/themes/naming_stars/) showing the current list of IAU-official names as of January 1, 2021, reflecting about a year and a half of updates since the original PR containing a large set of IAU names to add.

Of these new names, there were 78 that were not in previous versions of HYG and which corresponded to a star in HYG. These are outlined in the file "v38_name_updates.md", which gives the catalog IDs of the stars in HYG that were updated for version 3.8. Note that most of these are not readily naked-eye visible even from a dark site (M brighter than about +7), and so often reflect recent names from sources like NameExoWorlds (https://www.nameexoworlds.iau.org/) rather than older historical names.

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



###### v3.6.1: Reassign a problem label that was deleted (temporarily) in v3.5.1

This is a very small update to add a label to a single star (HYG 31446)

The star "9 Lyn" was incorrectly assigned to HYG 29366 (HD 43618). This was a result of an incorrect HD ID in the reference used for this ID ("Flamsteed's Missing Stars", M. Wagman, JHA xviii (1987), p 210-223)
The erroneous label was deleted from HYG 29366 in v. 3.5.1, but the correct assignment was not made at the time (it was not immediately clear if there was a correct assignment to be made).

The correct star for the label "9 Lyn" is HYG 31446 (HD 46318); there was a typo in the reference's HD number. This star now has the Flamsteed ID of "9 Lyn".
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

###### v3.1: Multiple small updates made early in 2023. 

No stars have been added or deleted, so there are no changes to the primary "id" field or to the large majority of primary catalog IDs (HIP, HD, and HR). However, there have been several significant changes in early 2023 to some of the proper names and secondary catalog IDs.

* March 21, 2023: Merged a PR to add all the IAU Working Group For Star Names standard/official names to the proper name field.
* April 10, 2023: Added a few proper names to nearby stars that lacked one, e.g. "Ross 128"
* April 11, 2023: Moved the proper name 'Guniibuu' for 36 Oph from the B component to the A component of the multiple star.
* April 24, 2023: Changed some deprecated Gliese catalog abbreviations ("NN" and "Wo") to the preferred "GJ". See https://cds.unistra.fr/cgi-bin/Dic-Simbad?GJ for comments on the labels. The original catalog numbers from the first edition of the catalog (in the range 1 - 999) still retain the "Gl" abbreviation.


###### v3.0: The original version, released in 2014.

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
