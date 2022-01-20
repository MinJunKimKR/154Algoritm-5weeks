#include <iostream>
#include <stack>
#include <string.h>

using namespace std;
int main() {
	char sen[50];
	int n, number;
	cin>>n;
	stack<int> s;
	
	for(int i = 0; i<n; i++) {
		cin>>sen;
		if(strcmp(sen, "push") == 0) {
			cin>>number;
			s.push(number);
		}
		else if(strcmp(sen, "top") == 0) {
			if(!s.empty()) {
				cout<<s.top()<<endl;
			}
			else {
				cout<<-1<<endl;
			}
		}
		else if(strcmp(sen, "size") == 0) {
			cout<<s.size()<<endl;
		}
		else if(strcmp(sen, "empty") == 0) {
			cout<<s.empty()<<endl;
		}
		else if(strcmp(sen, "pop") == 0) {
			if(!s.empty()) {
				cout<<s.top()<<endl;
				s.pop();
			}
			else {
				cout<<-1<<endl;
			}
		}
	}
}

