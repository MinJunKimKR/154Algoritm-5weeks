#refer: https://zzsza.github.io/development/2020/06/06/github-action/
from github_utils import get_github_repo, upload_github_issue
from datetime import datetime
import math
import os

access_token = os.environ['MY_GITHUB_TOKEN']
REPO_NAME = '154Algoritm-5weeks'
PROB_CNT = 154
TOTAL_DAYS = 7 * 5
startDate = datetime(2022, 1,17)
today = datetime.today()
dailyProbCnt = PROB_CNT/TOTAL_DAYS
passedDayCnt = (today-startDate).days
progress = int((passedDayCnt/TOTAL_DAYS) * 100)
recommendNum = math.ceil(dailyProbCnt * passedDayCnt)
dDay = TOTAL_DAYS-(today-startDate).days
todayStr = str(today).split()[0]

title = f"{todayStr} 알고리즘 진행도 알림!"
content = f"<h1>오늘도 화이팅입니다! D-{dDay}</h1><h3>현재 스터디 진행도 : {progress}%</h3><h3>권장 현재 문제번호 : {recommendNum} </h3><br/>\n"

repo = get_github_repo(access_token, REPO_NAME)
upload_github_issue(repo, title, content)
print("Upload Github Issue Success!")
