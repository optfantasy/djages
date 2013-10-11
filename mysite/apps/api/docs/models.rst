Fields, Models & Enumeration
==============================

Fields
-----------
Following is the definition of field types which are used for request and response.

.. _field-bool:

bool
~~~~~
When client makes a request, it is a String, which may be **"true"** or **"false"**.
When server makes a response, it is a Bolean, which may be **true** or **false**.

.. _field-date:

date
~~~~~~~
String, which is formatted as **mm/dd/yyyy**, e.g. **10/07/2011**..


.. _field-email:

email
~~~~~~~
String, which is formatted as **"gulu@gulu.com"**.


.. _field-email-list:

email list
~~~~~~~~~~~
Email list, which is formatted as **"gulu@gulu.com,jimmy@gulu.com"**.
In other words, it is a list of emails which are separated by **","**.

.. _field-file:

file
~~~~~~
File upload field, which must be used with :http:method:`POST` and ``enctype="multipart/form-data"``


.. _field-id:

id
~~~
MongoDB Id which is formatted as **"4ed1d110e710c417a0000000"** with 
**length 24**.


.. _field-id-list:

id list
~~~~~~~~
ID list, which is formatted as **"4ed1d110e710c417a0000000,4ed1d110e710c417a0000001"**.
In other words, it is a list of IDs which are separated by **","**.


.. _field-location:

location
~~~~~~~~~
A pair of float number, which is formatted as **"latitude,longitude"**, e.g. **"24.86,121.53"**,
where the legal range of latitude is **[-90, 90]** and longitude is **[-180, 180]**.

.. _field-string-list:

string list
~~~~~~~~~~~~
String list, which is formatted as **"apple,orange,berry"**. 
In other words, it is a list of string which are separated by **","**.

.. _field-timestamp:

timestamp
~~~~~~~~~~
String, which is formatted as float, e.g. **"1318932977.0"**.


.. _field-type:

type
~~~~~~~
String, which is formatted as **"app.model"** with lower case.

Options are:

    * :ref:`auth.user <model-user>`
    * chat.chat
    * :ref:`comments.comment <model-comment>`
    * :ref:`dare.dare <model-dare>`
    * dish.dish
    * events.event
    * :ref:`place.place <model-place>`
    * :ref:`photos.photo <model-photo>` 
    * post.post
    * review.review
    * :ref:`wantto.wantto <model-wantto>`
    
.. _field-url:

url
~~~~
String, which is formatted as http url, e.g. **"http://gulu.com/newapi/photos/"**.


.. _model:
    
Models 
-------
Following is the definition of models which are used for request and response.

About requesting extended fields please refer to :ref:`request-restful`. 
(Use a parameter *detail* to show extended fields of a model object.)

.. _model-comment:

Comment
~~~~~~~~

**Basic Fields:**

    * **id** (:ref:`field-id`):
        The comment ID.
  
    * **user** (:ref:`user object <model-user>`):
        The user object for the comment.
  
    * **content** (*string*):
        The content for the comment.
  
    * **target_type** (:ref:`field-type`):
        The type of the content object for the comment.
  
    * **target_id** (:ref:`field-id`):
        The ID of the content object for the comment.
  
    * **created** (:ref:`field-timestamp`):
        The created time of the comment.
  
    * **created_since** (*string*):
        The elapsed time since the comment creation.
  
       
**Sample Responses**:

    .. include:: methods/comments/object_response


.. _model-contact:

Contact
~~~~~~~~

**Basic Fields:**

    * **id** (:ref:`field-id`):
        The contact ID.

    * **nickname** (*string*):
        The name of the contact.
  
    * **email** (:ref:`field-email`):
        The email of the contact.
  
    * **gulu_user_id** (:ref:`field-id`):
        The corresponded gulu user ID of the contact. 
        If it is not corresponding to a gulu user, then it will be ``null``.
  
    * **is_favorited** (:ref:`field-bool`):
        The is_favorited attributed of the contact.
  
    * **photo** (:ref:`photo object <model-photo>`):
        The main photo of the contact.

**Sample Responses**:

    .. include:: methods/contact/object_response


.. _model-dare:

Dare
~~~~~~~~

**Basic Fields:**

    * **id** (:ref:`field-id`):
        The dare ID.
        
    * **title** (*string*):
        Title.

    * **created** (:ref:`field-timestamp`):
        The created time of the dare.
        
    * **place** (:ref:`place object <model-place>`):
        The place for the dare.

    * **creator** (:ref:`user object <model-user>`):
        The creator of the dare.

    * **challenger** (:ref:`user object <model-user>`):
        The challenger of the dare.

    * **city** (:ref:`searchcity object <model-search-city>`):
        The city for the dare.
    
**Extended Fields:**

    * **like_cnt** (*int*):
        The count of like for the dare.

    * **is_like** (:ref:`field-bool`):
        A boolean to tell whether the dare is liked by request user.

    * **can_vote** (:ref:`field-bool`):
        A boolean to tell can request user vote for this dare.

    * **yes_no** (*string*):
        The prediction status of the request user. The value might be *"yes", "no", ""*.

    * **ttu_ef** (*string*):
        The vote status of the request user. The value might be *"ttu", "ef", ""*.

    * **comment_cnt** (*int*):
        The count of comments for the dare.

    * **yes_cnt** (*int*):
        The count of "yes" prediction for the dare.

    * **no_cnt** (*int*):
        The count of "no" prediction for the dare.

    * **ttu_cnt** (*int*):
        The count of "ttu" vote for the dare.

    * **ef_cnt** (*int*):
        The count of "ef" vote for the dare.



**Sample Responses**:

    .. include:: methods/dare/object_response


