import unittest

from HW04GetRepos import fetchRepos


# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework
class TestHW04GetRepos(unittest.TestCase):
    def testAPIA(self):
        self.assertEqual(fetchRepos('mardhi'), "Repository doesn't exist!")

    def testAPIB(self):
        self.assertEqual(fetchRepos('marishadhimar'), ['Repo: helloworld  Number of commits: 2','Repo: HW_04A_GitHubApi  Number of commits: 1','Repo: portfolio  Number of commits: 1','Repo: Simon-Game  Number of commits: 1','Repo: SSW_567_HW01  Number of commits: 14','Repo: SSW_567_HW02_A  Number of commits: 2','Repo: story  Number of commits: 2'])


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
