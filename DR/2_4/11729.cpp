#include <iostream>

using namespace std;

void hanoi_tower(int n, int from, int temp, int to) {
	if(n==1) {
		printf("%d %d\n",from ,to);
	}
	else {
		hanoi_tower(n-1, from, to, temp);
		printf("%d %d\n",from ,to);
		hanoi_tower(n-1, temp, from, to);
	}
}

int pow(int x, int n) {
	if(n==0) return 1;
	else if(n%2==0) return pow(x*x, n/2);
	else return x*pow(x*x, (n-1)/2);
}

int main() { 
	int n, res;
	cin>>n;
	
	res = pow(2, n) - 1;
	cout<<res<<endl;
	
	hanoi_tower(n, 1, 2, 3);
}
