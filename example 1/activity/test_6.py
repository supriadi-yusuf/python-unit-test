"""==========================================================
     this test is created based on tutorial at 
     https://www.youtube.com/watch?v=_OyuFg9pGQg
=========================================================="""

from vehicles.bike import MotorBike
from vehicles.plane import Plane

from .morning import refreshing, refreshing2
from .afternoon import fly

import unittest
from unittest import mock,TestCase 

class TestRiding6(TestCase):

    @mock.patch("vehicles.plane.Plane.go",side_effect=Exception("boom"))# mock method go belongs to Plane class
    @mock.patch.object(MotorBike,"go",side_effect=[10,20,30]) # object reference ( we can user direct object or class)
    def test_riding(self,bike,plane):
        count = refreshing()
        self.assertEqual(count,10)

        count = refreshing()
        self.assertEqual(count,20)

        count = refreshing()
        self.assertEqual(count,30)

        status = fly()
        self.assertEqual(status,"error")