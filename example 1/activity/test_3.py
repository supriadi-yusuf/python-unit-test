"""==========================================================
     this test is created based on tutorial at 
     https://www.youtube.com/watch?v=_OyuFg9pGQg
=========================================================="""

import unittest
from unittest import mock,TestCase 
from .morning import refreshing, refreshing2

class TestRiding3(TestCase):

    def setUp(self):
        self.patcher = mock.patch("vehicles.bike.MotorBike.go",return_value=110) # mock method go belongs to MotorBike class
        self.patcher.start()

    def tearDown(self):
        self.patcher.stop()

    def test_1(self):
        total = refreshing()
        self.assertEqual(total,110)