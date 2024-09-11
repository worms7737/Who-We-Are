#include <iostream>
using namespace std;

/*int factorial(int num){
	int result = 1;
	
	for (int i =1; i <= num; i++){
		result = result * i;
	}
	
	return result;
}
*/

int main() {
	int num = 0;
	int count = 0;
	
	cin>>num;
	

	
	while(num >= 5){
		num /= 5;
		count += num;
	}
	
	cout<<count<<endl;
	
	return 0;
}
