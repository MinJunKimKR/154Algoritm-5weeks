#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(void) {	
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);
    
    // 보유하고 있는 랜선의 개수 K, 필요 랜선의 개수 N 입력 
    int k, n;
    cin>>k>>n;
	
    // k만큼의 벡터 선언 후, 가지고 있는 랜선의 길이 입력 
    vector<int> line(k);
    for(int i = 0; i <k; i++) {
      cin>>line[i];
    }

    // 이분 탐색을 하기위해 오름차순 정렬 
    sort(line.begin(), line.end());
	
    // 랜선의 길이가 2^31-1 이하이고, 개수 k는 1~10000 범위이므로 
    // 표현 범위 초과를 방지하기 위해 long long int형으로 선언해준다. 
    long long int start = 1, end = line[k-1];
    while(start<=end) {
      long long int mid = (start + end) / 2;

      // mid값으로 자를 수 있는 랜선의 개수를 구하기 위해 각각의 랜선을 mid로 나눈다. 
      int line_cnt = 0;
      for(int i = 0; i<k; i++) {
        line_cnt += line[i]/mid;
      }

      // 필요한 랜선의 개수보다 큰 경우, 개수를 줄여야 하므로 start는 mid+1로 바뀐다. 
      // 이와 반대인 경우, 개수를 늘려야 하므로 end를 mid-1로 바꿔준다. 
      if(line_cnt >= n) {
        start = mid + 1;
      } else { 
        end = mid - 1;
      }
    }
  
	  // 카운트한 자를 수 있는 랜선의 수가 n과 같아질 때 start가 mid에서 1이 증가하므로 end를 출력해주어야 한다. 
    cout<<end;
    return 0;
}
