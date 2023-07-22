#!/usr/bin/python3
"""
module for the base class
"""
import json
import csv


class Base:
    """The is the base class. It manages the id attribute for all classes"""
    __nb_objects = 0  # private static variable to track number of instances

    def __init__(self, id=None):
        """
        Initialize the class instance

        Args:
            id (int): identifier of the class instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Serialize list of dictionaries to JSON
        """
        return json.dumps(list_dictionaries) if list_dictionaries else "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file

        Args:
            cls (class):
            list_objs (list): list of instances who inherits of Base
        """

        with open(f"{cls.__name__}.json", "w", encoding="utf-8") as f:
            f.write(Base.to_json_string(
                [obj.to_dictionary() for obj in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string representation json_string

        Args:
            json_string (str): JSON string
        """
        return json.loads(json_string) if json_string else ""

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set

        Args:
            dictionary (dict): key value pair for attributes and values
        """
        instance = None
        if cls.__name__ == "Rectangle":
            instance = cls(1, 1)
        elif cls.__name__ == "Square":
            instance = cls(1)
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances
        """
        list_instances = []
        try:
            with open(f"{cls.__name__}.json", encoding="utf-8") as f:
                line = f.read()
                list_dict = Base.from_json_string(line)

                # create instances
                for d in list_dict:
                    list_instances.append(cls.create(**d))
        except FileNotFoundError:
            pass
        return list_instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Serialize list of objects to CSV

        Args:
            list_obj (list of class): list of class instances
        """
        with open(f"{cls.__name__}.csv", "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            # write the header row
            writer.writerow(list_objs[0].to_dictionary().keys())
            # write the values for each object
            for obj in list_objs:
                writer.writerow(obj.to_dictionary().values())

    @classmethod
    def load_from_file_csv(cls):
        """
        Deserialize CSV to list of class instances

        Returns: list of class instance
        """
        list_instances = []
        try:
            with open(f"{cls.__name__}.csv", encoding="utf-8") as f:
                reader = csv.DictReader(f)

                for row in reader:
                    obj = {key: int(value) for key, value in row.items()}
                    list_instances.append(cls.create(**obj))

        except FileNotFoundError:
            pass
        return list_instances