.. _model-notify:

Notify
~~~~~~~~

**Basic Fields:**

    * **id** (:ref:`field-id`):
        The notify ID.
        
    * **user** (:ref:`user object <model-user>`)
        The receiver of the notification.
        
    * **unseen** (:ref:`field-bool`):
        The flag to tell whether the notification has been seen.
        
    * **content** (*string*):
        The content of the notification.
        
    * **target_type** (:ref:`field-type`):
        The type of the content object for the notification.
    
    * **target_id** (:ref:`field-id`):
        The ID of the content object for the notification.
        
    * **notify_type** (*int*):
        The type of the notification.
        (TODO: create notification type full list.)
        

**Extended Fields:**

    * **status** (*int*):
        A special parameter which is used as a flag to show the notification status in some type of notification.

    * **created** (:ref:`field-timestamp`):
        The created time of the notification.

    * **object** (*object*):
        The content object of the notification with json format.


**Sample Responses**:

    .. include:: methods/notify/object_response




.. _model-photo:

Photo
~~~~~~~~

**Basic Fields:**

    * **id** (:ref:`field-id`):
        The photo ID.
        
    * **thumb** (:ref:`field-url`):
        The thumbnail image (50x50) url of the photo.

**Extended Fields:**

    * **medium** (:ref:`field-url`):
        The medium image (160x160) url of the photo.

    * **large** (:ref:`field-url`):
        The large image (450x450) url of the photo.

    * **original** (:ref:`field-url`):
        The original image (fullsize) url of the photo.


**Sample Responses**:

    .. include:: methods/photos/object_response



.. _model-place:

Place
~~~~~~~~

**Basic Fields:**

    * **id** (:ref:`field-id`):
        The place ID.

    * **name** (*string*):
        The place name.

**Extended Fields:**

    * **photo** (:ref:`photo object <model-photo>`):
        The main profile photo of the place.

    * **latitude** (*float*):
        The latitude of the place.

    * **longitude** (*float*):
        The longitude of the place.


**Sample Responses**:

    .. include:: methods/place/object_response
    


.. _model-search-city:

SearchCity
~~~~~~~~~~~~

**Basic Fields:**

    * **id** (:ref:`field-id`):
        The search city ID.

    * **name** (*string*):
        The name of the city.

    * **latitude** (*float*):
        The latitude of the city.

    * **longitude** (*float*):
        The longitude of the city.

**Sample Responses**:

    .. include:: methods/searchcity/object_response


.. _model-user:

User
~~~~~~~~

**Basic Fields:**

    * **id** (:ref:`field-id`):
        The user ID.
    
    * **nickname** (*string*):
        The nickname of the user.
    
    * **photo** (:ref:`photo object <model-photo>`)
        The main profile photo of the user.


**Extended Fields:**

    * **wantto_cnt** (*int*):
        The count of WantTo which are posted by the user.

    * **metoo_cnt** (*int*):
        The count of WantTo which are metooed by the user.

    * **create_dare_cnt** (*int*):
        The count of Dare which are created by the user.

    * **pre_dare_cnt** (*int*):
        The count of Dare which are played by the user.

    * **after_dare_cnt** (*int*):
        The count of Dare which are completed by the user.


**Personal Fields:**

These fields will only show when ``user == request.user``

    * **social** (:ref:`field-string-list`):
        The social profiles of the user. Options are :ref:`enum-social`.
    
    * **privacy** (*string*):
        The privacy setting of the user. Options are :ref:`enum-privacy`.
    
    * **allow_activity_email** (:ref:`field-bool`):
        The allow activity email setting of the user.
     

**Sample Responses**:

    .. include:: methods/user/object_response




.. _model-video:

Video
~~~~~~~~

**Basic Fields:**

    * **id** (:ref:`field-id`):
        The video ID.
        
    * **user** (:ref:`user object <model-user>`)
        The owner of this video.

    * **thumb** (:ref:`field-url`)
        The thumbnail url of this video.
        
    * **url** (:ref:`field-url`)
        The video url.

**Sample Responses**:

    .. include:: methods/video/object_response


.. _model-wantto:

WantTo
~~~~~~~~

**Basic Fields:**

    * **id** (:ref:`field-id`):
        The wantto ID.
        
    * **user** (:ref:`user object <model-user>`)
        The creator of the wantto.
    
    * **category** (*string*)
        The category of wantto. It might be *"eat", "shop", "show", "sports", "hangout", "party"*.
        
    * **display_time** (*string*)
        The time of this wantto post.
        
    * **created_since** (*string*)
        The elapsed time since the wantto posted.
        
    * **created** (:ref:`field-timestamp`):
        The creation time of the wantto.
        
    * **place** (:ref:`place object <model-place>`):
        The place for the wantto.
        
    * **content** (*string*):
        The content (verb) of this wantto.
        
    * **city** (:ref:`searchcity object <model-search-city>`):
        The city for the wantto.

**Extended Fields:**

    * **comment_cnt** (*int*):
        The count of comments for the wantto.

    * **metoo_cnt** (*int*):
        The count of metoo for the wantto.

    * **is_metoo** (*int*):
        A boolean to tell whether the wantto is metoo-ed by the request user.
        

**Sample Responses**:

    .. include:: methods/wantto/object_response



Enumeration
-------------
Following is the definition of gulu enums.

.. _enum-privacy:

Privacy Settings
~~~~~~~~~~~~~~~~~

* 'public'
* 'friends'
* 'private'

.. _enum-app:

Apps
~~~~~~

* 'dare'
* 'wantto'

.. _enum-social:

Social Networks
~~~~~~~~~~~~~~~~

* 'facebook'
* 'weibo'
