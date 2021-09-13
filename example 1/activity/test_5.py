"""==========================================================
     this test is created based on tutorial at 
     https://www.youtube.com/watch?v=_OyuFg9pGQg
=========================================================="""

import unittest
from unittest import mock,TestCase 
from .morning import refreshing, refreshing2
from .afternoon import fly

class TestRiding5(TestCase):

    @mock.patch("vehicles.plane.Plane.go",side_effect=Exception("boom"))# mock method go belongs to Plane class
    @mock.patch("vehicles.bike.MotorBike.go",side_effect=[10,20,30])# mock method go belongs to MotorBike class
    def test_riding(self,bike,plane):
        count = refreshing()
        self.assertEqual(count,10)

        count = refreshing()
        self.assertEqual(count,20)

        count = refreshing()
        self.assertEqual(count,30) 

        status = fly()
        self.assertEqual(status,"error")