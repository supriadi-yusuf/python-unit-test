"""==========================================================
     this test is created based on tutorial at 
     https://www.youtube.com/watch?v=_OyuFg9pGQg
=========================================================="""

import unittest
from unittest import mock,TestCase 
from .morning import refreshing, refreshing2

class TestRiding2(TestCase):

    def test_riding(self):
        with mock.patch("vehicles.bike.MotorBike.go",return_value=11): # mock method go belongs to MotorBike class
            total = refreshing()
            self.assertEqual(total,11)