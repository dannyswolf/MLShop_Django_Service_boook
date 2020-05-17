# https://www.protechtraining.com/blog/post/tutorial-using-djangos-multiple-database-support-477



class WarehouseRouter(object):
    def db_for_read(self, model, **hints):
        "Point all operations on warehouse models to 'SparePartsDb'"
        if model._meta.app_label == 'warehouse':
            return 'SparePartsDb'
        return 'default'

    def db_for_write(self, model, **hints):
        "Point all operations on warehouse models to 'SparePartsDb'"
        if model._meta.app_label == 'warehouse':
            return 'SparePartsDb'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        #  Allow any relation if a both models in warehouse app
        if obj1._meta.app_label == 'warehouse' and obj2._meta.app_label == 'warehouse':
            return True
        # Allow if neither is chinook app
        elif 'warehouse' not in [obj1._meta.app_label, obj2._meta.app_label]:
            return True
        return False

    def allow_syncdb(self, db, model):
        if db == 'SparePartsDb' or model._meta.app_label == "warehouse":
            return False  # we're not using syncdb on our legacy database
        else:  # but all other models/databases are fine
            return True