Client API
==========

Each resource below is sorted alphabetically by category.  For details on specific 
request/response formats, click on the resource URL link.



Auth
----

Method
~~~~~~~

Methods for authenticating users.

+-----------------------------+--------------------------------------------------------------------+
| Method URL                  | Description                                                        |
+=============================+====================================================================+
| :doc:`/auth/signin          | Authenticates a username/password combination and returns a        |
| </methods/auth/signin>`     | session key.                                                       |
+-----------------------------+--------------------------------------------------------------------+
| :doc:`/auth/logout          | Logout the user and clear his iphone token.                        |
| </methods/auth/logout>`     |                                                                    |
+-----------------------------+--------------------------------------------------------------------+


Comments
--------

RESTful Resource
~~~~~~~~~~~~~~~~~~

:doc:`/comments/ </methods/comments/index>`

======= =======================================
Query   :http:get:`/comments/`  
Create  :http:post:`/comments/` 
======= =======================================

:doc:`/comments/(comments_id)/ </methods/comments/object>`

======= =======================================
Get     :http:get:`/comments/(comments_id)/`
Delete  :http:delete:`/comments/(comments_id)/`
======= =======================================



Contact
-------

RESTful Resource
~~~~~~~~~~~~~~~~~~

:doc:`/contact/ </methods/contact/index>`

======= =======================================
Query   :http:get:`/contact/`  
Create  :http:post:`/contact/` 
======= =======================================

:doc:`/contact/(contact_id)/ </methods/contact/object>`

======= =======================================
Get     :http:get:`/contact/(contact_id)/`
Update  :http:post:`/contact/(contact_id)/`
Delete  :http:delete:`/contact/(contact_id)/`
======= =======================================

Method
~~~~~~~

+-------------------------------------------------+------------------------------------------------+
| Method URL                                      | Description                                    |
+=================================================+================================================+
| :doc:`/contact/upload                           | Batch upload contact list by emails and names. |
| </methods/contact/upload>`                      |                                                |
+-------------------------------------------------+------------------------------------------------+

Dare
-------

RESTful Resource
~~~~~~~~~~~~~~~~~

:doc:`/dare/ </methods/dare/index>`

======= =======================================
Query   :http:get:`/dare/`  
Create  :http:post:`/dare/` 
======= =======================================

:doc:`/dare/(dare_id)/ </methods/dare/object>`

======= =======================================
Get     :http:get:`/dare/(dare_id)/`
======= =======================================

Method
~~~~~~~

Methods for voting a specific dare.

+-------------------------------------------------+------------------------------------------------+
| Method URL                                      | Description                                    |
+=================================================+================================================+
| :doc:`/dare/(dare_id)/vote                      | Vote (POST) or get vote status (GET).          |
| </methods/dare/vote>`                           |                                                |
+-------------------------------------------------+------------------------------------------------+

Connections
~~~~~~~~~~~~~

Connections for a dare.

Comments
^^^^^^^^^
    
    **RESTful Resource**
    
    :doc:`/methods/dare/comments`
    
    ======= =================================================================================
    Create  :http:post:`/dare/(dare_id)/comments/` 
    Query   :http:get:`/dare/(dare_id)/comments/` 
    ======= =================================================================================


Emails
^^^^^^^^^
    
    **RESTful Resource**
    
    :doc:`/dare/(dare_id)/emails/ </methods/dare/emails>`
    
    ======= =====================================================
    Query    :http:get:`/dare/(dare_id)/emails/` 
    Create   :http:post:`/dare/(dare_id)/emails/` 
    ======= =====================================================


Likes
^^^^^^^
    
    **RESTful Resource**
    
    :doc:`/methods/dare/likes`

    =========== ===============================================================================
    Like        :http:post:`/dare/(dare_id)/likes/`
    Unlike      :http:delete:`/dare/(dare_id)/likes/` 
    Likers      :http:get:`/dare/(dare_id)/likes/` 
    =========== ===============================================================================


Photos
^^^^^^^
    
    **RESTful Resource**
    
    :doc:`/dare/(dare_id)/photos/ </methods/dare/photos>`
    
    ======= =====================================================
    Create  :http:post:`/dare/(dare_id)/photos/` 
    ======= =====================================================

    **Method**
    
    +-------------------------------------------------+------------------------------------------------+
    | Method URL                                      | Description                                    |
    +=================================================+================================================+
    | :doc:`/dare/(dare_id)/photos/(photo_id)/share   | Share dare photo.                              |
    | </methods/dare/photos_share>`                   |                                                |
    +-------------------------------------------------+------------------------------------------------+


