#!/usr/bin/python3
import json
import models


class FileStorage:
	"""Class file storage to
	storage information"""

	__file_path = "file.json"
	__objects = {}

	def all(self):
		"""Returns the
		dictionary"""
		return FileStorage.__objects

	def new(self, obj):
		"""set in __objects
		the obj with key
		<obj clase name>.id"""
		key = "{}.{}".format(obj.__class__.__name__, obj.id)
		FileStorage.__objects[key] = obj

	def save(self):
		"""Serialize __objects
		to JSON file path"""
		dict1 = {}
		for key, value in FileStorage.__objects.items():
			dict1[key] = value.to_dict()
			with open(FileStorage.__file_path, "w") as f:
				json.dump(dict1, f)


	"""def reload(self):"""
		"""deserializes the JSON
		file to __objects"""
