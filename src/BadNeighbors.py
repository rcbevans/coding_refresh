'''
class BadNeighbors 
{
  public:
  map<int, int> answer;
  vector<int> blah;
  
  int getAnswer(int i1, int i2)
  {
    int key = i1*500+i2;
    if (answer.count(key)) return answer[key];
    if (i1 > i2) return 0;
    answer[key] = MAX(getAnswer(i1+1,i2), getAnswer(i1+2,i2)+blah[i1]);
    return answer[key];
  }
  
  int maxDonations(vector <int> donations) 
  {
    blah = donations;
    int n = donations.size();
    return MAX(getAnswer(0,n-2), getAnswer(1,n-1));
  }
};
'''

class BadNeighbors:
	def __init__(self):
		self.answer = {}

	def getAnswer(self, i1, i2):
		key = str(i1*500+i2)
		if key in self.answer:
			return self.answer[key]
		elif i1 > i2:
			return 0
		self.answer[key] = max(self.getAnswer(i1+1, i2), self.getAnswer(i1+2, i2)+self.blah[i1])
		return self.answer[key]


	def maxDonations(self, donations):
		self.blah = donations
		print self.blah
		n = len(self.blah)
		print n
		ans = max(self.getAnswer(0,n-2), self.getAnswer(1,n-1))
		print self.answer
		return ans
		

if __name__ == '__main__':
	test = BadNeighbors()
	donations = [1,2,3,4,5,1,2,3,4,5]
	print test.maxDonations(donations)
	'''
	donations = [ 11, 15]
	print test.maxDonations(donations)
	donations = [ 7, 7, 7, 7, 7, 7, 7 ]
	print test.maxDonations(donations)
	donations = [ 1, 2, 3, 4, 5, 1, 2, 3, 4, 5 ]
	print test.maxDonations(donations)
	donations = [ 94, 40, 49, 65, 21, 21, 106, 80, 92, 81, 679, 4, 61,  
  6, 237, 12, 72, 74, 29, 95, 265, 35, 47, 1, 61, 397,
  52, 72, 37, 51, 1, 81, 45, 435, 7, 36, 57, 86, 81, 72 ]
	print test.maxDonations(donations)
	'''