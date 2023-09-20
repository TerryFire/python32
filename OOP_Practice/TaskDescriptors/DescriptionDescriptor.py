class DescriptionDescriptor:
    def __get__(self, instance, owner):
        return instance.__dict__.get("description", "Not found")

    def __set__(self, instance, value):
        if not isinstance(value,str):
            print("Title must be string")
        elif len(value) > 120:
            print("Title can't be longer than 120 chars")
        else:
            instance.__dict__["description"] = value