#!/usr/bin/python3
"""
"""
import unittest
from model.base_model import BaseModel


class TestBasemodel(unittest.TestCase):
    def test_init(self):
        my_model = BaseModel()
        self.assertIsNotNone(my_model.id)
        self.assertIsNotNone(my_model.created_at)
        self.assertIsNotNone(my_model.updated_at)

    def test_save(self):
        my_model = BaseModel()
        initial_updated_at = my_model.updated_at
        current_updated_at = my_model.save()
        self.assertNotEqual(initial_update_at, current_updated_at)

    def test_to_dict(self):
        my_model = BaseModel()
        my_model_dict = my_model.to_dict()
        self.assertIsInstance(my_model.to_dict, dict)
        self.assertEqual(my_model_dict["__class__"], 'BaseModel')
        self.assertEqual(my_model_dict['id'], my_model.id)
        self.assertEqual(my_model_dict['created_at'], my_model.create_at.isformat)
        self.assertEqual(my_model_dict['updated_at'], my_model.updated_at.isformat)

    def test_str(self):
        my_model = BaseModel()
        self.assertTrue(str(my_model).startswith('[BaseModel]'))
        self.assertIn(my_model.id, str(my_model))
        self.assertTrue(str(my_model.__dict__). str(my_model))
