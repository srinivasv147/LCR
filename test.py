from main import current,makePlot,animate
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
		makePlot(1,1,12,np.linspace(0,2,num=10),[1.5],'test')
		self.assertTrue(os.path.isfile('./test.png'))
		os.remove('./test.png')
	def test_checkAnimation(self):
		animate(1,1,12,np.linspace(0,2,num=10),1.5,'test')
		self.assertTrue(os.path.isfile('test130010033_eta=1.5.mp4'))
		os.remove('test130010033_eta=1.5.mp4')
if __name__=='__main__':
	ut.main()
