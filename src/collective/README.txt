Introduction
============

collective.easyslideshow is a product for displaying slideshows within your Plone site.  It uses fields already found in the Plone image type for presentation.  The base jQuery library is jQuery Cycle (http://malsup.com/jquery/cycle/)


Installation
============
- In your buildout.cfg, add collective.easyslideshow to the list of eggs within the [instance] section. It is using z3c.autoinclude so there is no need to add it to zcml too. 
- Run buildout, and start up the instance
- Install collective.easyslideshow via portal_quickinstaller


Use
===
- Create a folder in your site
- Once easyslideshow has been installed, you will be able to change the view on the folder to "Slideshow Folder"
- Add images into the folder
- The caption on top of the image in the slideshow displays each images's Title and Description
- To link a slide to a page in your site, edit the image, click on the Categorization tab, and set a related link.
- For best performance, all images used in the slideshow should be the same size, and be uploaded at that size. Slideshow size can be changed in Site Setup.
- Properties can be changed in Site Setup.  These properties will apply to all slideshows site-wide.
- A slideshow portlet is also available.  Each portlet has its own settings, and displays the images from a folder that you choose.


Customization
=============
- Slideshow appearance can be further modified by overriding slideshow_macros.pt
- The slideshow macro can be put into a custom template with the following code::

    <metal:block use-macro="here/slideshow_macros/macros/slideshow">
    slideshow here...
    </metal:block>

- When used on a custom template, the slideshow will look for images in a folder called "Slideshow Folder" (id slideshow-folder) at the same level as the page on which it will be displayed. The name of this folder can be modified within the macro.
- See http://malsup.com/jquery/cycle/ for further functions and customizations that can be used.
   

Examples
========
The following sites all use customized versions of easyslideshow:

- http://www.itsoc.org/
- http://www.indianahistory.org/
- http://www.sixfeetup.com/
- http://uvahealth.com/
- http://www.decisioneducation.org/
- http://abouthandeczema.com/
- http://abouthandeczema.com/living-with-it/
