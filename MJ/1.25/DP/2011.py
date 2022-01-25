#7:50 -> 8:20
#8:13 [GG]
# 8:17 -> [FAIL]
# refer : https://mooyoungblog.tistory.com/66
# password = "101010"

password = list(input())
len_str = len(password)

if password[0] == '0':
    print(0)
    exit(0)
else:
    if len_str == 1:
        print(1)
        exit(0)
    else:
        mod = 1000000
        dp = [0] * (len_str+1)
        password= ['0']+ password
        dp[0]= dp[1] = 1
        
        for i in range(2,len_str+1):
            if 1<=int(password[i]) <=9 :
                dp[i]+=dp[i-1]
            if 9<int(''.join(password[i-1:i+1]))<27:
                dp[i]+=dp[i-2]
                
        print(dp[len_str]%mod)
        
        # 오답
        # 0201
        # 2
        # if 10<int(password[1]+password[2]) < 27 :
        #     dp[2] = 2
        # else:
        #     dp[2] = 1
        # for i in range(3,len_str+1):
        #     if 1<=int(password[i]) <=9 :
        #         dp[i]+=dp[i-1]
        #     if 9<int(''.join(password[i-1:i+1]))<27:
        #         dp[i]+=dp[i-2]
        
        # print(dp[len_str]%mod)
        
        # 위의 코드에서 어차피 dp[2]에 해당하는 부분을 따로 게산해 주는것만 다르지,
        # 결국엔 1~10 이면 1, 11~26이면 2인데, 왜 틀렸는지 이해가 가지않습니다
        # 통과되었던 반례들
        # 0 -> 0
        # 101010 ->1  
        # 011 -> 0
        # 0101 -> 0
        # 1203 -> 1
        # 2626 -> 4
        # 2727 -> 1
        
        

