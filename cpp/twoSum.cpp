#include <iostream>
#include <vector>
#include <unordered_map>
#include <stdexcept>

std::vector<int> twoSum(std::vector<int>& nums, int target) {
	std::unordered_map<int, int> seen{};
	for (int i = 0; i < nums.size(); ++i) {
		int num = nums[i];
		int diff = target - num;
		if (seen.count(diff)) {
			return { seen[diff], i };
		}
		seen[num] = i;
	}
	throw std::invalid_argument("No two sum solution found!");
}

int main() {
	std::vector<int> numbers = { 2,3,4,5 };
	int tar = 9;
	try {
		std::vector<int> result = twoSum(numbers, tar);
		std::cout << "Indices:[";
		for (int i = 0; i < result.size(); ++i) {
			std::cout << result[i];
			if (i < result.size() - 1) {
				std::cout << ",";
			}
		}
		std::cout << "]" << std::endl;
	}
	catch (const std::invalid_argument& e) {
		std::cerr << "Error: " << e.what() << std::endl;
	}
	return 0;
}