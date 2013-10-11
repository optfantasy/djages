from bson.objectid import ObjectId
from django_mongodb_engine.contrib import MongoDBManager as OriginDBManager
from django.db import connections


class MongoDBManager(OriginDBManager):
    def set(self, field, object_pk, field_value):
        filter_query = {
            '_id': ObjectId(object_pk)
        }

        update_query = {
            '$set': {field: field_value}
        }

        self.raw_update(filter_query, update_query)

    def add(self, field, object_pk, field_value, cnt_field=None):
        filter_query = {
            '_id': ObjectId(object_pk),
            field: {'$ne': field_value}
        }

        update_query = {
            '$addToSet': {field: field_value}
        }
        if cnt_field:
            update_query['$inc'] = {cnt_field: 1}

        self.raw_update(filter_query, update_query)

    def batch_add(self, field, object_pks, field_value, cnt_field=None):
        filter_query = {
            '_id': {'$in': map(lambda pk: ObjectId(pk), object_pks)},
            field: {'$ne': field_value}
        }

        update_query = {
            '$addToSet': {field: field_value}
        }
        if cnt_field:
            update_query['$inc'] = {cnt_field: 1}

        self.raw_update(filter_query, update_query)

    def remove(self, field, object_pk, field_value, cnt_field=None):
        filter_query = {
            '_id': ObjectId(object_pk),
            field: field_value
        }

        update_query = {
            '$pull': {field: field_value}
        }
        if cnt_field:
            update_query['$inc'] = {cnt_field: -1}

        self.raw_update(filter_query, update_query)

    def find_and_modify(self, collection_name, query={}, update=None, upsert=False, **kwargs):
        database_wrapper = connections['default']
        collection = database_wrapper.get_collection(collection_name)
        result = collection.find_and_modify(query, update=update, upsert=upsert, **kwargs)
        return result

    def pymongo_aggregate(self, collection_name, match=None, group=None, project=None, unwind=None, sort=None, extra=None):
        database_wrapper = connections['default']
        collection = database_wrapper.get_collection(collection_name)
        query = []
        if match:
            query.append({"$match": match})
        if project:
            query.append({"$project": project})
        if unwind:
            query.append({"$unwind": unwind})
        if group:
            query.append({"$group": group})
        if sort:
            query.append({"$sort": sort})
        if extra:
            query.append(extra)

        r = collection.aggregate(query)
        if r["ok"] == 1:
            return r["result"]
        else:
            return []

    def unset(self, field, object_pk):
        filter_query = {
            '_id': ObjectId(object_pk),
        }

        update_query = {
            '$unset': {field: 1}
        }
        self.raw_update(filter_query, update_query)        

    def batch_remove(self, field, object_pks, field_value, cnt_field=None):
        filter_query = {
            '_id': {'$in': map(lambda pk: ObjectId(pk), object_pks)},
            field: field_value
        }

        update_query = {
            '$pull': {field: field_value}
        }
        if cnt_field:
            update_query['$inc'] = {cnt_field: -1}

        self.raw_update(filter_query, update_query)

    def get_by_items(self, field, items):
        filter_query = {
            field: {
                '$all': items,
                '$size': len(items)
            }
        }
        return self.raw_query(filter_query)

    def clean_multiple_objects(self, **query):
        objs = self.filter(**query)
        obj = objs[0]
        for each_obj in objs[1:]:
            each_obj.delete()
        return obj

    def geo_search(self, lonlat, radius=1, lonlat_field='lonlat'):
        MONGO_DISTANCE_FACTOR = 111.12
        return self.raw_query({lonlat_field: {
                '$maxDistance': radius/MONGO_DISTANCE_FACTOR,
                '$near': lonlat
            }
        })

    def geo_box_search(self, sw, ne, lonlat_field='lonlat'):
        return self.raw_query({lonlat_field: {
                '$geoWithin': {
                    '$box': [sw, ne]
                },
            }
        })

    def attach_objects(self, source_list, id_field, attach_field):
        """
        Target Class:
            The class of this manager.
        Source Class:
            The source class which needs batch attachment of this type of class.
        source_list: a list of Source Class objects
        id_field: id_field in Source Class, which is the foreign key point to Target Class.
        attach_field: after query, we will attach target object into this field.
        e.g.
            Target Class: FriendList
            Source Class: User
            id_field: user_id
            attach_field: user

            After the process, all objects in source_list will have 'user' object at the 'user' field.
        """
        id_list = map(lambda o: getattr(o, id_field), source_list)
        target_list = self.filter(id__in=id_list)
        keys = map(lambda o: getattr(o, 'id'), target_list)
        values = target_list
        dictionary = dict(zip(keys, values))
        for source in source_list:
            target_id = getattr(source, id_field)
            if not target_id:
                pass
            try:
                setattr(source, attach_field, dictionary[target_id])
            except:
                pass
