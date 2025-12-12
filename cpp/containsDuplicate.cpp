#include <iostream>
#include <vector>
#include <unordered_set>

bool containsDuplicate(std::vector<int>& nums) {
	std::unordered_set<int> nums2(nums.begin(), nums.end());
	return nums.size() != nums2.size();
}

int main() {
	std::vector<int> numbers = { 2,3,4 };
	std::cout << containsDuplicate(numbers);
	return 0;
}