Spectators
^^^^^^^^^^^^
    
    **RESTful Resource**
    
    :doc:`/dare/(dare_id)/spectators/ </methods/dare/spectators>`
    
    ======= =====================================================
    Query    :http:get:`/dare/(dare_id)/spectators/` 
    Create   :http:post:`/dare/(dare_id)/spectators/` 
    ======= =====================================================


Videos
^^^^^^^

    **RESTful Resource**
    
    :doc:`/dare/(dare_id)/videos/ </methods/dare/videos>`

    ======= =====================================================
    Create  :http:post:`/dare/(dare_id)/videos/` 
    ======= =====================================================

    **Method**

    +-------------------------------------------------+------------------------------------------------+
    | Method URL                                      | Description                                    |
    +=================================================+================================================+
    | :doc:`/dare/(dare_id)/videos/(video_id)/share   | Share dare video.                              |
    | </methods/dare/videos_share>`                   |                                                |
    +-------------------------------------------------+------------------------------------------------+
    

Email
--------

Method
~~~~~~~~

Methods for sending email.

+-------------------------------------------------+------------------------------------------------+
| Method URL                                      | Description                                    |
+=================================================+================================================+
| :doc:`/email/invite                             | Invite others to use gulu app.                 |
| </methods/email/invite>`                        |                                                |
+-------------------------------------------------+------------------------------------------------+


Facebook
--------

Method
~~~~~~~~

Methods for interacting with Facebook.

+-------------------------------------------------+------------------------------------------------+
| Method URL                                      | Description                                    |
+=================================================+================================================+
| :doc:`/facebook/connect                         | Connects a facebook access token and id to a   |
| </methods/facebook/connect>`                    | Gulu user.  This method has several purposes,  |
|                                                 | please see the detailed documentation.         |
+-------------------------------------------------+------------------------------------------------+


Like
----

Method
~~~~~~~~

Methods for liking and unliking target objects.  Doubles as 'me too' functionality.

+-------------------------------------------------+------------------------------------------------+
| Method URL                                      | Description                                    |
+=================================================+================================================+
| :doc:`/like/like  </methods/like/like>`         | Likes (me toos) a target object.               |
+-------------------------------------------------+------------------------------------------------+
| :doc:`/like/unlike  </methods/like/unlike>`     | Unlikes (un-me toos) a target object.          |
+-------------------------------------------------+------------------------------------------------+

Notify
--------

RESTful Resource
~~~~~~~~~~~~~~~~

:doc:`/notify/ </methods/notify/index>`

======= =======================================
Query   :http:get:`/notify/`  
======= =======================================

:doc:`/notify/(notify_id)/ </methods/notify/object>`

======= =======================================
Get     :http:get:`/notify/(notify_id)/`
Update  :http:post:`/notify/(notify_id)/`
======= =======================================

Method
~~~~~~~~

Methods for marking notify objects as "seen".

+-----------------------------------------------+--------------------------------------------------+
| Method URL                                    | Description                                      |
+===============================================+==================================================+
| :doc:`/notify/seen  </methods/notify/seen>`   | Mark notifications as "seen".                    |
+-----------------------------------------------+--------------------------------------------------+


Photos
------

RESTful Resource
~~~~~~~~~~~~~~~~

:doc:`/photos/ </methods/photos/index>`

======= =======================================
Query   :http:get:`/photos/`  
Create  :http:post:`/photos/` 
======= =======================================

:doc:`/photos/(photo_id)/ </methods/photos/object>`

======= =======================================
Get     :http:get:`/photos/(photo_id)/`
======= =======================================


Place
------

RESTful Resource
~~~~~~~~~~~~~~~~

:doc:`/place/ </methods/place/index>`

======= =======================================
Query   :http:get:`/place/`  
Create  :http:post:`/place/` 
======= =======================================

:doc:`/place/(place_id)/ </methods/place/object>`

======= =======================================
Get     :http:get:`/place/(place_id)/`
======= =======================================

:doc:`/place/search </methods/place/search>`

======= =======================================
Search  :http:get:`/place/search`
======= =======================================


Registration
------------

Method
~~~~~~~~

Methods for handling new user registration.

