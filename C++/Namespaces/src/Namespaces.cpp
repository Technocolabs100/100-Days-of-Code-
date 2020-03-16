//============================================================================

//============================================================================

#include <iostream>

#include "Animals.h"
#include "Cat.h"

using namespace std;
using namespace jwp;

int main() {

	Cat cat;
	cat.speak();

	jwp::Cat cat2;
	cat2.speak();

	cats::Cat cat3;
	cat3.speak();

	cout << jwp::CATNAME << endl;
	cout << cats::CATNAME << endl;

	cout << CATNAME << endl;

	return 0;
}
