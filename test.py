from main import current
import unittest as ut
import numpy as np
class TestCurrent(ut.TestCase):
	def setUp(self):
		print("setUp") 
	def tearDown(self):
		print("tearDown")
	def test_checkUnderDamped(self):
		self.assertEqual(current(1,1,12,np.linspace(0,2,num=10),0.5)[0],2.0)
	def test_checkCritical(self):
		self.assertEqual(current(1,1,12,np.linspace(0,2,num=10),0.5)[0],2.0)
	def test_checkOverDamped(self):
		self.assertEqual(current(1,1,12,np.linspace(0,2,num=10),1.5)[0],2.0)

if __name__=='__main__':
	ut.main()
