## dso.csv:  This is a collection of deep-sky objects used in http://www.astronexus.com/endeavour/chart.  
There are approximately 220K objects, mostly galaxies, but also all known NGC and IC objects.

Fields in the database:

1. ra, dec: The object's right ascension and declination, for epoch 2000.0 and equinox 2000.0. 
2. type:  The object's type, as in the Historically Corrected NGC (see "dso\_source").  A full list of types is in
https://ngcicproject.observers.org/public_HCNGC/The_HCNGC_intro.pdf, p. 19.  This is the canonical list of types for objects
in this catalog, regardless of source.
3. const: The object's constellation, if known.
4. mag:  The object's visual magnitude.
5. name:  A common name for the object.
6. rarad, decrad:  The object's right ascension and declination, in radians.
7. id: Database unique ID.
8. r1, r2:  Semi-major and semi-minor axes of the object, in arcminutes.  If r2 is undefined, r1 is interpreted as the object's radius.
9. angle: Position angle of the semimajor axis of the object, in degrees.  Only defined if r1 and r2 are present.
10.  dso\_source:  Source identifier for the object's position, size, and magnitude.  Valid values are:  "0": miscellaneous, limited detail (e.g. Wikipedia).  "1": NGC 2000 (Sinott, 1988). "2": Historically Corrected New General Catalogue from the NGC/IC project (https://ngcicproject.observers.org).  "3": PGC galaxy catalog (http://leda.univ-lyon1.fr/).  "4": Collinder open cluster catalog, items not already in Messier,Caldwell,NGC,IC and with defined size and magnitude (http://www.cloudynights.com/item.php?item_id=2544).  "5": Perek-Kohoutek catalog IDs, from original (Perek + Kouhoutek, 1967) and update (Perek + Kohoutek, 2001). "6":  Faint globulars (Palomar + Terzian) from http://www.astronomy-mall.com/Adventures.In.Deep.Space/obscure.htm and http://www.astronomy-mall.com/Adventures.In.Deep.Space/palglob.htm.
11. id1, cat1:  Primary (most commonly used) ID number/designation and catalog name for this object.
12. id2, cat2:  Additional, frequently-used ID and catalog name for this object (e.g., an NGC or IC number for Messier objects).
13. dupid, dupcat:  Duplicate ID number+catalog name. Unlike id2 and cat2, a duplicate ID normally means this object is better known by the duplicate ID, and should be excluded from display.
14. display_mag:  For objects whose actual magnitude is either not known or is not representative of their visibility (such as very large diffuse nebulas like the Veil or North America Nebula), this is a suggested magnitude cutoff for chart drawing software.  This field can be safely ignored for other purposes.

Catalogs represented in the database:
* M: Messier (bright objects of all types)
* NGC:  New General Catalogue (all types)
* IC: Index Catalog (all types)
* C: Caldwell (bright objects of all types)
* Col:  Collinder (open clusters and associations)
* PK:  Perek + Kohoutek (planetary nebulas)
* PGC:  Principal Galaxy Catalog  
* UGC:  Uppsala Galaxy Catalog 
* ESO:  European Southern Observatory Catalog (galaxies)
* Ter:  Terzian (globular clusters)
* Pal:  Palomar (globular clusters)