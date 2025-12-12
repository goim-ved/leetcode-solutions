#include <iostream>
#include <string>
#include <algorithm>

bool validAnagram(std::string a, std::string b) {
	if (a.size() != b.size()) {
		return false;
	}
	std::sort(a.begin(), a.end());
	std::sort(b.begin(), b.end());
	return a == b;
}

int main() {
	std::string x = "anagram";
	std::string y = "gramana";
	std::cout << validAnagram(x, y);
	return 0;
}