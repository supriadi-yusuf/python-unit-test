"""==========================================================
     this test is created based on tutorial at 
     https://www.youtube.com/watch?v=_OyuFg9pGQg
=========================================================="""

import unittest
from unittest import mock,TestCase 
from .morning import refreshing, refreshing2

class TestRiding1(TestCase):

    @mock.patch("vehicles.bike.MotorBike.go",return_value=10) # mock method go belongs to MotorBike class
    def test_riding1(self,a):
        total = refreshing()

        self.assertEqual(total,10)
    
    @mock.patch("vehicles.bike.MotorBike.go",return_value=15)
    @mock.patch("vehicles.bike.MotorBike.go",return_value=13)
    def test_riding2(self,a,b):
        total = refreshing()

        self.assertEqual(total,15)
    
    @mock.patch("vehicles.bike.MotorBike.go",return_value=15)
    @mock.patch("vehicles.bike.MotorBike.go",return_value=13)
    def test_riding3(self,a,b):
        total = refreshing2()

        self.assertEqual(total,15)