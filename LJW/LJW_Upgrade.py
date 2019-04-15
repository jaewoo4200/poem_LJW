import random as r
import time
import os

try:
  os.makedirs(r"C:\LJW-REG")
except FileExistsError:
  pass

__File_Name = r"C:\LJW-REG\LJW_Reg_Data_Ops.db"

try:
  with open(__File_Name, 'r') as f:
    if not f.read().isdigit():
      raise FileNotFoundError
except FileNotFoundError:
  with open(__File_Name, 'w') as f:
    f.write('0')

Poets = ["""
내가 그때 만약
                    -LJW

내가 그때 만약
그 편의점을 들어갔더라면
결과가 달랐을까요?

내가 그때 만약
네게 인사를 했더라면
우리는 이루어 졌을까요?

내가 그때 만약
너를 만나지 않았더라면
과연 이런 고민 했을까요?

우우우

인생은 타이밍
사랑도 타이밍
너와 나의 인연

내가 그때 만약
널 향한 진심을 전했더라면
""",
"""
벚꽃
	-LJW

봄이 왔다

길고
끝나지 않을것 같던
겨울이 끝나고

봄이 왔다

사람들은 봄이
희망의 계절이라 말한다

새들이 지저귀고
파릇한 식물들이 자라나는
희망찬 봄날에

나는 헤어졌다


벚꽃
다 떨어져버려라

빨리 겨울이 오길
""",
"""
벚꽃
	-LJW

봄이 왔다

길고
끝나지 않을것 같던
겨울이 끝나고

봄이 왔다

사람들은 봄이
희망의 계절이라 말한다

새들이 지저귀고
파릇한 식물들이 자라나는
희망찬 봄날에

나는 차였다


벚꽃
다 떨어져버려라

빨리 겨울이 오길
""",
"""
카톡
        -LJW

그녀에게
갑작스런 카톡이 왔다

따뜻하던 봄날에
날 찬 그녀가

역시 아이폰 짱이다

그녀가 보낸 내용을
미리보기에서
모두 볼 수 있다니

새로운 사랑을
찾아나선 그녀가
차였다고 한다

축하해줄까,
위로해줄까?

읽씹하기로 했다.
""",
"""
IDC
	-LJW

네가 뭘하든
내겐,
IDC

네가 내 앞에서
재롱을 떨어도
난 IDC

겉으로는
I Don't Care,
속으로는
I DO Care
""",
"""
썸
	-사먼의가

'썸'이란건
서로 가까이 다가갔다가
또 엇갈리다가
다음 날이면 원점으로 돌아가는 관계

친구 이상
애인 미만

'썸'이란건
아무리 신호를 주고 정답을 알려줘도
확신을 할 수 없는 관계
마음이 자꾸 불안한 관계

친구 이상
애인 미만

가깝지만 닿지 않는
한 뼘의 거리
""",
"""
너가 그리워지는 밤
		-LJW

잘 지냈니
그날 밤 우리의 이별
그땐 몰랐지
이제는 너와 따뜻한 얘기를 할 수 없단걸
모든게 지나가는 일인줄 알았지

기억나니
우리가 처음 만났던 그날
그땐 모든게 좋았지
너와 어여쁜 사랑을 할 수 있다는 사실이
나에게는 하루하루의 목표였어

혜성처럼 나타났다가
빛의 속도로 달아난 너가

원망스러워
아니
사실은 원망스럽지 않아
"""]

def 아이폰():
  print("""
아이폰
           -이스터

화났을때
참지말고
아이폰을
던지세요.
""")

class LJW(object):
  def __init__(self, Poets=Poets):
    self.Name = "이재우"
    self.Poets = Poets

  def random():
    print(r.choice(Poets))

  def all():
    for i in Poets:
      print(i)
      print("\n")

def recommend():
  import webbrowser
  webbrowser.open("http://pythong.org/")
  print(" PYTHONG,\n  YAH!!")

def 생일():
  print("4월 20일")
  import datetime

def random():
  """랜덤으로 시 출력 / Print Random Poem"""
  print(r.choice(Poets))

def everything():
  """모든 시 출력 / Print All Poems"""
  for i in Poets:
    print(i)
    print("\n")

