Introduction
============

This API documentation serves as a guide for both back-end API and client
developers.  Apart from the typical method signatures and sample
request/responses, I'll also try to include my notes where appropriate 
with suggestions for developers.

Goals
-----

For all developers working on this project, both client and server-side, please
keep the following goals in mind.  If you disagree with any of these or would 
like to add to this list, please see me.

* Unify AJAX front end and mobile client API, while keeping the possibility
  of a public facing API open for the future.
* Encourage good code maintenance habits, naming conventions, and documentation.
* Standardize API error handling across clients and methods.
* Promote API versioning, release, and deprecation processes to ensure support across 
  multiple client versions.
* Embrace REST without sacrificing practicality for the sake of strict standard adherence.

Required Reading
----------------

This documentation was generated using Sphinx.  In order to contribute 
you'll need to familiarize yourself with `reStructuredText 
<http://sphinx.pocoo.org/rest.html>`_  and the `Sphinx documentation 
<http://sphinx.pocoo.org/intro.html>`_.

To document API resources, you'll need to use the Sphinx HTTP domain,
which can be found `here <http://packages.python.org/sphinxcontrib-httpdomain/>`_

In addition, you'll want to understand what a `RESTful web service 
<http://en.wikipedia.org/wiki/Representational_state_transfer#RESTful_web_services>`_
is.

Most important, if anything is unfamiliar or unclear, don't hesitate to
ask questions!
