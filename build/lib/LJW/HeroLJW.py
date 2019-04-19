import time

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

  def born(self):
    print(f"""
{self.BIRTH}.
세상에 혼돈이 도래하고

희망과 신앙이 꺼져갈 무렵

붉은 휘광을 내뿜으며 예언의 아이가 태어나리니.

그는 세상을 구할 영웅이며

또다른 세상을 창조할 나의 대리이니

그 이름, "{self.NAME}"라 하노라.
""")

  def child(self):
    print("""
과거 영광의 제국 USA의 잔재 속에서

영광을 꿈꾸며 영웅은 나날로 자라나니

그 위엄은 제우스요

그 용기는 헤라클레스이니

존재만으로도 위협적인 위용은

세상의 희망과 정의의 상징이니라.
""")

  def teen(self):
    print("""
영웅이 태어나고 자라나는 동안에도

혼돈과 악은 세상을 침식시켜갔으나

오라, 악이여!

오라, 혼돈이여!

때가 되었다!

영웅은 만반의 준비를 끝마쳤고

모든 것을 되돌릴 준비가 되었다!

찾아라, 영웅이여!

세상의 빛을, 과거의 영광을!""")

  def meet(self):
    self.ENEMY_NAME = input(f"""
오라, 세상의 악이여!

더러움과 추악함의 종이여, 그대의 이름은 무엇인가!

*적의 이름을 입력해주세요 : """)
    self.ENEMY_HP = self.ENEMY_SAVE_HP + self.ENEMY_NUMBER*10
    self.ENEMY_ATK = self.ENEMY_SAVE_ATK + self.ENEMY_NUMBER*10

  def skill(self):
    self.meet()
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
        elif skill == 3 and self.SP > 2:
          self.SP -= 3
          self.HP = self.MAX_HP*0.8
          print(f"HP를 회복했다!")
        elif skill == 4 and self.SP > 2:
          self.SP -= 3
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
    


def Battle():
  LJW = HeroLJW(100, 100, 10, 0)
  LJW.born()
  time.sleep(5)
  LJW.child()
  time.sleep(5)
  LJW.teen()
  time.sleep(5)
  LJW.skill()

Battle()
