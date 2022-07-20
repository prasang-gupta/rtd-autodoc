.. ***** HELP *****
   Documentation Master File

.. ***** HELP *****
   This section contains the material that would be displayed on the main page. Edit as per your needs.

Documentation in RTD format
===========================

This document is a **templatised** form for a quick documentation of any type of python module.
This serves as a quick documentation solution for a python module / toolkit (*python module* in this case) hosted on Github.
Apart from this, it also serves as a one stop solution for understanding the documentation process in RTD format.

Check out the :doc:`installation` section for instructions on installation of required packages.

To add a Github-hosted documentation (in RTD format) to your module / toolkit, check out the :doc:`usage` section for details and steps.

Feel free to reach out to the authors for any additional information:

*Bibhash C Mitra, Prasang Gupta*

.. ***** HELP *****
   This generates the left pane of the documentation.
   Populate it with XXX <YYY> where,
      XXX = Name to be displayed on the side panel
      YYY = Name of the RST file / _autosummary/<module_folder_name> 

.. toctree::
   :hidden:
   :maxdepth: 3
   
   Home <self>
   Installation <installation>
   Usage <usage>
   Python Module <_autosummary/module>
   Changelogs <changelogs>
   References <references>