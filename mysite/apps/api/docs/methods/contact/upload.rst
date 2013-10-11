/contact/upload
==================

.. http:post:: /contact/upload

    .. admonition:: Action
    
        Batch upload contact list by their email and name.

    :param contact_list: Uploaded contact list in json list format. 
    :type contact_list: json list
    
    **Sample Request:**
    
        .. code-block:: js
        
            [
              { 
                 "name": "gulu",
                 "email": "gulu@gulu.com"
              },
              {
                 "name": "jimmy",
                 "email": "jimmy@gulu.com"
              }
            ]
    
      
    **Sample Responses:**
   
        .. include:: ../null_response
   
   
   
   