+-------------------------------------------------+------------------------------------------------+
| Resource URL                                    | Description                                    |
+=================================================+================================================+
| :doc:`/registration/check_email                 | Checks if an email address is valid and        |
| </methods/registration/check_email>`            | available for new users.                       |
+-------------------------------------------------+------------------------------------------------+
| :doc:`/registration/check_username              | Checks if a username is a valid format and     |
| </methods/registration/check_username>`         | available for new users.                       |
+-------------------------------------------------+------------------------------------------------+
| :doc:`/registration/signup                      | Registers a new Gulu user.                     |
| </methods/registration/signup>`                 |                                                |
+-------------------------------------------------+------------------------------------------------+

SearchCity
-----------

RESTful Resource
~~~~~~~~~~~~~~~~

:doc:`/searchcity/ </methods/searchcity/index>`

======= =======================================
Query   :http:get:`/searchcity/`  
======= =======================================

:doc:`/searchcity/(city_id)/ </methods/searchcity/object>`

======= =======================================
Get     :http:get:`/searchcity/(city_id)/`
======= =======================================

:doc:`/searchcity/search </methods/searchcity/search>`

======= =======================================
Search  :http:get:`/searchcity/search`
======= =======================================


User
-----

RESTful Resource
~~~~~~~~~~~~~~~~

:doc:`/user/(user_id)/ </methods/user/object>`

======= =======================================
Get     :http:get:`/user/(user_id)/`
Update  :http:post:`/user/(user_id)/`
======= =======================================


Method
~~~~~~~~

Methods for getting user info and performing several user operations.

+-----------------------------------------------+--------------------------------------------------+
| Method URL                                    | Description                                      |
+===============================================+==================================================+
| :doc:`/user/me/                               | Get current user information.                    |
| </methods/user/me>`                           |                                                  |
+-----------------------------------------------+--------------------------------------------------+
| :doc:`/user/(actor_id)/friends/(target_id)/   | Check friend relation or make friend request.    |
| </methods/user/friends>`                      |                                                  |
+-----------------------------------------------+--------------------------------------------------+


Video
------

RESTful Resource
~~~~~~~~~~~~~~~~

:doc:`/video/ </methods/video/index>`

======= =======================================
Query   :http:get:`/video/`  
Create  :http:post:`/video/` 
======= =======================================

:doc:`/video/(video_id)/ </methods/video/object>`

======= =======================================
Get     :http:get:`/video/(video_id)/`
======= =======================================

:doc:`/video/(video_id)/ </methods/video/object>`

======= =======================================
Get     :http:get:`/video/(video_id)/`
======= =======================================






WantTo
--------

RESTful Resource
~~~~~~~~~~~~~~~~

:doc:`/wantto/ </methods/wantto/index>`

======= =======================================
Query   :http:get:`/wantto/`  
Create  :http:post:`/wantto/` 
======= =======================================

:doc:`/wantto/(wantto_id)/ </methods/wantto/object>`

======= =======================================
Get     :http:get:`/wantto/(wantto_id)/`
======= =======================================


Connections
~~~~~~~~~~~~~

Connections for a wantto.

Comments
^^^^^^^^^
    
    **RESTful Resource**
    
    :doc:`/methods/wantto/comments`
    
    ======= =====================================================
    Create  :http:post:`/wantto/(wantto_id)/comments/` 
    Query   :http:get:`/wantto/(wantto_id)/comments/` 
    ======= =====================================================


Likes
^^^^^^^
    
    **RESTful Resource**
    
    :doc:`/methods/wantto/likes`
    
    =========== ===================================================================================
    Like        :http:post:`/wantto/(wantto_id)/likes/`
    Unlike      :http:delete:`/wantto/(wantto_id)/likes/` 
    Likers      :http:get:`/wantto/(wantto_id)/likes/` 
    =========== ===================================================================================

Weibo
--------

Method
~~~~~~~~

Methods for interacting with Weibo.

+-------------------------------------------------+------------------------------------------------+
| Method URL                                      | Description                                    |
+=================================================+================================================+
| :doc:`/weibo/connect                            | Connects a weibo account to a Gulu user.       |
| </methods/weibo/connect>`                       |                                                |
|                                                 |                                                |
+-------------------------------------------------+------------------------------------------------+



Complete API List
-----------------

.. toctree::
    :maxdepth: 1
    :glob:
    
    methods/auth/*
    methods/comments/*
    methods/contact/*
    methods/dare/*
    methods/email/*
    methods/facebook/*
    methods/like/*
    methods/notify/*
    methods/photos/*
    methods/place/*
    methods/registration/*
    methods/searchcity/*
    methods/user/*
    methods/video/*
    methods/wantto/*
    methods/weibo/*
