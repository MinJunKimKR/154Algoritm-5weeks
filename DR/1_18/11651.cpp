#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

typedef struct {
	int x, y;
}POS;

bool compare(POS& p1, POS& p2) {
	if(p1.y == p2.y) 
		return p1.x < p2.x;
	else
		return p1.y < p2.y;
}

int main() {
	int n;
	cin>>n;
	POS p[n];
	for(int i = 0; i<n; i++) {
		cin>>p[i].x>>p[i].y;
	}
	sort(p, p+n, compare);
	
	for(int i = 0; i<n; i++) {
		cout<<p[i].x<<" "<<p[i].y<<"\n";
	}
}
