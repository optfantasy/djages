Requests
========

The Gulu API supports GET, POST and DELETE HTTP requests with token and cookie-based
authentication.

Authentication
--------------

For the time being, we'll continue to use legacy API authentication to tie
into the Django auth system.  This has the advantage of simplicity and 
allows us to continue using the built-in auth system for both mobile
token-based clients and cookie-based (i.e. AJAX) requests.

To obtain a session key, use the auth/signin method, supplying a Gulu user
username and password.  When making authenticated HTTP requests either 
set the HTTP Authorization header or provide a valid session cookie.  For
example:::

   sessionid=c9d9338952400dc84772338d5ac74c38

The authentication middleware will first check for a valid session cookie,
and if invalid or not found, only then check the request Authorization
header.

.. _request-restful:

RESTful Request
-----------------

The Gulu API supports RESTful API Request. The basic idea is we have several Resources
like:

.. code-block:: python

    /contact/
    /dare/
    /place/
    .
    .
    /:collection/
    
Basically, each resource may have 3 types of RESTful sub-resource. For example,
the resource **:collection** has:

.. code-block:: python

    /:collection/ --> Index URI
    /:collection/(object_id)/ --> Object URI
    /:collection/search --> Search URI

There are several parameters for RESTfulu request. They are **offset, limit, order_by** and **detail**.
**offset** and **limit** are integers which can be used to determine return objects' offset and number.
**order_by** can be used to sort the result. 

**detail** is a boolean parameter. When it is *"true"*, the server will return the detail format of objects.

.. seealso:: The chapter :ref:`Model <model>` and the chapter :ref:`request-index`.
 

.. _request-index:

Index URI
~~~~~~~~~~~

Both **GET** and **POST** methods for **/:collection/** are available, but they stand for two 
different functions:

.. http:get:: /:collection/(object_id)/

    **Query** collection, below is several general parameters for this type of resource.
    
    :param offset: The offset of the query.
    :type offset: int

    :param limit: The limit number for the query return objects.
    :type limit: int

    :param order_by: Specify this parameter to determine the sorted order of query results.
    :type order_by: string
    
    :param filter_type: Specify this parameter to perform special query for this collection. *note: filter_type is only defined for several special collections.*
    :type filter_type: string
    
    .. admonition:: Multiple Values Query
    
        Gulu api also supports multiple values query. For example, if you want to query objects created by 
        Jason or Dennis, and the IDs of Jason and Dennis are **316** and **752**. 
        You can query objects this way: 
        
        ``/:collection/?creator_id=316,752``
        
        In short, just concat the query string with **','** and api will return the results match the 
        multiple values query.
    

.. http:post:: /:collection/(object_id)/

    **Create** object, return a object.


.. _request-object:

Object URI
~~~~~~~~~~~

Also, there are 3 methods -- **GET**, **POST** and **DELETE** available for **/:collection/(object_id)**, 
and here is the corresponding methods of these request:

.. http:get:: /:collection/(object_id)/

    **Get** object, return a object.
    
.. http:post:: /:collection/(object_id)/

    **Update** object, return a :ref:`field-string-list` to show the updated fields.
    
    **Sample Response**:

        .. code-block:: js
        
            {
                "response": "password,nickname",
                "success": true
            }
    
.. http:delete:: /:collection/(object_id)/

    **Delete** object, return ``null``.
    
    **Sample Response**:

        .. include:: methods/null_response
    
    
.. _request-search:

Search URI
~~~~~~~~~~~

The Search URI for a collection is like **/:collection/search**, and there are several important parameters 
for Search URI:

.. http:get:: /:collection/search

    :param q: The string to query objects.
    :type q: string

    :param offset: The offset of the query.
    :type offset: int

    :param limit: The limit number for the query return objects.
    :type limit: int
    
    :param search_fields: Use this parameter to specify the field of to search for this collection. 
    :type search_fields: :ref:`field-string-list`
    
    :param location: Used when the **filter_type** is *"location"*.
    :type location: :ref:`field-location`
    
    :param distance: Used when the **filter_type** is *"location"*. Constrain search range for spatial search. (in km)
    :type distance: int
    
    :param filter_type: Specify this parameter to perform different search methods for the collection. 
    :type filter_type: string
    
    
By defaults, there are 3 basic **filter_type**: *"auto_query"*, *"startswith"* and *"location"*. Below 
is the further description for these 3 types of **filter_type**.

Auto Query
^^^^^^^^^^^

    When client specify **filter_type** as ``null`` or *"auto_query"*, the server side will use
    the parameter **q** to do collection auto-query for the client.
    
Starts With
^^^^^^^^^^^^

    When client specify **filter_type** as *"startswith"*, the server side will use
    the parameter **q** to do prefix matching for the collection.

Location
^^^^^^^^^^^^

    When client specify **filter_type** as *"location"*, the server side will use
    the parameter **q** to do prefix matching for the collection, and do the spatial searching
    by the parameters **location** and **distance**.


Connections
------------

Some of Gulu api resources support Connection which is inspired by `Facebook Graph API`_.
When a resource have a connection to other type of resource, the url link will appear like below:

.. code-block:: python
    
    /dare/(dare_id)/videos/
    /dare/(dare_id)/videos/(video_id)/share
    .
    .
    .
    /:collection/(object_id)/:connection
    
Basically, the connections may provide some RESTful resources and Methods just like normal collections.

.. _Facebook Graph API: https://developers.facebook.com/docs/reference/api/user/

    