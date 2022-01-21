#include <iostream>
#include <limits.h>

using namespace std;

int getMaxSubsequence(int arr[], int n)   
{						
	int temp =0, max = 0;
	for(int i=0; i<n; i++)
	{
		temp += arr[i];
		if(temp > max)
			max=temp;
		else if(temp<0)
			temp=0;
	}
	return max;
}

int getMaxElement(int arr[], int n) {
	int max2 = -1000;
	for(int i=0; i<n; i++)
	{
		if(max2<arr[i])
			max2=arr[i];
	}
	return max2;
}

int main()
{
	int n;
	cin>>n;
	int arr[n];
	for(int i = 0; i<n; i++) {
		cin>>arr[i];
	}
    
	int result = getMaxSubsequence(arr, n);
	if(result != 0)
		cout<<result;
	else
        cout<<getMaxElement(arr, n);
	return 0;
	
} 
