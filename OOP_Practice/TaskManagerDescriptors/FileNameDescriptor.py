class FileNameDescriptor:
    def __get__(self, instance, owner):
        return instance.__dict__.get("filename", "Not found")

    def __set__(self, instance, value: str):
        if not isinstance(value,str):
            print("File name must be string")
        elif not value.endswith(".csv"):
            print("File name must be csv")
        elif len(value) <= 4:
            print("File name must have name and extension")
        else:
            instance.__dict__["description"] = value