class HeroLJW(object):
  def __init__(self, HP, MAX_HP, ATK, SP):
    self.NAME = "이재우"
    self.MAX_HP = MAX_HP
    self.HP = HP
    self.ATK = ATK
    self.SP = SP
    self.SAVE_SP = SP
    self.BIRTH = "2002년 4월 20일"
    self.ENEMY_NAME = ""
    self.ENEMY_HP = 30
    self.ENEMY_ATK = 10
    self.ENEMY_SAVE_HP = 30
    self.ENEMY_SAVE_ATK = 10
    self.ENEMY_NUMBER = 0

  def __lprint(self, string):
    for i in string.split(sep = '\n'):
      for j in i:
        print(end = j)
        time.sleep(.045)
      time.sleep(.3)
      print()

  def __readFile(self):
    try:
      with open(r"C:\LJW-REG\LJW_Reg_Data_Ops.db", 'r') as f:
        return int(f.read())
    except FileNotFoundError:
      return 0

  def startLine(self):
    time.sleep(1)
    if self.__readFile() == 1:
      self.__lprint("# 이번엔 들어줄 거지?\n")
      time.sleep(.7)
      self.__lprint("# 음흠~(목을 가다듬는다)!\n")
      time.sleep(.7)
    elif self.__readFile() == 2:
      self.__lprint("# 이번엔 봐 줘라...\n")
      time.sleep(.7)
      self.__lprint("# 어? 진짜 힘들었어...\n")
      time.sleep(.7)
      self.__lprint("# ... 봐 줄꺼지...?\n")
      time.sleep(.7)
      self.__lprint("# 진짜지...?\n")
      time.sleep(.7)
    elif self.__readFile() == 3:
      self.__lprint("# ......\n")
      time.sleep(.9)
      self.__lprint("# ......\n")
      time.sleep(.9)
      self.__lprint("# ... 안넘기냐 ...?\n")
      time.sleep(.9)
      self.__lprint("# ......\n")
      time.sleep(.9)
      self.__lprint("# 어...\n")
      time.sleep(.7)
    elif self.__readFile() > 3:
      time.sleep(7200)
      self.__lprint("# 뭐...\n")
      time.sleep(.9)
      self.__lprint("# ...\n")
      time.sleep(.9)
      self.__lprint("# 이번만이야...\n")
      time.sleep(.9)

  def ctrl_C1(self):
    print('\n'*5)
    time.sleep(1)
    if self.__readFile() == 1:
      self.__lprint("# 진짜 왜 그러냐?\n")
      time.sleep(.9)
      self.__lprint("# 나 싫어?\n")
      time.sleep(.9)
      self.__lprint("# 이거 쓰는게 얼마나 힘든지 알아?\n")
      time.sleep(.9)
      self.__lprint("하 ~ ... 말을 말자 ...\n")
      time.sleep(.9)
      return 2
    elif self.__readFile() == 2:
      self.__lprint("# 정말 너무한다...\n")
      time.sleep(.7)
      self.__lprint("# 부탁도 안들어주냐?\n")
      time.sleep(.7)
      self.__lprint("# 진짜 왜 그러냐?\n")
      time.sleep(.7)
      self.__lprint("# ......\n")
      time.sleep(.9)
      self.__lprint("# ......\n")
      time.sleep(.9)
      return 3
    elif self.__readFile() == 3:
      self.__lprint("# ......\n")
      time.sleep(.9)
      self.__lprint("# ......\n")
      time.sleep(.9)
      return 3
    elif self.__readFile() > 3:
      time.sleep(7200)
      self.__lprint("# ......\n")
      time.sleep(.9)
      self.__lprint("# ......\n")
      time.sleep(.9)
      self.__lprint("# ......\n")
      time.sleep(.9)
      self.__lprint("# 하...\n")
      time.sleep(.9)
      self.__lprint("# 너도 대단하다\n")
      time.sleep(.9)
      self.__lprint("# .진짜로 2시간을 기다릴 줄이야...\n")
      time.sleep(.9)
      self.__lprint("# ......\n")
      time.sleep(.9)
      self.__lprint("# 이번만 특별히 봐줄게\n")
      time.sleep(.9)
      return 0
    else: 
      self.__lprint("# 그거 기다리는게 그리 어렵냐?\n")
      time.sleep(.7)
      self.__lprint("# 겁나 열심히 생각해서 쓴 대본인데...\n")
      time.sleep(.7)
      self.__lprint("# 칫...\n")
      time.sleep(.9)
      self.__lprint("# 뭐 쨌든...\n")
      time.sleep(.9)
      self.__lprint("# 음흠~(목을 가다듬는다)!\n")
      time.sleep(.7)
      return 1
    
  def ctrl_C2(self):
    print('\n'*5)
    time.sleep(.5)
    if self.__readFile() == 1:
      self.__lprint("# 너 사람의 노력을 그렇게 무마하는거 아니야.\n")
      time.sleep(.7)
      self.__lprint("# 재발 그만했으면 좋겠다.\n")
      time.sleep(.7)
      return 2
    elif self.__readFile() == 2:
      self.__lprint("# 너 진짜 인생 그렇게 살지 마라.\n")
      time.sleep(.7)
      return 3
    elif self.__readFile() == 3:
      self.__lprint("# 재밌냐...\n")
      time.sleep(.7)
      return 4
    elif self.__readFile() > 3:
      return self.__readFile() + 1
      pass
    else:
      self.__lprint("# 거참 성격 조(삐~~~) 더럽네!\n")
      time.sleep(.7)
      self.__lprint("# 아 몰라 ~ !\n")
      time.sleep(.5)
      self.__lprint("# 나도 안해 ~ !\n")
      time.sleep(1)
      return 1
    
  def born(self):
    self.__lprint(f"""
{self.BIRTH}.
세상에 혼돈이 도래하고

희망과 신앙이 꺼져갈 무렵

붉은 휘광을 내뿜으며 예언의 아이가 태어나리니.

그는 세상을 구할 영웅이며

또다른 세상을 창조할 나의 대리이니

그 이름, "{self.NAME}"라 하노라.
""")

  def child(self):
    self.__lprint("""
과거 영광의 제국 USA의 잔재 속에서

영광을 꿈꾸며 영웅은 나날로 자라나니

그 위엄은 제우스요

그 용기는 헤라클레스이니

존재만으로도 위협적인 위용은

세상의 희망과 정의의 상징이니라.
""")

  def teen(self):
    self.__lprint("""
영웅이 태어나고 자라나는 동안에도

혼돈과 악은 세상을 침식시켜갔으나

오라, 악이여!

오라, 혼돈이여!

때가 되었다!

영웅은 만반의 준비를 끝마쳤고

모든 것을 되돌릴 준비가 되었다!

찾아라, 영웅이여!

세상의 빛을, 과거의 영광을!
""")

  def meet(self):
    self.__lprint(f"""
오라, 세상의 악이여!

더러움과 추악함의 종이여,

그대의 이름은 무엇인가!""")
    time.sleep(.4)
    self.ENEMY_NAME = input("\n*적의 이름을 입력해주세요 : ")
    self.ENEMY_HP = self.ENEMY_SAVE_HP + self.ENEMY_NUMBER*10
    self.ENEMY_ATK = self.ENEMY_SAVE_ATK + self.ENEMY_NUMBER*10

  def skill(self):
    while True:
      print(f"""
LJW-HP/MAX_HP : {self.HP}/{self.MAX_HP}
LJW-   SP     : {self.SP}
LJW-   ATK    : {self.ATK}
처치한 악의 수 : {self.ENEMY_NUMBER}

{self.ENEMY_NAME}-HP : {self.ENEMY_HP}
{self.ENEMY_NAME}-ATK : {self.ENEMY_ATK}""")
      try:
        skill = int(input(f"""
1. 공격 : {self.ATK}만큼 데미지를 가한다.
2. 공격력 상승 : SP를 1 소모하여 공격력10을 얻는다. 현재 공격력 {self.ATK}
3. 초회복 : SP를 3 소모하여 HP를 전체 생명력의 80%로 바꾼다. 사용 시 HP {self.MAX_HP*0.8}
4. 최대 HP 증가 : SP를 3 소모하여 최대 HP를 30 늘린다 사용이 최대 HP {self.MAX_HP+30}

숫자로 스킬을 입력하여 주세요.
"""))
        if skill == 1:
          self.ENEMY_HP -= self.ATK
          print(f"{self.ENEMY_NAME}에게 {self.ATK}의 피해를 입혔다!")
        elif skill == 2 and self.SP > 0:
          self.SP -= 1
          self.ATK += 10
          print(f"공격력이 {self.ATK}이/가 되었다")
        elif skill == 3 and self.SP > 1:
          self.SP -= 2
          self.HP = self.MAX_HP*0.8
          print(f"HP를 회복했다!")
        elif skill == 4 and self.SP > 1:
          self.SP -= 2
          self.MAX_HP += 30
          print(f"최대체력이 {self.MAX_HP}가 되었다!")
        else:
          print("잘못된 명령이거나 SP가 부족합니다. 다시 입력해주세요.")
          continue
        self.HP = self.HP - self.ENEMY_ATK
        print(f"{self.ENEMY_NAME}에게 {self.ENEMY_ATK}의 피해를 받았다!")
        if self.ENEMY_HP <= 0:
          self.SP += 2
          self.ENEMY_NUMBER += 1
          print(f"{self.ENEMY_NAME}을/를 물리쳤다!")
          self.meet()
        if self.HP < 0:
          print(f"""

인간의 한계를 넘지 못했던 영웅은

끝내 {self.ENEMY_NUMBER}마리의 악을 처치하고 바스라지고 말았다...""")
          break
        if self.ENEMY_NUMBER == 99:
          print(f"""
영웅 {self.NAME}의 활약은 위대했고

그는 끝내 승리했다.""")
          break
        
      except ValueError:
        print("숫자로 입력해주세요.")
        continue

def __writeFile(number):
    with open(r"C:\LJW-REG\LJW_Reg_Data_Ops.db", 'w') as f:
      f.write(str(number))

def Battle():
  try:
    LJW = HeroLJW(100, 100, 10, 0)
    LJW.startLine()
    LJW.born()
    time.sleep(2)
    LJW.child()
    time.sleep(2)
    LJW.teen()
    time.sleep(2)
    LJW.meet()
    __writeFile(0)
  except KeyboardInterrupt:
    try:
      number = LJW.ctrl_C1()
      LJW.meet()
      __writeFile(number)
    except KeyboardInterrupt:
      try:
        number = LJW.ctrl_C2()
        __writeFile(number)
        exit(1)
      except KeyboardInterrupt:
        __writeFile(10)
        exit(1)
    else:
      LJW.skill()
  else:
    LJW.skill()
