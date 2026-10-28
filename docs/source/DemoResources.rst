.. _evs-demoresources--supplied-visual-resources:

Supplied visual resources
=========================

Import Demo to use the example scene's materials and effect prefabs. Their Resources folder is an asset location; vehicle effects use assigned references.

+----------------+----------------------------------------------------------------------+
| Resource group | Assign to                                                            |
+================+======================================================================+
| EVSJetEffects  | PropulsionJets particle prefab or material                           |
+----------------+----------------------------------------------------------------------+
| EVSWater       | WaterSurface style/material and boat spray/foam materials or prefabs |
+----------------+----------------------------------------------------------------------+
| EVSWeapons     | WeaponEffects flash/smoke and mounted payload/projectile references  |
+----------------+----------------------------------------------------------------------+
| EVSSurfaces    | TireSmoke or surface-specific particle material                      |
+----------------+----------------------------------------------------------------------+

The sample source lives in ``Samples~/Demo``; the asset-package layout uses ``Demo``. Use the imported sample folder when assigning references in your project.

You can replace any of these with compatible assets. Check material/pipeline support, particle scale/lifetime and owned cleanup before saving a prefab. Missing references can leave an individual effect absent; opening the demo does not populate another vehicle's fields.

For audio defaults and clip assignment use :doc:`Audio </Audio>`; for attribution see :doc:`Third-party credits </ThirdParty>`.
