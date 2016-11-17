Introduction
============

.. image:: http://www.sixfeetup.com/logos/EasySlideshow.gif
   :height: 259
   :width: 248
   :alt: EasySlideshow
   :align: left

EasySlideshow is a Plone product that makes it easy for any content editor to create and manage online slideshows. It comes with all the settings you need to customize your slideshows, such as:

- Adjusting the delay between slide transitions;
- Managing the height/width of slideshow images;
- Controlling whether or not captions are shown with slides;
- Selecting whether or not users can pause the slideshow when cursor is hovering over the slideshow;
- Selecting slides timeout;
- Displaying navigation as numbers, titles, thumbnails, or not at all.

In order to create a slideshow, content editors just upload pictures to a regular folder, click the folder's ``Action`` menu, and select ``Enable Slideshow``. This transforms the regular folder into a slideshow folder, and automatically changes the folder display to a slideshow view. To modify the order in which the slideshow displays the images, content editors just need to reorder the pictures in the folder by dragging them up or down in the ``Contents`` tab.

Besides living in a dedicated folder, EasySlideshow also supports the ability to display images in a portlet (a.k.a. side box). Slideshows can actually be displayed in any template by calling the slideshow macro that ships with EasySlideshow.

While EasySlideshow's global parameters are controlled via the Control Panel (log in, click ``Site Setup``, and select ``EasySlideshow Configuration``), content editors also have the ability to override the global settings for a specific slideshow directly at the folder level.  This allows the use of EasySlideshow in multiple locations on your site without having to make the appearance and function of all slideshows the same.

EasySlideshow is Plone 4 compatible (Plone 3.3.x and up) and requires no custom installation, as it leverages the jQuery library that already ships with Plone. EasySlideshow uses fields already found in the Plone image type for presentation.  The jQuery plugin that is the basis for this product is `jQuery Cycle2 <http://malsup.com/jquery/cycle2>`_.

Examples
========

Sites that use EasySlideshow include:

- `ReTrans <http://www.re-trans.com>`_
- `Simons Foundation Autism Research Initiative <http://sfari.org/>`_
- `IEEE Information Theory Society <http://www.itsoc.org/>`_
- `Indiana Historical Society <http://www.indianahistory.org/>`_

Installation
============

- In your ``buildout.cfg``, add collective.easyslideshow to the list of eggs within the ``[instance]`` section. The package is using ``z3c.autoinclude`` so there is no need to add it to ``zcml`` if you are using Plone 3.2+::

    [instance]
    eggs = collective.easyslideshow
    zcml = collective.easyslideshow

- Run buildout, and start up the instance
- Install ``collective.easyslideshow`` via ``portal_quickinstaller``

NOTES:
* version 2.1 requires Plone >= 4.1
* version 2.3 requires >= 4.3
* version 3.0 requires Plone 5 or 4.3 with Dexterity Images.

Uninstall
=========

- Uninstall ``collective.easyslideshow`` via ``portal_quickinstaller``
- Existing slideshow folders will be fully reverted to normal folders
- Marker interfaces, layout, and annotations will be removed
- Slideshow portlets will be deleted

Upgrading to 3.x
================

When upgrading to EasySlideshow 3.0 or greater, you will need to first upgrade to 2.3. Version 2.3 removes dependencies on p4a.subtyper.

Steps for upgrading:
--------------------

1. Install version `2.3` into your existing EasySlideshow powered site
2. Go to the Plone Site Setup and from the Add-Ons panel click the button to
   upgrade EasySlideshow
3. Install version `3.x`
4. Go to the Plone Site Setup and from the Add-Ons panel click the button to
   upgrade EasySlideshow

Use
===

- Create a folder in your site
- Once EasySlideshow has been installed, you will be able to subtype the folder so it becomes a slideshow folder, by clicking on ``Sub-types`` tab then selecting ``slideshow``
- Add images into the folder
- The caption on top of the image in the slideshow displays each image's ``Title`` and ``Description``
- To link a slide to a page in your site, edit the image, click on the ``Categorization`` tab, and set a related link. Each slide can have its own related link.
- Properties can be changed either site wide or on each slideshow individually. Go to site setup to set the site wide properties. For changing the properties of individual slideshow, there is a ``slideshow`` tab available on each slideshow folder. 
- A slideshow portlet is also available.  Each portlet has its own settings, and displays the images from a folder that you choose.
- Images will be automatically resized to fit the height and width set in the slideshow properties, unless you choose to display them at their original size. White space will display to the right or bottom of images that do not match the width to height ratio of the slideshow.

Customization
=============

- Slideshow appearance can be further modified by overriding ``slideshow_macros.pt``
- The slideshow macro can be put into a custom template with the following code::

    <metal:block use-macro="here/slideshow_macros/macros/slideshow">
    slideshow here...
    </metal:block>

- When used on a custom template, the slideshow will look for images in a folder called ``Slideshow Folder`` (id ``slideshow-folder``) at the same level as the page on which it will be displayed. The name of this folder can be modified within the macro.
- For more transition options, see the Cycle2 Download page http://malsup.com/jquery/cycle2/download/
- See http://malsup.com/jquery/cycle2 for further functions and customizations that can be used.
