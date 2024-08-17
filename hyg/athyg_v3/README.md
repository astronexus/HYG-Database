### HYGLike v3.2 (all HYG stars in AT-HYG): 118,971 stars

This subset follows the field name and contents for HYG v3.x as closely as possible, for all stars in AT-HYG that have an entry in HYG. The subset is intended as a drop-in replacement for HYG for many applications that use HYG, but with better data. For example, just under 90% of stars in HYG v3.x and HYG v4.0 have Gaia DR3 distance data in AT-HYG v3.2, and thus also in HYGLike v3.2. 

The only difference in field names is the addition of the `*_src` fields from AT-HYG to identify the sources for each of the various data points. These fields can be dropped if desired in an application using the catalog. They are collected at the ends of the CSV rows, so should be easy to remove if desired.

### Differences between original HYG (v3.x / v4.x) and HYGLike subset from AT-HYG (v3.2):

There are a few small differences from both the original HYG and AT-HYG, mostly to handle fields in HYG that are not currently in AT-HYG, as well as to address a difference in design criteria in the two catalogs. HYG prioritized completeness, while AT-HYG prioritized accuracy, especially for 3D positions and velocities. In particular, as a subset of AT-HYG, HYGLike inherits the AT-HYG design criterion of prioritizing accurate position and velocity information for at least one star in every Tycho-2 star system over identifying every last component of every Tycho-2 star system.

If your application doesn't use any of the fields described below, AT-HYG's HYGLike subset is a drop-in replacement for HYG. Otherwise, you may need to make some small changes. However, most of the changes made were designed not to affect the core data from HYG, specifically historical star names + catalog IDs, positions, and velocities:

* Some Gliese _secondary_ and _tertiary_ stars in HYG are not currently matched to cross-references used to build AT-HYG. They will not be in the HYGLike subset. All Gliese _primary_ stars in HYG are present in AT-HYG, and thus also in HYGLike.
* The HYGLike `id` field is the AT-HYG `id` field rather than the HYG `id` field. 
* For consistency with HYG, the Sun's ('Sol') `id` is 0 as it is in HYG, not 1 as in AT-HYG.
* The HYGLike `comp`, `comp_id`, and `base` fields are pure placeholders, since AT-HYG does not track star multiplicity in the same way as HYG. The placeholder logic treats each star as single (more precisely, as not a component of a multiple star system).
* The HYGLike `lum` field is blank; if desired, calculate stellar luminosity from the absolute magnitude `absmag`. AT-HYG normalized most data to avoid redundancy.
* The HYGLike `var`, `var_min`, and `var_max` fields are blank. AT-HYG may include variable star IDs at some point, but is not currently planned to include variable star magnitude ranges.

### Summary of data updates in HYGLike

Of the 118,971 stars found for the HYGLike subset, over 99% fell into seven basic combinations of source data. Two of these are largely unchanged from the original HYG (except to use Tycho-2 as a basis for positions), but the remaining 5 include at least some data from Gaia DR3:

|Position  |Distance  |Magnitude  |Proper Motions      |Radial Velocities|Total Count     |Notes
|----------|----------|-----------|--------------------|-----------------|----------------|-------
| Tycho-2  | Gaia DR3 | HIPPARCOS | Gaia DR3           | Gaia DR3        | 89,686 (75.4%)| Full position and 3D velocity update from Gaia
| Tycho-2  | Gaia DR3 | HIPPARCOS | Gaia DR3           | (none)          | 10,381 (8.7%) | Full position and 2D velocity update from Gaia
| Tycho-2  | HIPPARCOS| HIPPARCOS | HYG sources (1)    | (none)          | 8,607 (7.2%)  | No major change from HYG
| Tycho-2  | Gaia DR3 | HIPPARCOS | Gaia DR3           | HYG sources (2) | 4,750 (4.0%)  | Full position and 2D velocity update from Gaia
| Tycho-2  | HIPPARCOS| HIPPARCOS | HYG sources (1)    | HYG sources (2) | 3,327 (2.8%)  | No major change from HYG
| Gliese   | Gaia DR3 | Gliese    | Gaia DR3           | Other sources(3)| 822 (0.7%)    | Gliese stars from HYG  w/ position and 2D velocity update from Gaia
| HIPPARCOS| Gaia DR3 | HIPPARCOS | Gaia DR3           | Gaia DR3        | 425 (0.4%)    | Full position and 3D velocity update from Gaia
| All Others|         |           |                    |                 | 973 (0.8%)    | Various incomplete levels of update

Just under 90% of all HYG stars got significant updates (Gaia DR3) to distance and proper motion. About 76% of HYG stars also got Gaia DR3 values for radial velocities. The remaining 10% of stars with no Gaia updates are generally stars not available in Gaia in the first place, including most stars brighter than about V = +3, or ones where the distance in Gaia was missing.

(1) The overwhelming majority of HYG proper motions come from the HIPPARCOS catalog. For stars without a HIPPARCOS entry, they may be from the Yale Bright Star Catalog or the Gliese catalog.

(2) HYG sources for radial velocities include the Gliese/GJ catalog, the Yale Bright Star catalog, and the Wilson Evans Batten catalog of radial velocities. In general, W.E.B values were preferred.

(3) Other sources for RVs (specific to Gliese/GJ stars) were based on the SIMBAD lookup results for those stars at the time the AT-HYG v2.5 catalog was compiled. These include a number of highly specialized surveys that apply only to a fairly small number of stars, unlike the sources used for radial velocity data for most of HYG (noted above) and AT-HYG (overwhelmingly Gaia DR3, with some from Gaia DR2).
