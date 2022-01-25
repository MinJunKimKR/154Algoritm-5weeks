#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
#define endl "\n"
using namespace std;

typedef struct subject {
	string name;
	int korean;
	int english;
	int math;
}subject;

bool compare(const subject & p1, const subject & p2) {
	if (p1.korean < p2.korean)
		return false; 
	else if (p1.korean == p2.korean) {
		if (p1.english > p2.english) {
			return false;
		}
		else if (p1.english == p2.english) {
			if (p1.math < p2.math) {
				return false;
			}
			else if (p1.math == p2.math) {
				if (p1.name > p2.name)
					return false;
			}
		}
	}
	return true;
}


int main() {

	int n;
	cin >> n;

	subject temp;
	vector<subject> student;

	string s;
	int ko;
	int en;
	int ma;
	for (int i = 0; i < n; i++) {
		cin >> s;
		cin >> ko;
		cin >> en;
		cin >> ma;
		temp.name = s;
		temp.english = en;
		temp.korean = ko;
		temp.math = ma;
		student.push_back(temp);
	}

	sort(student.begin(), student.end(), compare);

	for (int i = 0; i < n; i++) {
		cout << student[i].name << endl;
//		cout << student[i].name<<" "<<student[i].korean<<" "<<student[i].english<<" "<<student[i].math<<" " <<endl;
	}

	return 0;
}