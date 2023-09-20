class CompletedDescriptor:
    def __get__(self, instance, owner):
        return instance.__dict__.get("completed", "Not found")

    def __set__(self, instance, value):
        if not isinstance(value, bool):
            print("Title must be T/F")
        else:
            instance.__dict__["completed"] = value