class TitleDescriptor:
    def __get__(self, instance, owner):
        return instance.__dict__.get("title", "Not found")

    def __set__(self, instance, value):
        if not isinstance(value,str):
            print("Title must be string")
        elif len(value) > 30:
            print("Title can't be longer than 30 chars")
        else:
            instance.__dict__["title"] = value