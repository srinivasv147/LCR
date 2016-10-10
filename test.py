from main import current,makePlot
import unittest as ut
import numpy as np
import os
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
	def test_checkPlotting(self):
		makePlot(1,1,12,np.linspace(0,2,num=10),[1.5])
		self.assertTrue(os.path.isfile('./plots.png'))
		os.remove('./plots.png')
if __name__=='__main__':
	ut.main()
