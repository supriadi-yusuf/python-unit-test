"""==========================================================
     this test is created based on tutorial at 
     https://www.youtube.com/watch?v=_OyuFg9pGQg
=========================================================="""

import unittest
from unittest import mock,TestCase 
from .morning import refreshing, refreshing2

class TestRiding4(TestCase):

    @mock.patch("vehicles.bike.MotorBike.go",side_effect=[1,2,3])# mock method go belongs to MotorBike class
    def test_riding(self,a):
        count = refreshing()
        self.assertEqual(count,1)

        count = refreshing()
        self.assertEqual(count,2)

        count = refreshing()
        self.assertEqual(count,3)