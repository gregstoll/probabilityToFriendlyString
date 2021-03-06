#!/usr/bin/python3
import unittest, probabilityToFriendlyString, pathlib

class TestPercentToFriendlyString(unittest.TestCase):
	def test_allCases(self):
		testCasesPath = pathlib.Path(__file__).parent.parent.joinpath("testCases.txt")
		with open(testCasesPath, 'r') as f:
			lineNumber = 0
			for line in f.readlines():
				lineNumber += 1
				self.lineTest(line, lineNumber)

	def test_allFriendlyDescriptionCases(self):
		testCasesPath = pathlib.Path(__file__).parent.parent.joinpath("testCases.friendlyDescription.txt")
		with open(testCasesPath, 'r') as f:
			lineNumber = 0
			for line in f.readlines():
				lineNumber += 1
				self.lineTestFriendlyDescription(line, lineNumber)

	def lineTest(self, line, lineNumber):
		line = line.strip()
		if line.startswith('#'):
			return
		parts = line.split(',')
		if len(parts) == 3:
			expected = probabilityToFriendlyString.FriendlyProbability(int(parts[1]), int(parts[2]), None)
		elif len(parts) == 4:
			expected = probabilityToFriendlyString.FriendlyProbability(int(parts[1]), int(parts[2]), None, parts[3])
		else:
			self.fail("Line badly formatted: {0} (line {1})".format(line.strip(), lineNumber))
		actual = probabilityToFriendlyString.FriendlyProbability.fromProbability(float(parts[0]))
		self.assertEqual(expected.numerator, actual.numerator, "Numerator mismatch, called on {0} (line {1}) actual {2}".format(parts[0], lineNumber, actual))
		self.assertEqual(expected.denominator, actual.denominator, "Denominator mismatch, called on {0} (line {1}) actual {2}".format(parts[0], lineNumber, actual))
		self.assertEqual(expected.friendlyString, actual.friendlyString, "Denominator mismatch, called on {0} (line {1}) actual {2}".format(parts[0], lineNumber, actual))

	def lineTestFriendlyDescription(self, line, lineNumber):
		line = line.strip()
		if line.startswith('#'):
			return
		parts = line.split(',')
		expected = parts[1]
		actual = probabilityToFriendlyString.FriendlyProbability.fromProbability(float(parts[0])).friendlyDescription
		self.assertEqual(expected, actual, "Called on {0} (line {1})".format(parts[0], lineNumber))
	
if __name__ == '__main__':
	unittest.main()
